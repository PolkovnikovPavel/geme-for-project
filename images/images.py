from PIL import Image, ImageOps
import pygame


def get_bg_main_window(size):
    bg_main_window = Image.open('images/bg_main_window.png')
    bg_main_window = bg_main_window.resize(size, Image.ANTIALIAS)

    mode = bg_main_window.mode
    data = bg_main_window.tobytes()
    bg_main_window = pygame.image.fromstring(data, size, mode)
    return bg_main_window

def get_bg_tool_bar_map(size):
    bg_tool_bar_map = Image.open('images/bg_tool_bar_map.png')
    bg_tool_bar_map = bg_tool_bar_map.resize(size, Image.ANTIALIAS)

    mode = bg_tool_bar_map.mode
    data = bg_tool_bar_map.tobytes()
    bg_tool_bar_map = pygame.image.fromstring(data, size, mode)
    return bg_tool_bar_map


def get_btn_exit_main(size):
    btn_exit_main = Image.open('images/btn_exit_main.png')
    btn_exit_main = btn_exit_main.resize(size, Image.ANTIALIAS)

    mode = btn_exit_main.mode
    data = btn_exit_main.tobytes()
    btn_exit_main = pygame.image.fromstring(data, size, mode)
    return btn_exit_main


def get_btn_exit_main_click(size):
    btn_exit_main = Image.open('images/btn_exit_main_click.png')
    btn_exit_main = btn_exit_main.resize(size, Image.ANTIALIAS)

    mode = btn_exit_main.mode
    data = btn_exit_main.tobytes()
    btn_exit_main = pygame.image.fromstring(data, size, mode)
    return btn_exit_main


def get_btn_start_main_click(size):
    btn_start_main_click = Image.open('images/btn_start_main_click.png')
    btn_start_main_click = btn_start_main_click.resize(size, Image.ANTIALIAS)

    mode = btn_start_main_click.mode
    data = btn_start_main_click.tobytes()
    btn_start_main_click = pygame.image.fromstring(data, size, mode)
    return btn_start_main_click


def get_btn_start_main(size):
    btn_start_main = Image.open('images/btn_start_main.png')
    btn_start_main = btn_start_main.resize(size, Image.ANTIALIAS)

    mode = btn_start_main.mode
    data = btn_start_main.tobytes()
    btn_start_main = pygame.image.fromstring(data, size, mode)
    return btn_start_main


def get_btn_save_map(size):
    btn = Image.open('images/btn_save_map.png')
    btn = btn.resize(size, Image.ANTIALIAS)

    mode = btn.mode
    data = btn.tobytes()
    btn = pygame.image.fromstring(data, size, mode)
    return btn


def get_btn_save_map_click(size):
    btn = Image.open('images/btn_save_map_click.png')
    btn = btn.resize(size, Image.ANTIALIAS)

    mode = btn.mode
    data = btn.tobytes()
    btn = pygame.image.fromstring(data, size, mode)
    return btn

def get_image_player_on_mao(size):
    image = Image.open('images/player_on_map.png')
    image = image.resize(size, Image.ANTIALIAS)

    mode = image.mode
    data = image.tobytes()
    image = pygame.image.fromstring(data, size, mode)
    return image


def get_image_main_objectsbar(size):
    image = Image.open('images/main_objectsbar.png')
    image = image.resize(size, Image.ANTIALIAS)

    mode = image.mode
    data = image.tobytes()
    image = pygame.image.fromstring(data, size, mode)
    return image


def get_image_main_btnbar(size):
    image = Image.open('images/main_btnbar.png')
    image = image.resize(size, Image.ANTIALIAS)

    mode = image.mode
    data = image.tobytes()
    image = pygame.image.fromstring(data, size, mode)
    return image


def get_bg_for_inventory(size):
    image = Image.open('images/bg_for_inventiry.png')
    image = image.resize(size, Image.ANTIALIAS)

    mode = image.mode
    data = image.tobytes()
    image = pygame.image.fromstring(data, size, mode)
    return image


def get_bg_for_thinks_in_inventory(size):
    image = Image.open('images/bg_for_thinks_in_inventory.png')
    image = image.resize(size, Image.ANTIALIAS)

    mode = image.mode
    data = image.tobytes()
    image = pygame.image.fromstring(data, size, mode)
    return image


def get_image_btn_for_main_map_window(size):
    image = Image.open('images/btn_for_main_map_window.jpg')
    image = image.resize(size, Image.ANTIALIAS)

    mode = image.mode
    data = image.tobytes()
    image = pygame.image.fromstring(data, size, mode)
    return image


def get_image_btn_new_start_main(size):
    image = Image.open('images/btn_new_start_main.png')
    image = image.resize(size, Image.ANTIALIAS)

    mode = image.mode
    data = image.tobytes()
    image = pygame.image.fromstring(data, size, mode)
    return image


def get_image_btn_new_start_main_click(size):
    image = Image.open('images/btn_new_start_main_click.png')
    image = image.resize(size, Image.ANTIALIAS)

    mode = image.mode
    data = image.tobytes()
    image = pygame.image.fromstring(data, size, mode)
    return image


def get_image_btn_inventory_on_location(size):
    image = Image.open('images/btn_inventory_on_location.png')
    image = image.resize(size, Image.ANTIALIAS)

    mode = image.mode
    data = image.tobytes()
    image = pygame.image.fromstring(data, size, mode)
    return image


def get_image_btn_search(size):
    image = Image.open('images/btn_search.png')
    image = image.resize(size, Image.ANTIALIAS)

    mode = image.mode
    data = image.tobytes()
    image = pygame.image.fromstring(data, size, mode)
    return image



def get_map(size, mod=0):
    map = Image.open('images/map.png')
    map = map.resize(size, Image.ANTIALIAS)
    if mod == 1:
        return map
    mode = map.mode
    data = map.tobytes()
    map = pygame.image.fromstring(data, size, mode)
    return map



def cat_image(img, border):
    img = ImageOps.crop(img, border)
    return img


def get_pygame_image(image):
    mode = image.mode
    size = image.size
    data = image.tobytes()
    return pygame.image.fromstring(data, size, mode)


def resize_image(image, size):
    image = image.resize(size, Image.ANTIALIAS)
    return image


def get_free_image(name, size, mod=0):
    image = Image.open(name)
    image = image.resize(size, Image.ANTIALIAS)
    if mod == 1:
        return image
    mode = image.mode
    data = image.tobytes()
    image = pygame.image.fromstring(data, size, mode)
    return image
