from flask import render_template, session

def home():
    return render_template("user/home.html")
