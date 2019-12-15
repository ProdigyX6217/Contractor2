from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId

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
    { 'title': 'Dark Side of the Moon', 'genre': 'Rock', 'artist': 'Pink Floyd' },
    { 'title': 'Viva la Vida or Death and All His Friends', 'genre': 'Pop', 'artist': 'Coldplay' },

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

@app.route('/albums/<album_id>')
def albums_show(album_id):
    """Show a single album."""
    album = albums.find_one({'_id': ObjectId(album_id)})
    album_comments = comments.find({'album_id': ObjectId(album_id)})
    return render_template('albums_show.html', album=album)

@app.route('/albums/<album_id>', methods=['POST'])
def albums_update(album_id):
    """Submit an edited album."""
    album_ids = request.form.get('video_ids').split()
    albums = video_url_creator(video_ids)

    # create our updated album
    updated_album = {
        'title': request.form.get('title'),
        'genre': request.form.get('genre'),
        'artist': artist,
        'url': url
    }

    # set the former album to the new one we just updated/edited
    albums.update_one(
        {'_id': ObjectId(album_id)},
        {'$set': updated_album})
    # take us back to the album's show page
    return redirect(url_for('albums_show', album_id=album_id))

@app.route('/albums/<album_id>/edit')
 def albums_edit(album_id):
     """Show the edit form for a album."""
     album = albums.find_one({'_id': ObjectId(album_id)})
     # Add the title parameter here
     return render_template('albums_edit.html', album=album, title='Edit Album')





if __name__ == "__main__":
    app.run(debug=True)