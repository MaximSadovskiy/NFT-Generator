import os
import random

from PIL import Image, ImageDraw, ImageFont
from Logic import CharacterCreation, ItemsCreation
from Logic.Source import RGB_SOFT_BASE, WIDTH, HEIGHT, RESULT_PATH, ITEMS_PATH

def create_image(image_name, folder_name):
    background = random.choice(RGB_SOFT_BASE)
    img = Image.new("RGB", (WIDTH, HEIGHT), background)

    CharacterCreation.add_character(img)
    add_items_to_image(img)

    save_image(image_name, img, folder_name)

def save_image(image_name, img, folder_name):
    image_name = str(image_name)
    img_path = f"{RESULT_PATH}{folder_name}/{image_name}.png"
    folder_path = f"{RESULT_PATH}{folder_name}"
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
    if not os.path.exists(img_path):
        img.save(img_path)
    else:
        image_name += " f"
        save_image(image_name, img, folder_name)

def add_items_to_image(img):
    ITEMS_LIST = ItemsCreation.get_items_list(ITEMS_PATH)
    for item in ITEMS_LIST:
        ItemsCreation.add_item(item, img)

@DeprecationWarning
def generate_text():
    overlay = Image.new("RGBA", (500, 150), color=(0, 0, 0, 80))
    dr1 = ImageDraw.Draw(overlay)
    fnt = ImageFont.truetype('data/fonts/Ubuntu-Bold.ttf', size=104)
    text = "PLACEHOLDER".encode("utf-8").hex()
    dr1.text(
        (14, 14),
        f"0x{text}",
        font=fnt,
        fill=(255, 255, 255, 160),
    )
    return overlay