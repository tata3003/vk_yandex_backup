import os
from vk_api import VK
from yandex_disk import YandexDisk
from photo_processor import process_photos, save_to_json
from tqdm import tqdm

def main(vk_token, yandex_token, vk_user_id):
    vk = VK(vk_token, vk_user_id)
    yd = YandexDisk(yandex_token)

    photo_data = vk.get_photos()
    processed_photos = process_photos(photo_data)

    folder_name = f"vk_photos_{vk_user_id}"
    if yd.create_folder(folder_name):
        print(f"Folder '{folder_name}' created successfully on Yandex Disk")

    for photo in tqdm(processed_photos):
        file_path = f"{folder_name}/{photo['file_name']}"
        yd.upload_file(file_path, photo['url'])

    save_to_json(processed_photos)
    print("Photos have been uploaded and information saved to JSON file.")

if __name__ == "__main__":
    vk_token = input("Enter VK token: ")
    yandex_token = input("Enter Yandex Disk token: ")
    vk_user_id = input("Enter VK user ID: ")
    main(vk_token, yandex_token, vk_user_id)
    