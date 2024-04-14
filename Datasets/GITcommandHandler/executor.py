"""

The subprocess module is used to spawn new processes, connect to their input/output/error pipes, and obtain their return codes. It allows you to run external programs or system commands from within a Python script.


"""

import subprocess

# Git Command Functions

def gitInit():
    # Initialize a new Git repository
    print("Running: git init")
    subprocess.run(['git', 'init'])

def gitAdd(files=None):
    # Add file(s) to the staging area
    # files: dot or file names
    print(f"Running: git add {' '.join(files)}")
    if files:
        subprocess.run(['git', 'add'] + files)
    else:
        subprocess.run(['git','add','.'])

def gitCommit(message):
    # Commit changes with a message
    if not message:
        message = 'minor changes'
    print(f"Running: git commit -m '{message}'")
    subprocess.run(['git', 'commit', '-m', message])

def gitStatus():
    # Check the status of the repository
    print("Running: git status")
    subprocess.run(['git', 'status'])

def gitLog():
    # View commit history
    print("Running: git log")
    subprocess.run(['git', 'log'])

def gitBranch():
    # List all branches
    print("Running: git branch")
    subprocess.run(['git', 'branch'])

def gitCreateBranch(branch):
    # Create a new branch
    # branch: name of the new branch
    print(f"Running: git branch {branch}")
    subprocess.run(['git', 'branch', branch])

def gitCheckout(branch):
    # Switch to a different branch
    # branch: name of the new branch
    print(f"Running: git checkout {branch}")
    subprocess.run(['git', 'checkout', branch])

def gitMerge(branch):
    # Merge changes from a branch into the current branch
    # branch: name of the new branch
    print(f"Running: git merge {branch}")
    subprocess.run(['git', 'merge', branch])

def gitRemoteAdd(remote_name, remote_url):
    # Add a remote repository
    # remote_name: origin or upstream
    print(f"Running: git remote add {remote_name} {remote_url}")
    subprocess.run(['git', 'remote', 'add', remote_name, remote_url])

def gitRemoteRemove(remote_name):
    # Remove a remote repository
    # remote_name: origin or upstream
    print(f"Running: git remote remove {remote_name}")
    subprocess.run(['git', 'remote', 'rm', remote_name])

def gitPush(remote_name, branch):
    # Push changes to a remote repository
    # remote_name: origin or upstream
    print(f"Running: git push {remote_name} {branch}")
    subprocess.run(['git', 'push', remote_name, branch])

def gitPull(remote_name, branch):
    # Pull changes from a remote repository
    print(f"Running: git pull {remote_name} {branch}")
    subprocess.run(['git', 'pull', remote_name, branch])

def gitTag(tag_name, commit_hash):
    # Create a new tag referencing a specific commit
    print(f"Running: git tag {tag_name} {commit_hash}")
    subprocess.run(['git', 'tag', tag_name, commit_hash])

def gitAddInteractive():
    # Interactively stage specific changes within a file
    print("Running: git add -p")
    subprocess.run(['git', 'add', '-p'])

def gitRemoveFile(file_path, force=False):
    # Remove a file from the working directory and staging area
    if force:
        print(f"Running: git rm -f {file_path}")
        subprocess.run(['git', 'rm', '-f', file_path])
    else:
        print(f"Running: git rm {file_path}")
        subprocess.run(['git', 'rm', file_path])

def gitIgnoreFile(file_path):
    # Add a file to .gitignore
    print(f"Running: git update-index --ignore-add {file_path}")
    subprocess.run(['git', 'update-index', '--ignore-add', file_path])

def gitUndoChanges(file_path=None):
    # Undo changes made to a specific file or reset it from the staging area
    if file_path:
        print(f"Running: git checkout {file_path}")
        subprocess.run(['git', 'checkout', file_path])
    else:
        print(f"Running: git reset HEAD {file_path}")
        subprocess.run(['git', 'reset', 'HEAD', file_path])

def gitFetch():
    # Fetch the latest changes from a remote repository
    print("Running: git fetch")
    subprocess.run(['git', 'fetch'])

def gitRebase(branch):
    # Rebase the current branch on top of another branch
    print(f"Running: git rebase {branch}")
    subprocess.run(['git', 'rebase', branch])

def gitViewDifferences(file_path=None):
    # View differences between the working directory and the index or a specific file
    if file_path:
        print(f"Running: git diff {file_path}")
        subprocess.run(['git', 'diff', file_path])
    else:
        print("Running: git diff")
        subprocess.run(['git', 'diff'])

def gitShowStagedChanges():
    # Show changes staged in the index
    print("Running: git diff --cached")
    subprocess.run(['git', 'diff', '--cached'])

def gitStash():
    # Temporarily save uncommitted changes
    print("Running: git stash")
    subprocess.run(['git', 'stash'])

def gitPopStash():
    # Apply the most recent stashed changes
    print("Running: git stash pop")
    subprocess.run(['git', 'stash', 'pop'])

def gitCherryPick(commit_hash):
    # Select and apply a specific commit from another branch
    print(f"Running: git cherry-pick {commit_hash}")
    subprocess.run(['git', 'cherry-pick', commit_hash])


functionMap = {
    1: gitInit,
    2: gitAdd,
    3: gitCommit,
    4: gitStatus,
    5: gitLog,
    6: gitBranch,
    7: gitCreateBranch,
    8: gitCheckout,
    9: gitMerge,
    10: gitRemoteAdd,
    11: gitRemoteRemove,
    12: gitPush,
    13: gitPull,
    14: gitTag,
    15: gitAddInteractive,
    16: gitRemoveFile,
    17: gitIgnoreFile,
    18: gitUndoChanges,
    19: gitFetch,
    20: gitRebase,
    21: gitViewDifferences,
    22: gitShowStagedChanges,
    23: gitStash,
    24: gitPopStash,
    25: gitCherryPick
}
