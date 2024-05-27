import requests

class YandexDisk:
    def __init__(self, token):
        self.token = token
        self.base_url = 'https://cloud-api.yandex.net/v1/disk/resources'

    def create_folder(self, path):
        url = f"{self.base_url}?path={path}"
        headers = {
            'Authorization': f'OAuth {self.token}'
        }
        response = requests.put(url, headers=headers)
        return response.status_code == 201

    def upload_file(self, path, file_url):
        upload_url = f"{self.base_url}/upload"
        params = {
            'path': path,
            'url': file_url,
            'overwrite': 'true'
        }
        headers = {
            'Authorization': f'OAuth {self.token}'
        }
        response = requests.post(upload_url, headers=headers, params=params)
        return response.status_code == 202
    