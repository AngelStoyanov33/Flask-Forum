# AskTUES
A Flask powered forum for a school homework project ([Task](http://tp-elsys.com/tasks/4 "Task"))

# Features
  - A JWT based Authentication
  - Profile page
  - Profile pictures
  - Roles
  - Search Engine
  - Simple and beautiful UI
  - Emoji support
  - Topic management
  - Thread management
  - Reply management

# Installation

Create the virtual enviroment and activate it.
```py
$ virtualenv env
$ source env/bin/activate
```
Install the dependencies.
```py
$ pip install -r requirements.txt
```
### Start the server.
On Linux
```py
$ export FLASK_APP=run.py
$ export FLASK_ENV=development
$ flask run
```
On Windows
```py
$ py ./run.py
```

### Locate the forum @
```sh
localhost:5000
```

License
----

MIT
