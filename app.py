from flask import Flask, Blueprint, render_template, request, jsonify, redirect, flash, session
from flask_bcrypt import Bcrypt, check_password_hash
from db import db_init, db
from models import Users
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/topAnime')
def top_anime():
    return render_template('top_anime.html')

@app.route('/topMovies')
def top_movies():
    return render_template('top_movies.html')

@app.route('/sing-up')
def Sing_up():
    if request.method == 'POST':
        name = request.form['name']
        last_name = request.form['last name']
        email_address = request.form['email address']
        password = request.form['password']

        bcrypt = Bcrypt()
        hashed_hui = bcrypt.generate_password_hash(password)

        # save
        save = Users(name = name, last_name=last_name, email = email_address, password = hashed_hui)
        db.session.add(save)
        db.session.commit()

        return redirect('sing-in')
    return render_template('sing-up.html')


    
@app.route('/sing-in')
def Sing_in():
    if request.method == 'POST':
        email_address = request.form['email address']
        password = request.form['password'].encode('utf-8')
        profile = db.session.query(Users).filter_by(email= email_address).first()
        if not profile:
            flash('account not found')
            return redirect('/sing-in')
        if check_password_hash(profile.password, password):
            session['id'] = profile.id
            return redirect('/my_profile')
        else:
            flash('no correct password')
            return redirect('/sing-in')


    return render_template('sing-in.html')


if __name__ == '__main__':
    app.run(debug=True)
