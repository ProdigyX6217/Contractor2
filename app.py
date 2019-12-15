from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

client = MongoClient()
db = client.Albums
albums = db.albums


app = Flask(__name__)

# @app.route('/')
# def index():
#     """Return homepage."""
#     return render_template('index.html')

# OUR ARRAY OF ALBUMS
albums = [
    { 'title': 'Is This It', 'genre': 'Indie', 'artist': 'The Strokes'},
    { 'title': 'Channel Orange', 'genre': 'R&B', 'artist': 'Frank Ocean' },
    { 'title': 'The Blueprint', 'genre': 'Hip-Hop', 'artist': 'JAY-Z' },
    { 'title': 'Dark Side of the Moon', 'genre': 'Rock', 'artist': 'Pink Floyd' }
]

@app.route('/')
def albums_index():
    """Show all albums."""
    return render_template('albums_index.html', albums=albums)

@app.route('/albums/new')
def albums_new():
    """Create a new album."""
    return render_template('albums_new.html')

@app.route('/albums', methods=['POST'])
def albums_submit():
    """Submit a new album."""
    album = {
        'title': request.form.get('title'),
        'genre': request.form.get('genre'),
        'artist': request.form.get('artist'),
        'url': request.form.get('url')
    }
    albums.insert_one(album)
    return redirect(url_for('albums_index'))




if __name__ == "__main__":
    app.run(debug=True)