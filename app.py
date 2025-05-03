import os
from flask import Flask, render_template,request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user

app = Flask(__name__)

# Set the absolute path for the database file
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(BASE_DIR, 'database.db')}"
app.config['SECRET_KEY'] = '05052010'

USERNAME = "jim" 
PASSWORD = "05052025"



# Routes
@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user = request.form.get("username")
        pw = request.form.get("password")
        user = user.lower()

    
        if user == USERNAME and pw == PASSWORD:
            return redirect(url_for('shallwe'))
        else:
            flash("Incorrect username or password!")

    
    return render_template("index.html")





@app.route("/register", methods=['GET', 'POST'])
def register():
    return render_template('register.html')


@app.route("/home",methods=['GET', 'POST'])

def home():
    return render_template('home.html')


@app.route("/shallwe",methods=['GET', 'POST'])
def shallwe():
    if request.method == 'POST':
        q1 = request.form.get('q1')
        q2 = request.form.get('q2')
        q3 = request.form.get('q3').strip()
        q4 = request.form.get('q4').lower().strip()
         
        

       
        
    return render_template('shallwe.html')


@app.route("/bday",methods=['GET', 'POST'])
def bday():


    return render_template('bday.html')



# Main execution
if __name__ == "__main__":
    with app.app_context():
        app.run()

