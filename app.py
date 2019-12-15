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
    { 'title': 'Is This It', 'genre': 'Indie' },
    { 'title': 'Channel Orange', 'genre': 'R&B' },
    { 'title': 'The Blueprint', 'genre': 'Hip-Hop' },
    { 'title': 'Dark Side of the Moon', 'genre': 'Rock' }
]

@app.route('/')
def albums_index():
    """Show all albums."""
    return render_template('albums_index.html', albums=albums)

if __name__ == "__main__":
    app.run(debug=True)