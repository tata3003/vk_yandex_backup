import json

def process_photos(photo_data):
    photos = photo_data['response']['items']
    processed_photos = []
    for photo in photos:
        likes = photo['likes']['count']
        sizes = photo['sizes']
        max_size_photo = max(sizes, key=lambda size: size['height'] * size['width'])
        file_name = f"{likes}.jpg"
        processed_photos.append({
            'file_name': file_name,
            'size': max_size_photo['type'],
            'url': max_size_photo['url']
        })
    return processed_photos

def save_to_json(data, filename='photos_info.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
        