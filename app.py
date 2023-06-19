import requests
from bs4 import BeautifulSoup
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
    url = 'https://www.imdb.com/list/ls057577566/'
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'lxml')
    information = soup.find_all('div', class_="lister-item mode-detail")
    images = soup.find_all('div', class_="lister-item-image ribbonize")
    image_urls = [image.find('img')['src'] for image in images]
    return render_template('top_anime.html', information=information, image_urls=image_urls)
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
