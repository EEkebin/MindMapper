from flask import Flask, jsonify, make_response
from flask_cors import CORS
import psycopg2
import os
import bcrypt

app = Flask(__name__)
CORS(app)

conn = psycopg2.connect(
    host="74.207.249.96",
    database="mindmapperdb",
    user="postgres",
    password="Mindmapperpassword1!",
    port=5432
)


def encrypt_password(password: str) -> str:
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8')


def verify_password(password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))


@app.route('/api')
def hello_world():
    return 'Welcome to MindMapper API!\nVersion 1.0\nThis is supposed to be uninteractive. Please use the Web Application.'


@app.route('/api/create_user/<username>/<password>', methods=['POST'])
def create_user(username, password):
    cur = conn.cursor()
    try:
        passwordhash = encrypt_password(password)
        cur.execute("INSERT INTO user_credentials (username, password) VALUES (%s, %s)",
                    (username, passwordhash))
        conn.commit()
        return 'User created!'
    except Exception as e:
        # Handle the exception here
        conn.rollback()
        return 'Error: ' + str(e)
    finally:
        cur.close()


# Delete user
@app.route('/api/delete_user/<username>/<password>', methods=['DELETE'])
def delete_user(username, password):
    cur = conn.cursor()
    try:
        cur.execute(
            "SELECT * FROM user_credentials WHERE username = %s", (username,))
        user = cur.fetchone()
        if verify_password(password, user[2]):
            cur.execute(
                "DELETE FROM user_credentials WHERE username = %s", (username,))
            conn.commit()
            return 'User deleted!'
        else:
            return 'Incorrect password!'
    except Exception as e:
        # Handle the exception here
        conn.rollback()
        return 'Error: ' + str(e)
    finally:
        cur.close()


# Get user
@app.route('/api/get_user/<username>/<password>', methods=['GET'])
def get_user(username, password):
    cur = conn.cursor()
    try:
        cur.execute(
            "SELECT * FROM user_credentials WHERE username = %s", (username,))
        user = cur.fetchone()
        if user is None:
            return 'User not found!'
        if verify_password(password, user[2]):
            return str(user)
        else:
            return 'Incorrect password!'
    except Exception as e:
        # Handle the exception here
        return 'Error: ' + str(e)
    finally:
        cur.close()


@app.route('/api/get_userid/<username>/<password>', methods=['GET'])
def get_userid(username, password):
    cur = conn.cursor()
    try:
        cur.execute(
            "SELECT * FROM user_credentials WHERE username = %s", (username,))
        user = cur.fetchone()
        if user is None:
            return 'User not found!'
        if verify_password(password, user[2]):
            return str(user[0])
        else:
            return 'Incorrect password!'
    except Exception as e:
        # Handle the exception here
        return 'Error: ' + str(e)
    finally:
        cur.close()


# Login user
@app.route('/api/login_user/<username>/<password>', methods=['GET'])
def login_user(username, password):
    cur = conn.cursor()
    try:
        cur.execute(
            "SELECT * FROM user_credentials WHERE username = %s", (username,))
        user = cur.fetchone()
        if user is None:
            return 'User not found!', 401
        if verify_password(password, user[2]):
            return 'Login successful!', 200
        else:
            return 'Incorrect password!', 401
    except Exception as e:
        # Handle the exception here
        return 'Error: ' + str(e), 500
    finally:
        cur.close()


@app.route('/api/get_user_habits/<username>/<password>', methods=['GET'])
def get_user_habits(username, password):
    cur = conn.cursor()
    try:
        user_id = get_userid(username, password)
        if user_id == 'Incorrect password!':
            return 'Incorrect password!', 401
        cur.execute("SELECT * FROM habits WHERE user_id = %s", (user_id,))
        habits = cur.fetchall()
        return jsonify(habits), 200
    except Exception as e:
        # Handle the exception here
        return 'Error: ' + str(e), 500
    finally:
        cur.close()


@app.route('/api/create_habit/<username>/<password>/<habit_name>/<metric_name>/<metric_value>/<goal_value>', methods=['POST'])
def create_habit(username, password, habit_name, metric_name, metric_value, goal_value):
    cur = conn.cursor()
    try:
        user_id = get_userid(username, password)
        if user_id == 'Incorrect password!':
            return 'Incorrect password!'
        cur.execute("INSERT INTO habits (user_id, habit_name, metric_name, metric_value, goal_value) VALUES (%s, %s, %s, %s, %s)",
                    (user_id, habit_name, metric_name, metric_value, goal_value))
        conn.commit()
        return 'Habit created!'
    except Exception as e:
        # Handle the exception here
        return 'Error: ' + str(e)
    finally:
        cur.close()


@app.route('/api/delete_habit/<username>/<password>/<habit_name>', methods=['DELETE'])
def delete_habit(username, password, habit_name):
    try:
        cur = conn.cursor()
        user_id = get_userid(username, password)
        if user_id == 'Incorrect password!':
            return 'Incorrect password!'
        cur.execute(
            "DELETE FROM habits WHERE user_id = %s AND habit_name = %s", (user_id, habit_name))
        conn.commit()
        return 'Habit deleted!'
    except Exception as e:
        return str(e)


@app.route('/api/update_habit/<username>/<password>/<habit_name>/<metric_name>/<metric_value>', methods=['PUT'])
def update_habit(username, password, habit_name, metric_name, metric_value):
    try:
        cur = conn.cursor()
        user_id = get_userid(username, password)
        if user_id == 'Incorrect password!':
            return 'Incorrect password!'
        cur.execute("UPDATE habits SET metric_name = %s, metric_value = %s WHERE user_id = %s AND habit_name = %s",
                    (metric_name, metric_value, user_id, habit_name))
        conn.commit()
        return 'Habit updated!'
    except Exception as e:
        return str(e)


# Get habit
@app.route('/api/get_habit/<username>/<password>/<habit_name>', methods=['GET'])
def get_habit(username, password, habit_name):
    cur = conn.cursor()
    user_id = get_userid(username, password)
    if user_id == 'Incorrect password!':
        return 'Incorrect password!'
    cur.execute(
        "SELECT * FROM habits WHERE user_id = %s AND habit_name = %s", (user_id, habit_name))
    habit = cur.fetchone()
    if habit:
        return str(habit)
    else:
        return 'Habit not found!'


# Get habit history
@app.route('/api/get_habit_history/<username>/<password>/<habit_name>', methods=['GET'])
def get_habit_history(username, password, habit_name):
    try:
        cur = conn.cursor()
        user_id = get_userid(username, password)
        if user_id == 'Incorrect password!':
            return 'Incorrect password!'
        cur.execute(
            "SELECT * FROM habits WHERE user_id = %s AND habit_name = %s", (user_id, habit_name))
        habit = cur.fetchone()
        habit_id = habit[0]
        cur.execute(
            "SELECT * FROM habits_history WHERE habit_id = %s", (habit_id,))
        habit_history = cur.fetchall()
        return str(habit_history)
    except Exception as e:
        return "Error: " + str(e)


if __name__ == '__main__':
    app.run()
