import git
import os

# https://github.com/SidharthAnand04/CodeSentinel


# Clone the repository if it does not exist
REPO_URL = 'https://github.com/SidharthAnand04/CodeSentinel.git'
REPO_PATH = './CodeSentinel'

# Clone the repository if it doesn't exist
if not os.path.exists(REPO_PATH):
    git.Repo.clone_from(REPO_URL, REPO_PATH)

# Open the repository


















































































repo = git.Repo(REPO_PATH)

# Fetch the latest commits
# repo.remotes.origin.fetch()
repo.remotes.origin.pull()

# Print all commits
for commit in repo.iter_commits('main'):
    print(f"Commit: {commit.hexsha}")
    print(f"Author: {commit.author.name} <{commit.author.email}>")
    print(f"Date: {commit.committed_datetime}")
    print(f"Message: {commit.message}")
    print("-" * 50)

if __name__ == "__main__":
    print("List of commits from CodeSentinel repository:")
    for commit in repo.iter_commits('main'):
        print(f"Commit: {commit.hexsha}")
        print(f"Author: {commit.author.name} <{commit.author.email}>")
        print(f"Date: {commit.committed_datetime}")
        print(f"Message: {commit.message}")
        print("-" * 50)
