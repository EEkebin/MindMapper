# MindMapper API

> The API for MindMapper

## Description:
MindMapper's API allows integration with self-hosted PostgreSQL Databases

# Build Instructions

## Dependencies
> Python 3.10.11: [Click Here for Download](https://www.python.org/downloads/release/python-31011/)

> PostgreSQL: [Click Here for Installation Instructions](https://www.postgresql.org/download/)

***Although not required, we recommend using DBeaver rather than PGAdmin to manage your database(s).***
> DBeaver [Click Here for Download](https://dbeaver.io/download/)

## Building and Running WebApp
1. Clone the GitHub Repo:
```bash
git clone https://github.com/EEkebin/MindMapper.git
```

2. Change into the MindMapper/api/ directory.
```bash
cd MindMapper/api/
```

3. Install pip libraries
```bash
pip install -r requirements.txt
```

4. Run the Development Flask RESTFUL API Server.
```bash
flask run
```

# Endpoints

> **GET** `/api`  
> *Get information about api*

> **POST** `/api/create_user/<username>/<password>`  
> *Create a User Account*

> **DELETE** `/api/delete_user/<username>/<password>`  
> *Delete a User ACcount*

> **GET** `/api/get_user/<username>/<password>`  
> *Get User Information*

> **GET** `/api/get_userid/<username>/<password>`  
> *Get userid from Username*

> **GET** `/api/login_user/<username>/<password>`  
> *Login to User Account*

> **GET** `/api/get_user_habits/<username>/<password>`  
> *Get User Habits*

> **POST** `/api/create_habit/<username>/<password>/<habit_name>/<metric_name>/<metric_value>/<goal_value>`  
> *Create a Habit for a User Account*

> **DELETE** `/api/delete_habit/<username>/<password>/<habit_name>`  
> *Delete a Habit from a User Account*

> **PUT** `/api/update_habit/<username>/<password>/<habit_name>/<metric_name>/<metric_value>`  
> *Update a Habit for a User Account*

> **GET** `/api/get_habit/<username>/<password>/<habit_name>`  
> *Get a Habit in a User Account*

> **GET** `/api/get_habit_history/<username>/<password>/<habit_name>`  
> *Get History of Habit as Data Points*
