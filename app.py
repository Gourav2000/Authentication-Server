from sqlite3.dbapi2 import Cursor
from flask import Flask, request, render_template , session
from flask import *
import sqlite3
import random
import string
import hashlib

from flask.helpers import url_for

app = Flask(__name__,template_folder="templates",static_folder="templates/static")
app.secret_key = '#d\xe9X\x00\xbe~Uq\xebX\xae\x81\x1fs\t\xb4\x99\xa3\x87\xe6.\xd1_'

def IsUserPresent(email):
    db=sqlite3.connect("userdb.db")
    crsr = db.cursor()
    crsr.execute("SELECT email FROM users")
    email_li=crsr.fetchall()
    db.close()
    email_list=[]
    for i in email_li:
        email_list.append(i[0])
    if email in email_list:
        return True
    else:
        return False

def logoutUser(uid):
    db=sqlite3.connect('userdb.db')
    crsr=db.cursor()
    crsr.execute("UPDATE users SET token = ? where uid=?",(None,uid))
    db.commit()
    db.close()
    

def loginUser(email,password):
    p=password.encode()
    IsUserNew=True
    password=hashlib.sha256(p).hexdigest()
    db=sqlite3.connect("userdb.db")
    crsr = db.cursor()
    crsr.execute("SELECT * FROM users")
    allData=crsr.fetchall()
    for i in allData:
        if email in i:
            IsUserNew=False
            if password==i[3]:
                print('done')
                token = ''.join(random.choices(string.ascii_uppercase +string.ascii_lowercase +string.digits, k = 30))
                crsr.execute("UPDATE users SET token = ? where uid=?",(token,i[0]))
                db.commit()
                db.close()
                
                return {'uid':i[0],'name':i[1],'email':i[2],'token':token}
            else:
                db.close()
                raise Exception('incorrect password')
        if IsUserNew==True:
            raise Exception('User not present')


def CreateNewUser(name,email,password):
    db=sqlite3.connect("userdb.db")
    crsr = db.cursor()
    uid = ''.join(random.choices(string.ascii_uppercase +string.ascii_lowercase +string.digits, k = 50))
    p=password.encode()
    password=hashlib.sha256(p).hexdigest()
    sql_command ="""INSERT INTO users VALUES (?,?,?,?,?);"""
    crsr.execute(sql_command,(uid,name,email,password,None))
    db.commit()
    db.close()
    return {'uid':uid,'name':name,'email':email}
@app.route('/', methods=['GET', 'POST'])
def main():
    if 'user' in session:
        return render_template("login.html")
    else:
        return redirect(url_for("profile"))
@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'user' not in session:
        return render_template("login.html")
    else:
        return redirect(url_for("profile"))


@app.route('/signup', methods=['GET', 'POST'])
def sign_up():
    if 'user' not in session:
        return render_template("signup.html")
    else:
        return redirect("profile")

@app.route('/profile_signup', methods=['GET', 'POST'])
def profile_signup():
    if request.method == 'POST':
        req_data=request.form
        print(req_data)
        if IsUserPresent(req_data['email']):
            return 'user already present go to <a href="/login">login page</a>'
        else:
            CreateNewUser(req_data['name'],req_data['email'],req_data['password'])
            
            session['user']=loginUser(req_data['email'],req_data['password'])
            session['login']=True
            return session['user']
    else:
        return redirect(url_for('profile'))

@app.route('/profile_login', methods=['GET', 'POST'])
def profile_login():
    if request.method == 'POST':
        req_data=request.form
        print(req_data)
        if not IsUserPresent(req_data['email']):
            return 'no user registered under this email go to <a href="/signup">signup page</a>'
        else:
            session['user']=loginUser(req_data['email'],req_data['password'])
            session['login']=True
            return session['user']
    else:
        return redirect(url_for('profile'))
@app.route('/profile',methods=['GET'])
def profile():
    if 'user' not in session:
        return redirect(url_for('login'))
    return session['user']

@app.route('/logout',methods=['GET'])
def logout():
    if 'user' not in session:
        return redirect(url_for('login'))
    logoutUser(session['user']['uid'])
    session['login']=False
    del session['user']
    return redirect(url_for('login'))

if __name__ == '__main__':
    # run app in debug mode on port 5000
    db=sqlite3.connect("userdb.db")
    crsr = db.cursor() 
    sql_command = """CREATE TABLE IF NOT EXISTS users (  
    uid varchar(10),  
    name VARCHAR(50),    
    email VARCHAR(30),  
    password VARCHAR(1000),
    token VARCHAR(50));"""
    crsr.execute(sql_command)
    db.commit()
    db.close()
    app.run(debug=True, port=5000)