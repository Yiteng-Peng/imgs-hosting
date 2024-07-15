import os
import random
import string


IMG_URL = "https://raw.githubusercontent.com/Yiteng-Peng/imgs-hosting/main/"


def is_valid_hex(name):
    return len(name) == 12 and all(c in string.hexdigits for c in name)

def generate_random_hex_name():
    return ''.join(random.choices(string.hexdigits.lower(), k=12))

def rename_images():
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif']  # 可根据需要添加其他图片格式的扩展名
    new_name_list = []

    for file in os.listdir('.'):
        if os.path.isfile(file) and os.path.splitext(file)[1].lower() in image_extensions:
            name, ext = os.path.splitext(file)
            if not is_valid_hex(name):
                new_name = generate_random_hex_name() + ext
                new_name_list.append(new_name)
                os.rename(file, new_name)
                print(f'Renamed {file} to {new_name}')

    return new_name_list


new_name_list = rename_images()
for i in new_name_list:
    print(IMG_URL+i)
if len(new_name_list) == 0:
    print('No name is invalid.')