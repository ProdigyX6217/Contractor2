from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient()
db = client.Albums
albums = db.albums


app = Flask(__name__)

# OUR ARRAY OF ALBUMS
albums = [
    { 'title': 'Is This It', 'genre': 'Indie', 'artist': 'The Strokes', 'url': 'https://bit.ly/36EoFAQ'},
    { 'title': 'Channel Orange', 'genre': 'R&B', 'artist': 'Frank Ocean', 'url': 'https://bit.ly/2LZ7S3z' },
    { 'title': 'The Blueprint', 'genre': 'Hip-Hop', 'artist': 'JAY-Z', 'url': 'https://bit.ly/36Bc5lW' },
    { 'title': 'Dark Side of the Moon', 'genre': 'Rock', 'artist': 'Pink Floyd', 'url': 'https://bit.ly/2sqLR75' },
    { 'title': 'Viva la Vida or Death and All His Friends', 'genre': 'Pop', 'artist': 'Coldplay', 'url': 'https://bit.ly/38G92KZ' },

]

def image_url_creator(id_lst):
    images = []
    for img_id in id_lst:
        image = 'url' + img_id
        images.append(image)
    return images


@app.route('/')
def albums_index():
    """Show all albums."""
    return render_template('albums_index.html', albums=albums)


@app.route('/albums/new')
def albums_new():
    """Create a new album."""
    return render_template('albums_new.html', title ='New Album')


@app.route('/albums', methods=['POST'])
def albums_submit():
    """Submit a new album."""

    image_ids = request.form.get('image_ids').split()
    images = image_url_creator(image_ids)

    album = {
        'title': request.form.get('title'),
        'genre': request.form.get('genre'),
        'artist': request.form.get('artist'),
        'url': 'url',
        'image_ids': 'image_ids'
    }
    album_id = albums.insert_one(album).inserted_id
    return redirect(url_for('albums_index'))


@app.route('/albums/<album_id>')
def albums_show(album_id):
    """Show a single album."""
    album = albums.find_one({'_id': ObjectId(album_id)})
    # album_comments = comments.find({'album_id': ObjectId(album_id)})
    return render_template('albums_show.html', album=album)


@app.route('/albums/<album_id>', methods=['POST'])
def albums_update(album_id):
    """Submit an edited album."""
    image_ids = request.form.get('image_ids').split()
    albums = image_url_creator(image_ids)

    # create our updated album
    updated_album = {
        'title': request.form.get('title'),
        'genre': request.form.get('genre'),
        'artist': artist,
        'url': url,
        'image_ids': image_ids
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