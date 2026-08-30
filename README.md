# MY COURSES
## How to set up my project ?

1. [Download Python](https://www.python.org/downloads/release/python-3147/) Windows installer (64-bit)
2. Re-install Python and add this 2n option

    ![Python option](./Images/Python%20installed%20option.png)

3. Verify that Python is installed: `python --version`
4. Create a specific place (virtual environment) for Python depedencies: `python -m venv .venv` 
5. Activate this virtual environment: `./.venv/scripts/activate.ps1`
6. Install dependencies: `pip install mkdocs mkdocs-material`
7. Freeze dependencies: `pip freeze -r requirements.txt > requirements.txt`
8. Initalize website's structure: `mkdocs new .`
9. To start and get website's link (locally): `mkdocs serve`
10. Create Github repository
11. Initialize local repository (via terminal) `git init`
12. Link Github repository and local repository `git remote add origin https://github.com/PaulineB15/mycourses.git`




## How to deploy this project on another laptop ?
1. Do step 1 to 5 from previous list
2. Install dependencies `pip install -r requirements.txt`
3. Activate the virtual environment `.\.venv\Scripts\activate`
4. To start and get website's link (locally): `mkdocs serve`
5. Create course contents (Markdown), `git add`, `git commit`, `git push`
6. Publish website on Github: `mkdocs gh-deploy`