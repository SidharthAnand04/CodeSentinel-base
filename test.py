import os
import git
from g4f.client import Client

# Repository details
REPO_URL = 'https://github.com/SidharthAnand04/CodeSentinel.git'
REPO_PATH = './CodeSentinel'

# Clone the repository if it does not exist
if not os.path.exists(REPO_PATH):
    repo = git.Repo.clone_from(REPO_URL, REPO_PATH)
else:
    repo = git.Repo(REPO_PATH)

# Fetch the latest commits
origin = repo.remotes.origin
origin.pull()

# Collect commit information along with changed files and their contents
commit_info = ""
commit_count = 0
for commit in repo.iter_commits('main'):
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
    commit_count += 1

if commit_count == 0:
    commit_info = "No commits found in the repository."

# Function to query the LLM using g4f client
def query_llm(input_text):
    client = Client()
    with open('prompt.txt', 'r') as f:
        prompt = f.read()
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": f"{prompt}\n{input_text}"}],
    )
    return response.choices[0].message.content

# Query the LLM to find out how many files have changed
# try:
# save commit info to a file
with open("commit_info.txt", "w") as f:
    f.write(commit_info)
    
llm_response = query_llm(commit_info)
print("LLM Response:", llm_response)

# Construct the correct file path
response_file_path = os.path.join(REPO_PATH, "llm_response.md")

if os.path.exists(response_file_path):
    # If the file exists, replace it
    os.remove(response_file_path)


# Save LLM response to a file
with open(response_file_path, "w") as f:
    f.write(llm_response)

# Stage and commit the LLM response
repo.index.add(["*"])
repo.index.commit("Add LLM code review response")
origin.push()
        
# except Exception as e:
#     print(f"An error occurred: {e}")
