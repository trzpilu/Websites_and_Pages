from flask import Flask
from flask import request, redirect
from flask import render_template

app = Flask(__name__)

@app.route('/mypage')
def render_view_mypage():
    return render_template("mypage.html")

@app.route('/mypage/me')
def render_view_mypage_me():
    return render_template("me.html")

@app.route('/mypage/contact', methods=['GET', 'POST'])
def render_request_mypage_contact():
   
   if request.method == 'GET':
       print("We received GET")
       return render_template("contact.html")
   elif request.method == 'POST':
       print("We received POST")
       print(request.form)
       return redirect("/mypage")

@app.route('/mypage/form_type')
def render_view_mypage_form():
    return render_template("form_type.html")

@app.route('/mypage/login')
def render_view_mypage_login():
    return render_template("login.html")

