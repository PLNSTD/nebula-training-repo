from flask import Flask, request, jsonify
import psycopg2
from psycopg2.extras import RealDictCursor

app = Flask(__name__)

# Database connection parameters
DATABASE = {
    'dbname': 'sqlflask',
    'user': 'postgres',
    'password': 'admin',
    'host': 'localhost',
    'port': '5432'
}

def get_db_connection():
    return psycopg2.connect(**DATABASE)

def initialize_db():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        DROP TABLE IF EXISTS users;
        CREATE TABLE users (
            id SERIAL PRIMARY KEY,
            name VARCHAR(50),
            email VARCHAR(50)
        )
    """)
    conn.commit()
    cur.close()
    conn.close()

def seed():
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("INSERT INTO users (name, email) VALUES('John', 'john@gmail.com')")
    conn.commit()
    cur.close()
    conn.close()

@app.route('/')
def index():
    return 'Welcome to the Flask API with psycopg2!'

@app.route('/users', methods=['GET'])
def get_users():
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute('SELECT * FROM users')
    users = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(users)

if __name__ == '__main__':
    initialize_db()
    seed()
    app.run(debug=True)