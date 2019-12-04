import pygame
import os
from game.Sistem import *
from game.images.images import *


def exit(*args):
    global running
    running = False

def save(*args):
    pass


def start(*args):
    global type_window
    for button in objects_main['objects']:
        button.visibility = False
    for object in objects_main['buttons']:
        object.visibility = False
    main_map.visibility = True
    type_window = 'main'


def update_map():   # сдвинуть отображаемую облость карты
    global image_map, zoom_images, map_x_on_main_map, map_y_on_main_map

    last_map_x, last_map_y = map_x_on_main_map, map_y_on_main_map

    if player.x > width_map / 2:
        if player.x > 3906 - width_map / 2:
            map_x_on_main_map = 3906 - width_map
        else:
            map_x_on_main_map = player.x - width_map // 2
    else:
        map_x_on_main_map = 0

    if player.y > height_map / 2:
        if player.y > 2047 - height_map / 2:
            map_y_on_main_map = 2047 - height_map
        else:
            map_y_on_main_map = player.y - height_map // 2
    else:
        map_y_on_main_map = 0

    if last_map_x == map_x_on_main_map and last_map_y == map_y_on_main_map:
        return

    image_map = cat_image(main_image_map,
                          (map_x_on_main_map, map_y_on_main_map,
                           3906 - width_map - map_x_on_main_map,
                           2047 - height_map - map_y_on_main_map))
    zoom_images = [None for i in range(6)]
    update_image_map()


def update_image_map():
    global zoom_images
    if zoom_images[zoom] is not None:
        image = zoom_images[zoom][0]
    else:
        new_zoom = 2
        for i in range(zoom):
            new_zoom *= zoom_plus
        image = resize_image(image_map,
                             (int(width_map * new_zoom), int(height_map * new_zoom)))
        image = get_pygame_image(image)

        zoom_images[zoom] = (image, int(size_cell * new_zoom), new_zoom)
    main_map.change_image(image)


def create_all_objects():
    global main_map, BOARD_MAP, parametrs, tool_bar_map, zoom_images, player
    image = get_bg_main_window(size)
    bg_main_window = Object(screen, image, 0, 0, *size)

    image = get_btn_exit_main((200, 50))
    image_2 = get_btn_exit_main_click((200, 50))
    btn_exit_main = Button(screen, image, width / 2 - 100, height / 2 + 300, 200, 50, exit, image_2)

    image = get_btn_start_main((200, 50))
    image_2 = get_btn_start_main_click((200, 50))
    btn_start_main = Button(screen, image, width / 2 - 100, height / 2 + 200,
                           200, 50, start, image_2)

    image = get_pygame_image(image_map)
    main_map = Object(screen, image, map_x, map_y, 3906 * zoom, 2047 * zoom)
    main_map.visibility = False

    objects_main['objects'].append(bg_main_window)
    objects_main['buttons'].append(btn_exit_main)
    objects_main['buttons'].append(btn_start_main)

    file = open('map/description_map.txt', 'r')
    font = pygame.font.Font(None, zoom * 10)
    BOARD_MAP = Board(screen, 3906 // size_cell, 2047 // size_cell, font,
                      size_cell, parametrs=file.read())
    zoom_images = [None for i in range(6)]


FPS = 100

ratio = 3 / 5
zoom = 2
zoom_plus = 1.2
timer_between_clicks = 0
size_cell = 10
old_mouse_x, old_mouse_y = 0, 0
map_x, map_y = 0, 0
BOARD_MAP = None


player_x, player_y = 2000, 0
width_map, height_map = 900, 900

if player_x > width_map / 2:
    map_x_on_main_map = player_x - width_map // 2
else:
    map_x_on_main_map = 0
if player_y > height_map / 2:
    map_y_on_main_map = player_y - height_map // 2
else:
    map_y_on_main_map = 0

main_map = None

main_image_map = get_map((3906, 2047), 1)
image_map = cat_image(main_image_map, (map_x_on_main_map, map_y_on_main_map,
                      3906 - width_map - map_x_on_main_map,
                      2047 - height_map - map_y_on_main_map))

objects_main = {'objects': [], 'buttons': []}
type_window = 'main_window'


pygame.init()

display = pygame.display.Info()
width, height = display.current_w - 75, display.current_h - 75
if width * ratio <= height:
    height = int(width * ratio)
else:
    width = int(height / ratio)
size = width, height
print(size)
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (30, 30)
screen = pygame.display.set_mode(size)

create_all_objects()
update_image_map()

player = Player(screen, player_x, player_y)
running = True
moving_map = False
clock = pygame.time.Clock()
x, y = 0, 0

while running:
    clock.tick(FPS)
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            for button in objects_main['buttons']:
                if button.check_tip(x, y):
                    button.status = True

            if type_window == 'main':
                if event.button == 1:
                    moving_map = True
                    old_mouse_x, old_mouse_y = x, y

                if event.button == 5:  # скрол вниз
                    zoom -= 1
                    if zoom < 0:
                        zoom = 0
                    else:
                        update_image_map()

                if event.button == 4:   # скрол вверх
                    zoom += 1
                    if zoom > len(zoom_images) - 1:
                        zoom = len(zoom_images) - 1
                    else:
                        update_image_map()
                if event.button == 1:   # левое нажатие мыши
                    if time.time() - timer_between_clicks < 0.3:
                        new_x = ((x - map_x) / zoom_images[zoom][2]) + map_x_on_main_map
                        new_y = ((y - map_y) / zoom_images[zoom][2]) + map_y_on_main_map
                        player.move_to(new_x, new_y)

                    timer_between_clicks = time.time()

        if event.type == pygame.MOUSEBUTTONUP:
            x, y = event.pos
            for button in objects_main['buttons']:
                if button.status and button.check_tip(x, y):
                    button.click()
                button.status = False

            moving_map = False

        if event.type == pygame.MOUSEMOTION:
            x, y = event.pos
            if moving_map:
                shift_x = old_mouse_x - x
                shift_y = old_mouse_y - y
                old_mouse_x, old_mouse_y = x, y
                map_x = map_x - shift_x
                map_y = map_y - shift_y
                if map_x > 0:
                    map_x = 0
                if map_y > 0:
                    map_y = 0
                image_size= main_map.image.get_size()
                if map_x < -image_size[0] + width:
                    map_x = -image_size[0] + width
                if map_y < -image_size[1] + height:
                    map_y = -image_size[1] + height

                main_map.move_to(map_x, map_y)

    if type_window == 'main_window':
        for object in objects_main['objects']:
            object.show()
        for object in objects_main['buttons']:
            object.show()

    if type_window == 'main':
        main_map.show()
        player.show(map_x_on_main_map, map_y_on_main_map, map_x, map_y, zoom_images[zoom][2])
        if player.moving:   # сдвигает игрока на расчитаные по времени координаты
            player.made_step()
            call = BOARD_MAP.get_call_in_bord((player.x, player.y))
            if call is not None:
                player.speed = player.start_speed * float(call.speed)

                if not player.moving:
                    # вызывается если игрок остановился после
                    # своего последнего шага
                    player_x_on_map = player.x - map_x_on_main_map
                    player_y_on_map = player.y - map_y_on_main_map
                    if (player_x_on_map < 50 or player_y_on_map < 50 or
                            player_x_on_map > width_map - 150 or player_y_on_map > height_map - 150):
                        update_map()
    pygame.display.flip()

pygame.quit()
