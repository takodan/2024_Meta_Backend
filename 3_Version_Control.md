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
## Module 4: Graded Assessment