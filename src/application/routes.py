from flask import render_template, redirect, url_for
from application import app, db
from application.models import Posts
from application.forms import PostForm

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')
    
@app.route('/about')
def about():
    return render_template('about.html', title='About')