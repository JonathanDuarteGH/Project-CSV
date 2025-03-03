# Project-CSV
***Make sure python (any recent stable version) is installed***

## How to start an empty github project for Python

1. Create an empty repo on github
2. Launch gitbash in VS Code terminal
3. Navigate to directory in gitbash if haven't done so
4. Clone the repo: ```git clone https://github.com/[username]/[repo_name]```
5. Make a new ```.py``` file
6. Copy/Paste/Add any files to folder
7. Open ```.py``` file in VS Code
8. Select desired Python Interpreter by typing ```>``` in search bar 
9. Type ```python -m venv .venv``` in git bash terminal
10. New environment will be created. Click **Yes** from prompt
11. Activate Virtual Environment:  ```source .venv/Scripts/activate```
12. Type ```pip install [your desired packages]``` to install any packages
13. Type ```pip install -r requirements.txt``` to create "requirements.txt" file
14. Type ```pip freeze > requirements.txt``` to save current list of installed packages
15. Type ```pip install pipreqs``` to install only packages being used in current project
16. Type ```pip install pipreqs --force```, if necessary
17. Type ```pipreqs .``` to record the packages and libraries used in the python.py project
18. Type ```pip freeze > requirements.txt``` to save current list of installed packages

## How to use a repo from a github project for Python
1. Create an empty repo on github
2. Launch gitbash in VS Code terminal
3. Navigate to directory in gitbash if haven't done so
4. Clone the repo: ```git clone https://github.com/[username]/[repo_name]```
5. Activate Virtual Environment:  ```source .\venv\Scripts\activate```
6. Install the requirements: ```pip install -r requirements.txt```

## How to uninstall all packages in Virtual Environment for Python
1. Type: ```pip freeze > requirements.txt```
2. Type: ```pip uninstall -r requirements.txt -y```
3. Type: ```git rm file1.txt``` to remove file for Git repository **and** the filesystem
4. Type: ```git rm --cached file1.txt``` to remove file for only Git repository **and not** the filesystem

https://datalumina.clickup.com/docs/9015213037/d/h/8cnjezd-17675/ddd52c673443975

## How to automate uninstall on git bash
1. Launch Notepad
2. Type: ```pip uninstall <package-name>```
3. Repeat <b>Step 2</b> for multiple packages:
```plaintext
pip uninstall <package-name2>
pip uninstall <package-name3>
...
pip uninstall <package-name(n)>
```
4. File -> Save as
5. Under Save as type dropdown -> Select <b>All types (* . *)</b> -> Save to desired folder
6. Type ```file-name.bat``` and **Save**
7. Launch Gitbash terminal
8. Navigate to where .bat file was saved:
```bash
path/to/your/file-name.bat
```
10. Acitvate cmd under Gitbash by typing ```cmd```
11. Type the following to activate the automation:
```bash
file-name.bat
```
12. After finishing type: ```exit``` to exit cmd