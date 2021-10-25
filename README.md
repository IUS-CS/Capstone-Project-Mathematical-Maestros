# Capstone-Project-Mathematical-Maestros
## Getting Started
---

### Install Magenta
<https://github.com/magenta/magenta>

---
```
# Create Virtual Environment
$ python -m venv venv

# Activate Virtual Environment (Linux)
$ source venv/bin/activate

# Install dependencies
$ pip install -r requirements.txt

# Create DB
$ python
>> from server import db
>> db.create_all()
>> exit()

# Run Server (http://127.0.0.1:5000)
python server.py
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