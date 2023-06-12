from flask import Flask, render_template

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

if __name__ == '__main__':
    app.run()
