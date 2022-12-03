from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm

@app.route('/')
@app.route('/home')
def index():
    """Index URL"""
    return render_template('index.html' , title='Index Page')


@app.route('/AboutMe')
def AboutMe():
    """About Me URL"""
    return render_template('AboutMe.html', title='About Me Page')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Login"""
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'You wanna log on as {form.username.data}')
        return redirect(url_for('index'))
    return render_template('login.html', title='LoginIn Page', form=form)

