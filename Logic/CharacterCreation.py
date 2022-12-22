import random

from PIL import Image
from Logic import Source
from Logic.Source import WIDTH, HEIGHT


def add_character(img):
    character_image = Image.open(Source.CHARACTER_PATH).convert("RGBA")
    change_character_color(character_image)

    img.paste(character_image, (0, 0), character_image)

def change_character_color(character_image):
    character_pixels = character_image.load()
    # Генерируем диапазон смещения байта RGBA
    r_byte = random.randint(0, 70)
    g_byte = random.randint(0, 70)
    b_byte = random.randint(0, 70)

    # Редактируем пиксели слайма
    for w in range(WIDTH):
        for h in range(HEIGHT):
            # Получаем текущий пиксель и кортеж RGBA
            pixel = character_pixels[w, h]

            if pixel != (0, 0, 0, 0):
                # Меняем цвет на рандомный диапазон
                # Красим только объект слайма
                character_pixels[w, h] = (
                    pixel[0] + r_byte,
                    pixel[1] + g_byte,
                    pixel[2] + b_byte,
                    255)
