# AgriHire Solutions Equipment and Order Management System

## New proposed packages
### WTForms
WTForms is a flexible forms validation and rendering library for Python web development. It can work with whatever web framework and template engine you choose. It supports data validation, CSRF protection, internationalization (I18N), and more. We use Flask-WTF which is a simple integration of Flask and WTForms, including CSRF, file upload, and reCAPTCHA.

Documentation: https://wtforms.readthedocs.io/en/3.1.x/ and https://flask-wtf.readthedocs.io/en/1.2.x/

### BCrypt
Considerably more acceptable password hashing method. It also uses a secure algorithm to generate salts.

Documentation: https://github.com/pyca/bcrypt/

Examples are included in the initial commit.

## Getting started
### 1. Clone the repo

#### 1.1 Using GitHub Desktop
Simply click `Code` and `Open with GitHub Desktop`, and save repo to your preferred location.

#### 1.2 Using command line
Nagivate to where you would like to save the repo by using `cd your/path/`

### 2. Config `connect.py`
Create `connect.py` under `eoms` folder with your database configuration. (sql script to create database will be provided later)

### 3. (Optional) create virtual environment
1. Open your local repo folder with VS Code
2. Open Command Pellete by pressing `Ctrl+Shift+P`
3. Tpye in and select `Python: Create Environment`
4. Select `Venv` and the Python version you want to use

### 4. Install dependancies
1. After creating the environment, run Terminal: Create New Terminal or press `` Ctrl+Shift+` ``
2. Enter command `pip install -r requirements.txt`
3. All required dependancies should be installed one by one.

### 5. Create database
All database related files are under `database` folder.
* TBC: Run `eoms.sql` in MySQL workbench. 
* _You might need to remove the 1000-row limit in MySQL workbench > https://superuser.com/questions/240291/how-to-remove-1000-row-limit-in-mysql-workbench-queries_
* _Updated SQL with procedure and event to update membership status automatically. `Safe Updates` mode needs to be tunred of in MySQL workbench: Go to `Eidt` > `Peferences` > `SQL Editor` > Uncheck `Safe Updates` > Go to `Query` > `Reconnect to server`._

### 6. Create a New Branch and start coding
* In GitHub Desktop, simply click Current branch and New branch
* Commland line `git branch new-branch-name`

### 7. Test user accounts
* TBC
