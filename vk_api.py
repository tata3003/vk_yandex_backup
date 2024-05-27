import requests

class VK:
    def __init__(self, access_token, user_id):
        self.token = access_token
        self.user_id = user_id

    def get_photos(self, album_id='profile', count=5):
        url = 'https://api.vk.com/method/photos.get'
        params = {
            'owner_id': self.user_id,
            'album_id': album_id,
            'access_token': self.token,
            'v': '5.131',
            'extended': 1,
            'photo_sizes': 1,
            'count': count
        }
        response = requests.get(url, params=params)
        return response.json()

        