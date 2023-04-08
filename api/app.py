from flask import Flask
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect(
    host="74.207.249.96",
    database="mindmapperdb",
    user="postgres",
    password="Mindmapperpassword1!",
    port=5432
)

@app.route('/')
def hello_world():
    return 'Welcome to MindMapper!'

if __name__ == '__main__':
    app.run()
