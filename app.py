from flask import Flask
import psycopg2
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World from Ching-Hsiang Lin in CSPB 3308!'

@app.route("/db_test")
def db_test():
    conn = None
    try:
        conn = psycopg2.connect("postgresql://sean_postgres_db_user:3mGXzlo9Ga1fAUrMU20BBDcSH1hlKsvP@dpg-d9kdkatg1s2s73fth090-a/sean_postgres_db")
        return "Database connection successful"
    except Exception as e:
        return f"Database connection failed: {e}"
    finally:
        if conn is not None:
            conn.close()

@app.route('/db_create')
def db_create():
    conn = psycopg2.connect("postgresql://sean_postgres_db_user:3mGXzlo9Ga1fAUrMU20BBDcSH1hlKsvP@dpg-d9kdkatg1s2s73fth090-a/sean_postgres_db")
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Basketball (
        First varchar(255),
        Last varchar(255),
        City varchar(255),
        Name varchar(255),
        Number int
        );
    ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Created"

@app.route('/db_insert')
def insert():
    conn = psycopg2.connect("postgresql://sean_postgres_db_user:3mGXzlo9Ga1fAUrMU20BBDcSH1hlKsvP@dpg-d9kdkatg1s2s73fth090-a/sean_postgres_db")
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO Basketball (First, Last, City, Name, Number)
        VALUES
        ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
        ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
        ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
        ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2),
        ('Sean', 'Lin', 'CU Boulder', 'Infinity', 3308);        
    ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Populated"
    