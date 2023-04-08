from flask import make_response
from flask import Flask, make_response, redirect, jsonify
from flask_cors import CORS
import psycopg2
import os
import bcrypt
import uuid
import base64

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
    return 'Welcome to MindMapper API!'


@app.route('/api/create_user/<username>/<password>', methods=['POST'])
def create_user(username, password):
    cur = conn.cursor()
    try:
        passwordhash = encrypt_password(password)
        cur.execute("INSERT INTO user_credentials (username, password) VALUES (%s, %s)",
                    (username, passwordhash))
        conn.commit()
        return jsonify({"success": True}), 200
    except Exception as e:
        # Handle the exception here
        conn.rollback()
        return jsonify({"error": str(e)}), 500
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
            return jsonify({"success": True}), 200
        else:
            return jsonify({"error": "Incorrect password!"}), 401

    except Exception as e:
        # Handle the exception here
        conn.rollback()
        return jsonify({"error": str(e)}), 500
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
            return jsonify({"error": "User not found!"}), 401
        if verify_password(password, user[2]):
            return jsonify({"user": user}), 200
        else:
            return jsonify({"error": "Incorrect password!"}), 401
    except Exception as e:
        # Handle the exception here
        return jsonify({"error": str(e)})
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
            return jsonify({"error": "User not found!"}), 404
        if verify_password(password, user[2]):
            return jsonify({"user_id": user[0]})
        else:
            return jsonify({"error": "Incorrect password!"}), 401
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cur.close()


# Login user and set cookie in user_credentials table
@app.route('/api/login_user/<username>/<password>', methods=['POST'])
def login_user(username, password):
    cur = conn.cursor()
    try:
        cur.execute(
            "SELECT * FROM user_credentials WHERE username = %s", (username,))
        user = cur.fetchone()
        if user is None:
            return jsonify({"message": "User not found!"}), 401
        if verify_password(password, user[2]):
            uuid_value = uuid.uuid4()
            cookie = base64.b64encode(uuid_value.bytes).decode('utf-8')
            response = make_response('User logged in!')
            response.set_cookie('cookie', cookie)
            cur.execute("UPDATE user_credentials SET cookie = %s WHERE username = %s",
                        (cookie, username))
            conn.commit()
            return jsonify({"success": True})
        else:
            return jsonify({"success": False}), 401
    except Exception as e:
        # Handle the exception here
        return jsonify({"message": "Error: " + str(e)})
    finally:
        cur.close()


# Login with Cookie
@app.route('/api/login_user_cookie/<username>/<cookie>', methods=['POST'])
def login_user_cookie(username, cookie):
    cur = conn.cursor()
    try:
        cur.execute(
            "SELECT * FROM user_credentials WHERE username = %s", (username,))
        user = cur.fetchone()
        if user is None:
            return jsonify({"message": "User not found!"}), 401
        if cookie == user[3]:
            response = make_response('User logged in!')
            response.set_cookie('cookie', cookie)
            return jsonify({"success": True}), 200
        else:
            return jsonify({"success": False}), 401
    except Exception as e:
        # Handle the exception here
        return jsonify({"message": "Error: " + str(e)}), 500
    finally:
        cur.close()


# Logout user and delete cookie in user_credentials table
@app.route('/api/logout_user/<username>/<password>', methods=['POST'])
def logout_user(username, password):
    cur = conn.cursor()
    try:
        cur.execute(
            "SELECT * FROM user_credentials WHERE username = %s", (username,))
        user = cur.fetchone()
        if user is None:
            return jsonify({"message": "User not found!"})
        if verify_password(password, user[2]):
            response = make_response('User logged out!')
            response.set_cookie('cookie', '', expires=0)
            cur.execute("UPDATE user_credentials SET cookie = %s WHERE username = %s",
                        (None, username))
            conn.commit()
            return jsonify({"message": "User logged out!"})
        else:
            return jsonify({"message": "Incorrect password!"})
    except Exception as e:
        # Handle the exception here
        return jsonify({"message": "Error: " + str(e)})
    finally:
        cur.close()


@app.route('/api/get_user_habits/<username>/<password>', methods=['GET'])
def get_user_habits(username, password):
    cur = conn.cursor()
    try:
        user_id = get_userid(username, password)
        if user_id == 'Incorrect password!':
            return jsonify({"message": "Incorrect password!"})
        cur.execute("SELECT * FROM habits WHERE user_id = %s", (user_id,))
        habits = cur.fetchall()
        return jsonify(habits)
    except Exception as e:
        # Handle the exception here
        return jsonify({"message": "Error: " + str(e)})
    finally:
        cur.close()


@app.route('/api/create_habit/<username>/<password>/<habit_name>/<metric_name>/<metric_value>/<goal_value>', methods=['POST'])
def create_habit(username, password, habit_name, metric_name, metric_value, goal_value):
    cur = conn.cursor()
    try:
        user_id = get_userid(username, password)
        if user_id == 'Incorrect password!':
            return jsonify({"message": "Incorrect password!"}), 401
        cur.execute("INSERT INTO habits (user_id, habit_name, metric_name, metric_value, goal_value) VALUES (%s, %s, %s, %s, %s)",
                    (user_id, habit_name, metric_name, metric_value, goal_value))
        conn.commit()
        return jsonify({"message": "Habit created!"}), 200
    except Exception as e:
        # Handle the exception here
        return jsonify({"message": "Error: " + str(e)}), 500
    finally:
        cur.close()



@app.route('/api/delete_habit/<username>/<password>/<habit_name>', methods=['DELETE'])
def delete_habit(username, password, habit_name):
    try:
        cur = conn.cursor()
        user_id = get_userid(username, password)
        if user_id == 'Incorrect password!':
            return jsonify({"message": "Incorrect password!"})
        cur.execute(
            "DELETE FROM habits WHERE user_id = %s AND habit_name = %s", (user_id, habit_name))
        conn.commit()
        return jsonify({"message": "Habit deleted!"}), 200
    except Exception as e:
        return jsonify({"message": "Error: " + str(e)}), 500


@app.route('/api/update_habit/<username>/<password>/<habit_name>/<metric_name>/<metric_value>', methods=['PUT'])
def update_habit(username, password, habit_name, metric_name, metric_value):
    try:
        cur = conn.cursor()
        user_id = get_userid(username, password)
        if user_id == 'Incorrect password!':
            return jsonify({"message": "Incorrect password!"})
        cur.execute("UPDATE habits SET metric_name = %s, metric_value = %s WHERE user_id = %s AND habit_name = %s",
                    (metric_name, metric_value, user_id, habit_name))
        conn.commit()
        return jsonify({"message": "Habit updated!"}), 200
    except Exception as e:
        return jsonify({"message": "Error: " + str(e)}), 500


@app.route('/api/get_habit/<username>/<password>/<habit_name>', methods=['GET'])
def get_habit(username, password, habit_name):
    cur = conn.cursor()
    user_id = get_userid(username, password)
    if user_id == 'Incorrect password!':
        return jsonify({"message": "Incorrect password!"}), 401
    cur.execute(
        "SELECT * FROM habits WHERE user_id = %s AND habit_name = %s", (user_id, habit_name))
    habit = cur.fetchone()
    if habit:
        return jsonify({"habit": habit}), 200
    else:
        return jsonify({"message": "Habit not found!"}), 500


@app.route('/api/get_habit_history/<username>/<password>/<habit_name>', methods=['GET'])
def get_habit_history(username, password, habit_name):
    try:
        cur = conn.cursor()
        user_id = get_userid(username, password)
        if user_id == 'Incorrect password!':
            return jsonify({"message": "Incorrect password!"}), 401
        cur.execute(
            "SELECT * FROM habits WHERE user_id = %s AND habit_name = %s", (user_id, habit_name))
        habit = cur.fetchone()
        habit_id = habit[0]
        cur.execute(
            "SELECT * FROM habits_history WHERE habit_id = %s", (habit_id,))
        habit_history = cur.fetchall()
        return jsonify({"habit_history": habit_history}), 200
    except Exception as e:
        return jsonify({"message": "Error: " + str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
