# Version Control
## Module 1 Software Collaboration
1. GitHub Git Cheat Sheet: https://education.github.com/git-cheat-sheet-education.pdf
2. Centralized version control system:
    1. a server acts as the main repository that stores every version of the code.
    2. every user commits directly to the main branch on the server.
3. Distributed version control system: 
    1. every single client will have a copy of the entire history.
    2. send a request to the master repository to get new changes or merge your local changes.
4. other tools and procedures in the software development process:
    1. Workflow: to ensure code is managed correctly and reduce mistakes.
    2. Continuous Integration: automatically compile the project and test on every code change.
    3. Continuous Delivery: automatically packages and prepares the application for deployment.
    4. Continuous Deployment: Deploy software frequently and safely.
5. Staging environment: a mimic of your production environment. for submitting new features, testing, data migrations, and configuration changes.
6. Production environment: for people to see and interact with. Look out for downtime, vulnerabilities, and reputation.


## Module 2: Command Line
1. Unix / Linux commands
```bash
cd
touch
mkdir # -p flag to create the parent directories if they do not exist
history
man # manual for a command
ls # -l -a
pwd
cp
mv
less # read the contents of a text file one page (one screen) at a time
echo
chmod
clear
cat
wc # word count, line word bytes
```
2. Pipe, Redirection, grep
```bash
# Pipe: passes stdout as the stdin to another command
cat file1.txt file2.txt | wc # passes cat stdout to wc stdin


# Redirection: passes stdout to a file
cat > file.txt # take stdin to file.txt, ctrl+D to end stdin
ls -l > file.txt # take stdout of (ls -l) to file.txt

# 0 for stdin, 1 for stdout, 2 for stderr
ls /not_exist_dir 2 > file.txt # take stderr to file.txt
ls > file.txt 2>&1 # take stdout and stderr to file.txt


# global regular expression print (grep): use regex for searching
grep Name name.txt # return strings that had "Name" in name.txt
# -i: ignore case; -w: exact match
ls / | grep zip # search zip in /
```


## Module 3: Git
1. `git clone <HTTPS URL>`
2. Git workflow: Modified -> (git add) -> Staged -> (git commit) -> Committed
3. git command
```bash
git init # initialized a directory as a Git repository
git status
git add fine_name
git restore --stage file_name # unstage the file
git commit -m "commit message"

git checkout -B branches/new_branch # move to branches/new_branch. -B flag will create a branch if it doesn’t exist; otherwise, reset it.
git branch # show branches

# Everything mentioned above happens locally

git git push -u remote_name_origin branches/new_branch # -u flag sets source remote information for the branch you're pushing.
git pull

# link to a remote repository
git remote -v # show remote repository. -v flag shows a remote with more detail (more verbose)
git remote add remote_name_origin remote_url # sets remote repository for the current git
git push remote_name_origin branch_name
# if you added a new remote, you may also want to checkout the remote branch.

# HEAD
cat .git/branch # show reference path
cat .git/refs/heads/main # show reference id


# Diff
git diff HEAD uncommited_file # compare files

git log --pretty=oneline # --pretty=oneline flag shows each commit id on a separate line
git diff id_1 id_2 # compare commits

git main branches/new_branch # compare branches


# Blame
git blame file_name # shows: <commit_id> (<author> <date> <time> <changes_line_number>) <content>
git blame -L start_line_number,end_line_number file_name # -L flag shows content only between start to end lins.
git log -p commit_id # log detail of the changes
```


## Module 4: Graded Assessment
1. some recap
2. class repo is expired