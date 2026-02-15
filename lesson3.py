# 1. git push
# i. git push sends your local commits to a remote repository (like GitHub, GitLab, Bitbucket).

# Think:

# “I made changes locally; now I want the remote to see them.”

# Basic syntax:

# git push <remote> <branch>

# Defaults:

# <remote> → usually origin

# <branch> → usually main or master

# Example:

# git push origin main

# Pushes your current commits from local main branch to remote origin.

# Example 1: Simple push after a commit

# You’ve just made a commit locally:

# git add lesson_01.py
# git commit -m "docs: add lesson 1 instructions"
# git push

# If your local branch tracks a remote branch, just git push works.

# Remote now has your new file.

# Example 2: Push a new branch

# You created a new branch feature/exercises:

# git checkout -b feature/exercises
# git add lesson_02.py
# git commit -m "docs: add lesson 2 exercises"
# git push -u origin feature/exercises

# -u sets upstream, so future git push knows where to push automatically.

# Remote now has a new branch with your commit.

# Example 3: Force push (careful!)

# Sometimes you rewrite history (like git commit --amend) and need to overwrite remote:

# git push origin main --force

# ⚠️ This can overwrite remote changes, so only do if you know no one else relies on this branch.

# Example 4: Push tags

# Tags are used for releases:

# git tag v1.0
# git push origin v1.0

# Pushes the tag v1.0 to remote so others can reference this exact commit.

# 2. git fetch
# i. git fetch downloads updates from a remote repository but:
# ❌ does NOT change your working directory

# ❌ does NOT change your current branch

# ✅ updates remote-tracking branches (origin/main, etc.)

# Mental model:

# “Let me see what changed over there, without touching my work.”

# Basic form:

# git fetch

# Example 1: Fetch latest changes safely

# You want to check if the remote has new commits.

# git fetch

# Then inspect:

# git log main..origin/main

# Meaning:

# Shows commits that exist on remote but not locally

# Your code remains untouched

# Example 2: Fetch a specific remote

# You have multiple remotes (e.g., origin, upstream).

# git fetch upstream

# What happens:

# Downloads updates from upstream

# Updates upstream/main, upstream/dev, etc.

# Still no local changes

# Example 3: Compare before merging

# You want to see differences before integration.

# git fetch
# git diff main origin/main

# Meaning:

# Shows exact code changes

# You decide whether to merge

# This is the phase git pull skips.

# Example 4: Fetch without merging, then merge manually

# You want full control.

# git fetch
# git merge origin/main

# What happens:

# First command updates knowledge

# Second command updates reality

# This is explicit Git usage.

# 3. git merge
# i. "git merge" combines another branch into your current branch.

# Key points:

# It changes your branch

# It may create a merge commit

# Conflicts (if any) happen here, not during fetch

# Mental model:

# “Bring that branch’s history into this branch.”

# Basic form:

# git merge <branch>

# Example 1: Fast-forward merge (no conflict, no merge commit)

# You’re on main. No one changed main, but feature/loops has new commits.

# git merge feature/loops

# What happens:

# main simply moves forward

# No merge commit created

# This is the cleanest merge.

# Example 2: Merging remote-tracking branch after fetch

# You fetched new remote changes and want to integrate them.

# git fetch
# git merge origin/main

# What happens:

# Combines fetched remote commits into your local branch

# This is exactly what git pull hides

# Example 3: Merge with conflicts

# Both you and a teammate edited the same lines.

# git merge origin/main

# Git responds with a conflict.

# Resolution flow:

# fix conflicts in files
# git add .
# git commit

# Result:

# Merge commit created

# Conflict resolved explicitly

# Example 4: Abort a merge

# You start a merge and realize it’s wrong or too messy.

# git merge --abort

# What happens:

# Repository returns to pre-merge state

# No history damage

# This is a safety valve many beginners don’t know.

# 4. "merge conflict"
# i. A merge conflict happens when:

# Git tries to merge two histories

# Both modified the same part of the same file

# Git cannot decide which version is correct

# Important:

# Git never guesses. It asks you.

# *What a conflict looks like

# Inside a conflicted file, Git marks it clearly:

# <<<<<<< HEAD
# print("Hello from main")
# =======
# print("Hello from feature")
# >>>>>>> feature-branch

# Meaning:

# HEAD → your current branch

# Bottom section → incoming branch

# Your job → choose or combine

# ii. The universal conflict-resolution workflow

# Run merge (conflict occurs)

# Open conflicted files

# Decide what code should survive

# Remove conflict markers

# Stage resolved files

# Commit the merge

# git add .
# git commit

# iii. Four concrete conflict examples
# Example 1: Same line edited differently

# Situation:
# You change a print statement in main.
# Your teammate changes the same line in feature.

# Result: conflict.

# Resolution:
# Pick one version or combine:

# print("Hello from main and feature")

# Then:

# git add file.py
# git commit

# Example 2: One deletes a file, the other edits it

# Situation:

# Branch A deletes notes.py

# Branch B edits notes.py

# Git asks:

# “Delete or keep?”

# Resolution options:

# Keep file → stage it

# Delete file → git rm notes.py

# Then commit.

# Example 3: Same file, different nearby lines

# Situation:
# Two branches modify adjacent lines in a function.

# Git may still conflict because context overlaps.

# Resolution:
# Manually merge logic carefully, ensuring correctness.

# Then:

# git add .
# git commit

# Example 4: Conflict during git pull

# Situation:
# You run:

# git pull

# Conflict appears.

# 5. git pull
# i. "git pull" brings changes from a remote repository into your local branch.

# Under the hood, it does two steps:

# git fetch  +  git merge

# So mentally:

# “Get remote changes, then integrate them into my current branch.”

# Basic form:

# git pull <remote> <branch>

# Most of the time:

# git pull

# Example 1: Simple pull (most common)

# You’re on main, and someone pushed new commits to origin/main.

# git pull

# What happens:

# Fetches latest commits from the remote

# Merges them into your local main

# Use this before you start working.

# Example 2: Pull from a specific branch

# You want to pull changes from origin/main while on another branch.

# git pull origin main

# What happens:

# Downloads changes from origin/main

# Merges them into your current branch

# Useful when syncing a feature branch with main.

# Example 3: Pull with rebase (clean history)

# You want to avoid merge commits.

# git pull --rebase

# What happens:

# Fetches remote changes

# Replays your local commits on top of them

# Result:

# Linear, cleaner commit history

# Common in professional workflows

# Example 4: Pull after a conflict exists

# You try:

# git pull

# Git responds with a merge conflict.

# What you do:

# Open conflicted files

# Resolve conflicts manually

# Stage fixes:

# git add .

# Complete the merge:

# git commit

# This finalizes the pull.