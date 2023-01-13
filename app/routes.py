from app import app
from flask import render_template

@app.route('/')
@app.route('/home')
def homePage():
    return render_template('home.html')

@app.route('/post')
def postPage():
    return ("Hello World!")
#replace postPage with actual post page