import pygame
import os
from game.System import *
from game.images.images import *


def exit(*args):
    global running
    running = False

def save(*args):
    description_map = open('map/start_description_map.txt', 'w')
    text = ''
    for i in range(BOARD.height):
        for j in range(BOARD.width):
            description_call = BOARD.board[i][j].get_text_for_save()
            text = text + description_call
    description_map.write(text)
    description_map.close()


def start(*args):
    global type_window
    for button in buttons_main:
        button.visibility = False
    for object in objects_main:
        object.visibility = False
    main_map.visibility = True
    type_window = 'editor'


def create_all_objects():
    global main_map, BOARD, parametrs, tool_bar_map
    image = get_bg_main_window(size)
    bg_main_window = Object(screen, image, 0, 0, *size)

    image = get_btn_exit_main((200, 50))
    image_2 = get_btn_exit_main_click((200, 50))
    btn_exit_main = Button(screen, image, width / 2 - 100, height / 2 + 300, 200, 50, exit, image_2)

    image = get_btn_start_main((200, 50))
    image_2 = get_btn_start_main_click((200, 50))
    btn_start_main = Button(screen, image, width / 2 - 100, height / 2 + 200,
                           200, 50, start, image_2)

    image = get_btn_save_map((200, 50))
    image_2 = get_btn_save_map_click((200, 50))
    btn_save_map = Button(screen, image, width - 220, height - 72, 200, 50, save, image_2)

    image = get_pygame_image(image_map)
    main_map = Object(screen, image, map_x, map_y, 3906 * zoom, 2047 * zoom)
    main_map.visibility = False

    objects_main.append(bg_main_window)
    buttons_main.append(btn_exit_main)
    buttons_main.append(btn_start_main)
    buttons_map.append(btn_save_map)

    file = open('map/start_description_map.txt', 'r')
    font = pygame.font.Font(None, zoom * 10)
    BOARD = Board(screen, 3906 // 10, 2047 // 10, font, 10 * zoom, parametrs=file.read())

    image = get_bg_tool_bar_map((200, 1005))
    tool_bar_map = Window(screen, image, 0, 0, 200, 1005, 3)
    tool_bar_map.mod = False

    count_btns_for_tool_bar_map = 46
    for i in range(count_btns_for_tool_bar_map):
        name = 'images/editor/btn_toolbar_' + str(i) + '.png'
        image = get_free_image(name, (50, 50))
        name = 'images/editor/btn2_toolbar_' + str(i) + '.png'
        image_2 = get_free_image(name, (50, 50))

        btn = Button(screen, image, 0, 0, 50, 50, change_parametrs, image_2)
        btn.id = i
        tool_bar_map.add_object(btn)

    parametrs = '''0;(x,y);0;0;1
NONE
NONE
NONE'''


FPS = 100

ratio = 3 / 5
zoom_plus = 1
zoom = 1
old_x, old_y = 0, 0
map_x, map_y = 0, 0
x_on_map, y_on_map = 0, 0
width_map, height_map = 3906, 2047
main_map = None

main_image_map = get_map((3906, 2047), 1)
image_map = cat_image(main_image_map, (x_on_map, y_on_map,
                      3906 - width_map - x_on_map, 2047 - height_map - y_on_map))

objects_main = []
buttons_main = []
buttons_map = []


type_window = 'main'


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
running = True
moving_map = False
highlighting_call = False
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
            for button in buttons_main:
                if button.check_tip(x, y):
                    button.status = True
            for button in buttons_map:
                if button.check_tip(x, y):
                    button.status = True
            if type_window == 'editor':
                if event.button == 1:
                    moving_map = True
                    old_x, old_y = x, y
                    if tool_bar_map.check_tip(x, y):
                        moving_map = False
                        tool_bar_map.paging = True
                        for object in tool_bar_map.objects:
                            if object.check_tip(x, y):
                                for i in tool_bar_map.objects:
                                    i.status = False
                                object.status = True

                elif event.button == 3:
                    highlighting_call = True


            if event.button == 5:  # скрол вниз
                zoom -= zoom_plus
                if zoom < 0.6:
                    zoom += zoom_plus
                else:
                    image = resize_image(image_map, (int(width_map * zoom), int(height_map * zoom)))
                    image = get_pygame_image(image)
                    main_map.change_image(image)
                    map_x = map_x - int((width_map * zoom) - (width_map * (zoom * zoom_plus))) // 2
                    map_y = map_y - int((height_map * zoom) - (height_map * (zoom * zoom_plus))) // 2
                    main_map.move_to(map_x, map_y)
                    BOARD.change_size_call(int(10 * zoom))

                    font = pygame.font.Font(None, zoom * 10)
                    BOARD.font = font

            if event.button == 4:   # скрол вверх
                zoom += zoom_plus
                if zoom > 4:
                    zoom -= zoom_plus
                else:
                    image = resize_image(image_map, (int(width_map * zoom), int(height_map * zoom)))
                    image = get_pygame_image(image)
                    main_map.change_image(image)
                    map_x = map_x - int((width_map * zoom) - (width_map * (zoom / zoom_plus))) // 2
                    map_y = map_y - int((height_map * zoom) - (height_map * (zoom / zoom_plus))) // 2
                    main_map.move_to(map_x, map_y)
                    BOARD.change_size_call(int(10 * zoom))

                    font = pygame.font.Font(None, zoom * 10)
                    BOARD.font = font

        if event.type == pygame.MOUSEBUTTONUP:
            x, y = event.pos
            for button in buttons_main:
                if button.status and button.check_tip(x, y):
                    button.click()
                button.status = False
            for button in buttons_map:
                if button.status and button.check_tip(x, y):
                    button.click()
                button.status = False
            for object in tool_bar_map.objects:
                if object.check_tip(x, y):
                    object.status = True
                    parametrs = object.click(object.id)

            moving_map = False
            highlighting_call = False
            tool_bar_map.paging = False

        if event.type == pygame.MOUSEMOTION:
            x, y = event.pos
            if moving_map:
                shift_x = old_x - x
                shift_y = old_y - y
                old_x, old_y = x, y
                map_x = map_x - shift_x
                map_y = map_y - shift_y
                main_map.move_to(map_x, map_y)
            BOARD.set_move(map_x, map_y)

            if highlighting_call:
                coord = BOARD.get_cell((x, y))
                if coord is not None:
                    j, i = coord
                    BOARD.board[i][j].change_parametrs(parametrs)
            if tool_bar_map.paging:
                tool_bar_map.pag(tool_bar_map.shift_y - (old_y - y))
                old_x, old_y = x, y

    if type_window == 'main':
        for object in objects_main:
            object.show()
        for button in buttons_main:
            button.show()
    main_map.show()

    if highlighting_call:
        coord = BOARD.get_cell((x, y))
        if coord is not None:
            j, i = coord
            BOARD.board[i][j].change_parametrs(parametrs)

    if type_window == 'editor':
        BOARD.render()
        tool_bar_map.render()
        for button in buttons_map:
            button.show()
    pygame.display.flip()

pygame.quit()
