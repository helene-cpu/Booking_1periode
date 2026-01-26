from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, render_template, redirect import mysql.connector
from forms import RegisterForm, LoginForm


app= Flask(__name__)
app.secret_key= "passord"

def get_conn():
    return mysql.connector.connect(
        host="localhost",
        user="booking"
        password="Strkno321!"
        database="booking_system"
    )


@app.route('/')
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)