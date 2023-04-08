from flask import Flask
import psycopg2
import os
import bcrypt

app = Flask(__name__)

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


@app.route('/')
def hello_world():
    return 'Welcome to MindMapper!'


@app.route('/create_user/<username>/<password>', methods=['POST'])
def create_user(username, password):
    cur = conn.cursor()
    passwordhash = encrypt_password(password)
    cur.execute("INSERT INTO user_credentials (username, password) VALUES (%s, %s)",
                (username, passwordhash))
    conn.commit()
    return 'User created!'


# Delete user
@app.route('/delete_user/<username>/<password>', methods=['DELETE'])
def delete_user(username, password):
    cur = conn.cursor()
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


# Get user
@app.route('/get_user/<username>/<password>', methods=['GET'])
def get_user(username, password):
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM user_credentials WHERE username = %s", (username,))
    user = cur.fetchone()
    
    if verify_password(password, user[2]):
        return str(user)
    else:
        return 'Incorrect password!'


@app.route('/get_userid/<username>/<password>', methods=['GET'])
def get_userid(username, password):
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM user_credentials WHERE username = %s", (username,))
    user = cur.fetchone()
    if verify_password(password, user[2]):
        return str(user[0])
    else:
        return 'Incorrect password!'


@app.route('/get_user_habits/<username>/<password>', methods=['GET'])
def get_user_habits(username, password):
    cur = conn.cursor()
    user_id = get_userid(username, password)
    if user_id == 'Incorrect password!':
        return 'Incorrect password!'
    cur.execute("SELECT * FROM habits WHERE user_id = %s", (user_id,))
    habits = cur.fetchall()
    return str(habits)


@app.route('/create_habit/<username>/<password>/<habit_name>/<metric_name>/<metric_value>', methods=['POST'])
def create_habit(username, password, habit_name, metric_name, metric_value):
    cur = conn.cursor()
    user_id = get_userid(username, password)
    if user_id == 'Incorrect password!':
        return 'Incorrect password!'
    cur.execute("INSERT INTO habits (user_id, habit_name, metric_name, metric_value) VALUES (%s, %s, %s, %s)",
                (user_id, habit_name, metric_name, metric_value))
    conn.commit()
    return 'Habit created!'


@app.route('/delete_habit/<username>/<password>/<habit_name>', methods=['DELETE'])
def delete_habit(username, password, habit_name):
    cur = conn.cursor()
    user_id = get_userid(username, password)
    if user_id == 'Incorrect password!':
        return 'Incorrect password!'
    cur.execute(
        "DELETE FROM habits WHERE user_id = %s AND habit_name = %s", (user_id, habit_name))
    conn.commit()
    return 'Habit deleted!'


@app.route('/update_habit/<username>/<password>/<habit_name>/<metric_name>/<metric_value>', methods=['PUT'])
def update_habit(username, password, habit_name, metric_name, metric_value):
    cur = conn.cursor()
    user_id = get_userid(username, password)
    if user_id == 'Incorrect password!':
        return 'Incorrect password!'
    cur.execute("UPDATE habits SET metric_name = %s, metric_value = %s WHERE user_id = %s AND habit_name = %s",
                (metric_name, metric_value, user_id, habit_name))
    conn.commit()
    return 'Habit updated!'


if __name__ == '__main__':
    app.run()
