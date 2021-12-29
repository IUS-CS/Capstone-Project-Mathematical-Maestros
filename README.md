# Capstone-Project-Mathematical-Maestros
## Getting Started
---

### Install Magenta
<https://github.com/magenta/magenta>

---
```
# Navigate to flask-server
$ cd flask-server

# Create Virtual Environment
$ python -m venv venv

# Activate Virtual Environment (Linux)
$ source venv/bin/activate

# Install dependencies
$ pip install -r requirements.txt

# Create DB
$ python
>> from models import db
>> db.create_all()
>> exit()

# Run Server (http://127.0.0.1:5000)
python app.py

# Navigate to react-front-end
$ cd ../react-front-end/

# Run Frontend (http://127.0.0.1:3000)
$ npm start
```

## Endpoints
--- 

* GET       /song
* GET       /song/:id
* POST      /song
* PUT       /song/:id
* DELETE    /song/:id

* GET, POST /sign_in
* GET, POST /register