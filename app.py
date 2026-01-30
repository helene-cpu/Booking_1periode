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
            "SELECT passord, brukernavn FROM brukere WHERE brukernavn=%s", 
            (brukernavn,)
        )
        user = cur.fetchone()
        cur.close()
        conn.close()

        if user:
            passord_db, brukernavn_db= user

            if check_password_hash(passord_db, passord):
                session['user'] = brukernavn_db
                return redirect("/start")
            else:
                form.username.errors.append("Feil brukernavn eller passord")
     return render_template("index.html", form=form)

@app.route('/start', methods=["GET", "POST"])
def start():
    if "user" not in session:
        return redirect("/")
    return render_template("start.html")

@app.route('/register', methods=["GET", "POST"])
def register():
    form= RegisterForm()

    if form.validate_on_submit():
        navn = form.name.data
        brukernavn = form.username.data
        klasse = form.classname.data
        passord_hash = generate_password_hash(form.password.data)

        conn = get_conn()
        cur = conn.cursor()

        cur.execute(
            "INSERT INTO brukere (navn, brukernavn, klasse, passord) VALUES (%s, %s, %s, %s)", 
            (navn, brukernavn, klasse, passord_hash)
        )
        conn.commit()

    return render_template("register.html", form=form)

if __name__ == "__main__":
    app.run(debug=True)