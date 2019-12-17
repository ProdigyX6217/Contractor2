# tests.py

from unittest import TestCase, main as unittest_main
from app import app, video_url_creator
from bson.objectid import ObjectId


sample_album_id = ObjectId('5d55cffc4a3d4031f42827a3')
sample_album = {
    'title': 'Cat Videos',
    'genre': 'Cats acting weird',
    'artist': 'Cats',
    'rating': '5',
    'url': 'url',
    'videos': [
        'https://youtube.com/embed/hY7m5jjJ9mM',
        'https://youtube.com/embed/CQ85sUNBK7w'
    ],
    'video_ids': ['hY7m5jjJ9mM','CQ85sUNBK7w']
}
sample_form_data = {
    'title': sample_album['title'],
    'genre': sample_album['genre'],
    'artist': 'artist',
    'rating': 'rating',
    'url': 'url'
    'videos': '\n'.join(sample_album['video_ids'])
}


class AlbumsTests(TestCase):
    """Flask tests."""

    def setUp(self):
        """Stuff to do before every test."""

        # Get the Flask test client
        self.client = app.test_client()

        # Show Flask errors that happen during tests
        app.config['TESTING'] = True

    def test_index(self):
        """Test the albums homepage."""
        result = self.client.get('/')
        self.assertEqual(result.status, '200 OK')

    def test_new(self):
        """Test the new album creation page."""
        result = self.client.get('/albums/new')
        self.assertEqual(result.status, '200 OK')

    def test_video_url_creator(self):
    """Test the video_url_creator function"""
    expected_list = ['https://youtube.com/embed/hY7m5jjJ9mM', 'https://youtube.com/embed/CQ85sUNBK7w']
    output_list = video_url_creator(sample_id_list)
    self.assertEqual(expected_list, output_list)

    @mock.patch('pymongo.collection.Collection.find_one')
    def test_show_album(self, mock_find):
        """Test showing a single album."""
        mock_find.return_value = sample_album

        result = self.client.get(f'/albums/{sample_album_id}')
        self.assertEqual(result.status, '200 OK')
    
    @mock.patch('pymongo.collection.Collection.update_one')
    def test_update_album(self, mock_update):
        result = self.client.post(f'/albums/{sample_album_id}', data=sample_form_data)

        self.assertEqual(result.status, '302 FOUND')
        mock_update.assert_called_with({'_id': sample_album_id}, {'$set': sample_album

    @mock.patch('pymongo.collection.Collection.delete_one')
    def test_delete_album(self, mock_delete):
        form_data = {'_method': 'DELETE'}
        result = self.client.post(f'/albums/{sample_album_id}/delete', data=form_data)
        self.assertEqual(result.status, '302 FOUND')
        mock_delete.assert_called_with({'_id': sample_album


if __name__ == '__main__':
    unittest_main()