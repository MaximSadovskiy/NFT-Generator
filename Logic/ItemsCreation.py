import math
import os
import random

from PIL import Image
from Logic.Source import EMPTY_PERCENTAGE

def add_item(name, img):
    items_length = read_items_length(name)
    item = get_item_from_folder(name, items_length)
    if item is not None:
        image = Image.open(f"data/items/{name}/{item}").convert("RGBA"), item[0]
        img.paste(image[0], (0, 0), image[0])

def get_item_from_folder(folder_name, items_length):
    if items_length <= 0:
        return None

    empty_chance = math.floor(items_length / 100 * EMPTY_PERCENTAGE)
    item_number = random.randint(0, items_length + empty_chance)
    if item_number <= items_length:
        return get_item(folder_name, item_number)
    else:
        return None

def get_item(folder_name, item_number):
    item_list = os.listdir(f"data/items/{folder_name}")
    if len(item_list) > 0:
        return item_list[item_number - 1]

def read_items_length(item_name):
    dir_path = f"data/items/{item_name}"
    if os.path.exists(dir_path):
        return count_files(dir_path)
    else:
        print(f"Не найден предмет с названием {item_name}")
        return 0

def count_files(dir_path):
    count = 0
    for file in os.scandir(dir_path):
        count += 1
    return count

def get_items_list(dir_path):
    return [name for name in os.listdir(dir_path) if os.path.isdir(os.path.join(dir_path, name))]