
import os
import git
import time
from threading import Thread
from flask import Flask, jsonify, render_template
from g4f.client import Client

app = Flask(__name__)

# Repository details
REPO_URL = 'https://github.com/SidharthAnand04/CodeSentinel.git'
REPO_PATH = './CodeSentinel'
POLL_INTERVAL = 30  # Poll every 30 seconds

# Clone the repository if it does not exist
if not os.path.exists(REPO_PATH):
    repo = git.Repo.clone_from(REPO_URL, REPO_PATH)
else:
    repo = git.Repo(REPO_PATH)

def fetch_latest_commits():
    origin = repo.remotes.origin
    origin.fetch()
    return origin.refs.main.commit.hexsha

def collect_commit_info():
    commit_info = ""
    for commit in repo.iter_commits('main'):
        if "Add LLM code review response" in commit.message:
            continue
        commit_info += f"Commit: {commit.hexsha}\n"
        commit_info += f"Author: {commit.author.name} <{commit.author.email}>\n"
        commit_info += f"Date: {commit.committed_datetime}\n"
        commit_info += f"Message: {commit.message}\n"
        commit_info += "Changed files:\n"
        for file in commit.stats.files:
            commit_info += f"  - {file}\n"
            file_path = os.path.join(REPO_PATH, file)
            if os.path.exists(file_path):
                with open(file_path, 'r') as f:
                    file_contents = f.read()
                    commit_info += f"    Contents:\n{file_contents}\n"
        commit_info += "-" * 50 + "\n"
    return commit_info

def query_llm(input_text):
    client = Client()
    with open('prompt.txt', 'r') as f:
        prompt = f.read()
        
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": f"{prompt}\n{input_text}"}],
    )
    return response.choices[0].message.content

def process_commits():
    last_processed_commit = None
    while True:
        try:
            latest_commit = fetch_latest_commits()

            if latest_commit != last_processed_commit:
                repo.remotes.origin.pull()
                
                commit_info = collect_commit_info()

                with open("commit_info.txt", "w") as f:
                    f.write(commit_info)
                
                llm_response = query_llm(commit_info)
                print("LLM Response:", llm_response)
                
                response_file_path = os.path.join(REPO_PATH, "llm_response.md")
                
                if os.path.exists(response_file_path):
                    os.remove(response_file_path)
                
                with open(response_file_path, "w") as f:
                    f.write(llm_response)
                
                repo.index.add(["*"])
                repo.index.commit("Add LLM code review response")
                repo.remotes.origin.push()

                last_processed_commit = latest_commit
        
        except Exception as e:
            print(f"An error occurred: {e}")
        
        time.sleep(POLL_INTERVAL)

@app.route('/')
def index():
    with open("commit_info.txt", "r") as f:
        commit_info = f.read()
    with open("llm_response.txt", "r") as f:
        llm_response = f.read()
    return render_template('index.html', commit_info=commit_info, llm_response=llm_response)

@app.route('/status', methods=['GET'])
def status():
    return jsonify({'message': 'Polling for updates'})

if __name__ == '__main__':
    # Start the background thread for polling
    polling_thread = Thread(target=process_commits, daemon=True)
    polling_thread.start()

    # Start the Flask server
    app.run(host='0.0.0.0', port=5000)
