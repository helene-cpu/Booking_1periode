from flask import Flask, render_template, redirect, session
from werkzeug.security import generate_password_hash, check_password_hash
import mysql.connector
from forms import RegisterForm, LoginForm


app= Flask(__name__)
app.secret_key= "passord"

def get_conn():
    return mysql.connector.connect(
        host="localhost",
        user="booking",
        password="Strkno321!",
        database="booking_system"
    )


@app.route('/', methods=["GET", "POST"])
def index():
     form = LoginForm()

     if form.validate_on_submit():
        brukernavn = form.username.data
        passord = form.password.data

        conn = get_conn()
        cur = conn.cursor()
        cur.execute(
            "SELECT navn, passord, brukernavn FROM brukere WHERE brukernavn=%s", 
            (brukernavn,)
        )
        user = cur.fetchone()
        cur.close()
        conn.close()

        if user:
            passord_db= user[1]

            if check_password_hash(passord_db, passord):
                session['Navn'] = user[0]
                return render_template("start.html", form=form)
        else:
            form.username.errors.append("Feil brukernavn eller passord")
     return render_template("start.html", form=form)

if __name__ == "__main__":
    app.run(debug=True)