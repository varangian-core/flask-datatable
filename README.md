### Project Description

Simple implementation of a flask data table along with the bootstrap and jquery. Application is designed to provide a dynamic table with connectivity to other APIs. In this particular case, we are accessing a static file server to display the links.

**Notice: both the information pertaining to the database and the API static file server have been removed. You will need to adjust those parameters accordingly. While this project does utilize MySQL, due to the licensing requirements the user is encouraged to use MariaDB for production purposes.**

### Installation

Fork or download this repository.

1. You will need to build python virtual environment
  ```bash
  sudo apt install python3-pip python3-virtualenv
  ```
2. Then construct the virtual environment within the app folder and source the requirements
  ```bash
  python3 -m virtualenv venv
  python3 -r requirements.txt
  ```


3. Install the sql database, create the data tables, and assign correct user privileges
4. Adjust app.py and the templates to reflect the desired results

### Deployment
Bind flask app to your source file.
```bash
export FLASK_APP=app.py
flask.run
```
Check locaholhost:5000 for core functionality of the app. 

You can install gunicorn or nginx as your proxies to serve the app

### Support

You can reach out to me by dropping a comment in http://posts.varangianroute.com 

### License
MIT License
