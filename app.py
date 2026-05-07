from flask import Flask, render_template, request, redirect, url_for, session, flash, abort, Response
from werkzeug.security import generate_password_hash, check_password_hash
import mysql.connector
import os
import base64
from dotenv import load_dotenv
from waitress import serve

load_dotenv()

user = os.getenv("user")
pword = os.getenv("p_word")
app = Flask(__name__)
app.secret_key = os.getenv("skey")

# Database-tilkobling
# bruker du Mariadb så bytter du ut mysql med mariadb. connect
# return mariadb.connect(
# Husk å endre host, user, password og database, slik at de er tilpasset dine instillinger 
def get_db_connection():
    return mysql.connector.connect(
        host="127.0.0.1",
        user=user,
        password=pword,
        database="uploader"
    )
@app.route("/")
def blank():
    return redirect(url_for('login'))

@app.route("/login", methods=["POST","GET"])
def login():
    if  session.get('id'):
      return redirect(url_for('home'))
    if request.method == "POST":
        brukernavn = request.form['brukernavn']
        passord = request.form['passord']

        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT id,name,email,password,role FROM users WHERE name=%s", (brukernavn,))
        bruker = cursor.fetchone()
        cursor.close()
        conn.close()
        if not bruker:
            return render_template("login.html", feil_melding="wrong username or password")
        if bruker and check_password_hash(bruker['password'], passord):
            session['name'] = bruker['name']
            session['id'] = bruker['id']
            session['role'] = bruker['role']
            session['email'] = bruker['email']

            return redirect(url_for("home"))
        else:
            return render_template("login.html", feil_melding="wrong username or password")

    return render_template("login.html")

@app.route("/new_user", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        brukernavn = request.form['brukernavn']
        epost = request.form['epost']
        passord = generate_password_hash(request.form['passord'])

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (name, email, password) VALUES (%s, %s, %s)", 
                       (brukernavn, epost, passord))
        conn.commit()
        cursor.close()
        conn.close()
        flash("user registrert!", "success")
        return redirect(url_for("login"))

    return render_template("registrer.html")

@app.route("/logout")
def logout():
    session.clear()
    flash("you have logged out", "info")
    return redirect(url_for("login"))

@app.route("/home")
def home():
    if  not session.get('id'):
      return redirect(url_for('login'))
    
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT id,name, mimetype FROM files WHERE poster_id = %s",(session['id'],))
    files = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('home.html',files= files)

@app.route("/upload",methods = ["GET","POST"])
def upload():
    if  not session.get('id'):
      return redirect(url_for('login'))
    if request.method == "POST":
        file = request.files.get('file')
        if not file or file.filename == "":
             return 'no file uploaded', 400
        file_data = base64.b64encode(file.read()).decode('utf-8')
        file_type =file.mimetype
        filename = file.filename
        # print("file: ",file,"data: ",file_data,"type: ",file_type,"name: ",filename)
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("INSERT INTO files(name,data,mimetype,poster_id) VALUES(%s,%s,%s,%s)",(filename,file_data,file_type,session['id']))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('home'))
    else:
        return render_template('upload.html')
if __name__ == "__main__":

    app.run(debug=True,host='0.0.0.0', port=5000)
    #running normaly^

    #serve(app, host='0.0.0.0', port=5000)
    #run with waitress