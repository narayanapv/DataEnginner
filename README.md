# DataEnginner
datapv
this is about data engineer

Git commands:

• git config --global user.name "Your Name": Sets your commit author name globally.
• git config --global user.email "your.email@example.com": Sets your commit email address globally.
• git init: Initializes a brand-new, empty local Git repository in the current folder.
• git clone <url>: Downloads a copy of an existing remote repository to your local machine.
2. The Daily Workflow (Stage & Commit)
This is the loop you will use constantly to save changes locally.
• git status: Shows which files are modified, untracked, or staged for the next snapshot.
• git add <file>: Moves specific file modifications to the staging area.
• git add .: Stages all modified and new files at once.
• git commit -m "your message": Saves the staged snapshot securely into project history.
• git diff: Shows exact line-by-line differences of unstaged changes.
3. Branching & Merging
Used to build separate features without disturbing stable code.
• git branch: Lists all local branches; a star indicates the active branch.
• git switch <branch-name> or git checkout <branch-name>: Switches your working tree to the specified branch.
• git switch -c <branch-name> or git checkout -b <branch-name>: Creates a new branch and immediately switches to it.
• git merge <branch-name>: Combines the specified branch's history into your current active branch.
• git branch -d <branch-name>: Deletes a branch safely (only if it has been fully merged).
4. Sharing & Collaboration
Commands for interacting with remote platforms like GitHub, GitLab, or Bitbucket.
• git remote add origin <url>: Links your local repository to a remote server URL.
• git fetch: Downloads tracking history and objects from the remote repo without altering your local files.
• git pull: Fetches remote changes and immediately merges them into your current branch.
• git push origin <branch-name>: Uploads your local commits to the designated branch on the remote server.
5. Inspecting History & Undoing Mistakes
• git log --oneline: Shows a condensed, clean list of past commits.
• git stash: Temporarily shelves uncommitted changes so you can switch tasks cleanly.
• git restore <file>: Discards unstaged modifications in a file, resetting it to the last commit.
• git reset --hard HEAD: Completely wipes out all local staged and unstaged changes since your last commit (use with caution).
