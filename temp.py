import pygame
import os
from System import *
from images.images import *


def exit(*args):
    global running
    running = False


def the_end():
    start_new_game()
    opening_main_window()


def start_new_game(*args):
    description_map = open('map/description_map.txt', 'w')
    with open('map/start_description_map.txt', 'r') as f:
        text = f.read()
    description_map.write(text)
    description_map.close()

    description_player = open('data/SaveGame.txt', 'w')
    text = '''0;100;100;0;0;100;0;36.6;50000;0;0;0;0;0;5;5;0;1.5;3;-0.5;0;4;0;0;622080000</>
21;30;0, 33;5;720, 26;2;0, 25;1;0, 28;1;19000, 4;40;0</>'''
    description_player.write(text)
    description_player.close()
    start()


def continue_game(*args):
    if os.path.exists('map/description_map.txt'):
        start()
    else:
        start_new_game()


def searching_on_call(*args):
    call = BOARD_MAP.get_call_in_bord((player.x, player.y))
    call.find_things()
    location.update_thinks(location.convert_thinks_to_object(call.lies.split(';'), ':'))


def save():
    description_player = open('data/SaveGame.txt', 'w')
    text = ''
    text += str(int(player.exhaustion)) + ';'
    text += str(int(player.hunger)) + ';'
    text += str(int(player.water)) + ';'
    text += str(int(player.poison)) + ';'
    text += str(int(player.radiation)) + ';'
    text += str(int(player.energy)) + ';'
    text += str(int(player.bleeding)) + ';'
    text += str(player.temperature) + ';'
    text += str(player.max_heft) + ';'

    text += str(player.armor) + ';'
    text += str(player.xp_chemistry) + ';'
    text += str(player.xp_survival) + ';'
    text += str(player.xp_mechanics) + ';'
    text += str(player.xp_sewing) + ';'

    text += str(player.x) + ';'
    text += str(player.y) + ';'

    text += str(player.change_exhaustion) + ';'
    text += str(player.change_hunger) + ';'
    text += str(player.change_water) + ';'
    text += str(player.change_poison) + ';'
    text += str(player.change_radiation) + ';'
    text += str(player.change_energy) + ';'
    text += str(player.change_bleeding) + ';'
    text += str(player.change_temperature) + ';'

    text += str(int(game_time.num_time)) + '</>\n'
    text += inventory.get_text_for_saving()

    description_player.write(text)
    description_player.close()

    description_map = open('map/description_map.txt', 'w')
    text = ''
    for i in range(BOARD_MAP.height):
        for j in range(BOARD_MAP.width):
            description_call = BOARD_MAP.board[i][j].get_text_for_save()
            text = text + description_call
    description_map.write(text)
    description_map.close()


def start(*args):
    global type_window, inventory, location, BOARD_MAP
    for button in objects_main['objects']:
        button.visibility = False
    for object in objects_main['buttons']:
        object.visibility = False
    main_map.visibility = True
    player.set_parametrs(open_file())

    inventory = Inventory(screen, None, player, parametrs=open_file())
    inventory.bg_image = get_bg_for_inventory((width, ps_height(83.2)))

    file = open('map/description_map.txt', 'r')
    font = pygame.font.Font(None, zoom * 10)
    BOARD_MAP = Board(screen, 3906 // size_cell, 2047 // size_cell, font,
                      size_cell, parametrs=file.read())
    call = BOARD_MAP.get_call_in_bord((player.x, player.y))
    location = Inventory(screen, None, player, parametrs=call.get_text_for_save(), mod=2)
    location.bg_image = get_bg_for_inventory((width, ps_height(83.2)))

    update_map()

    type_window = 'main'

def show_and_change_all_options():
    texts_of_options_player[0].text = int(player.exhaustion)
    texts_of_options_player[1].text = int(player.hunger)
    texts_of_options_player[2].text = int(player.water)
    texts_of_options_player[3].text = int(player.poison)
    texts_of_options_player[4].text = int(player.radiation)
    texts_of_options_player[5].text = int(player.energy)
    texts_of_options_player[6].text = inventory.get_ps_of_load()
    texts_of_options_player[7].text = int(player.bleeding)
    texts_of_options_player[8].text = player.temperature
    for text in texts_of_options_player:
        text.show()


def opening_inventory(*args):
    global type_window
    inventory.visibility = True
    location.visibility = False
    player.stop()
    type_window = 'inventory'


def change_inventory_type_to_location(*args):
    global location, type_window
    type_window = 'inventory'
    inventory.visibility = False

    call = BOARD_MAP.get_call_in_bord((player.x, player.y))
    if 'NONE' not in call.lies:
        location.update_thinks(location.convert_thinks_to_object(call.lies.split(';'), ':'))
    else:
        location.update_thinks(location.convert_thinks_to_object([]))

    location.visibility = True




def opening_quests(*args):
    global type_window
    player.stop()
    type_window = 'quests'


def opening_statistics(*args):
    global type_window
    player.stop()
    type_window = 'statistics'


def opening_main_window(*args):
    global type_window
    player.stop()
    save()
    for button in objects_main['objects']:
        button.visibility = True
    for object in objects_main['buttons']:
        object.visibility = True
    main_map.visibility = False
    type_window = 'main_window'


def open_map(*args):
    global type_window
    inventory.visibility = False
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
    global texts_of_options_player, btn_searching

    image = get_bg_main_window(size)
    bg_main_window = Object(screen, image, 0, 0, *size)

    image = get_btn_exit_main((200, 50))
    image_2 = get_btn_exit_main_click((200, 50))
    btn_exit_main = Button(screen, image, width / 2 - 100, height / 2 + 300, 200, 50, exit, image_2)

    image = get_btn_start_main((200, 50))
    image_2 = get_btn_start_main_click((200, 50))
    btn_continue_game_main = Button(screen, image, width / 2 - 100, height / 2 + 200,
                           200, 50, continue_game, image_2)

    image = get_image_btn_new_start_main((200, 50))
    image_2 = get_image_btn_new_start_main_click((200, 50))
    btn_start_new_main = Button(screen, image, width / 2 - 100, height / 2 + 100,
                            200, 50, start_new_game, image_2)

    image = get_pygame_image(image_map)
    main_map = Object(screen, image, map_x, map_y, 3906 * zoom, 2047 * zoom)
    main_map.visibility = False

    objects_main['objects'].append(bg_main_window)
    objects_main['buttons'].append(btn_exit_main)
    objects_main['buttons'].append(btn_continue_game_main)
    objects_main['buttons'].append(btn_start_new_main)

    image = get_image_btn_for_main_map_window((ps_width(14.2), ps_height(9.9)))
    btn = Button(screen, image, 0, ps_height(89.6), ps_width(14.2), ps_height(9.9))
    btn.add_function(opening_main_window)
    objects_map['buttons'].append(btn)

    image = get_image_btn_for_main_map_window((ps_width(14.2), ps_height(9.9)))
    btn = Button(screen, image, ps_width(14.2), ps_height(89.6), ps_width(14.2), ps_height(9.9))
    btn.add_function(opening_statistics)
    objects_map['buttons'].append(btn)

    image = get_image_btn_for_main_map_window((ps_width(14.2), ps_height(9.9)))
    btn = Button(screen, image, ps_width(28.6), ps_height(89.6), ps_width(14.2), ps_height(9.9))
    btn.add_function(opening_quests)
    objects_map['buttons'].append(btn)

    image = get_image_btn_for_main_map_window((ps_width(14.2), ps_height(9.9)))
    btn = Button(screen, image, ps_width(85.8), ps_height(89.6), ps_width(14.2), ps_height(9.9))
    btn.add_function(open_map)
    objects_map['buttons'].append(btn)

    image = get_image_btn_for_main_map_window((ps_width(14.2), ps_height(9.9)))
    btn = Button(screen, image, ps_width(71.6), ps_height(89.6), ps_width(14.2), ps_height(9.9))
    btn.add_function(change_inventory_type_to_location)
    objects_map['buttons'].append(btn)

    image = get_image_btn_for_main_map_window((ps_width(14.2), ps_height(9.9)))
    btn = Button(screen, image, ps_width(57.4), ps_height(89.6), ps_width(14.2), ps_height(9.9))
    btn.add_function(opening_inventory)
    objects_map['buttons'].append(btn)


    file = open('map/description_map.txt', 'r')
    font = pygame.font.Font(None, zoom * 10)
    BOARD_MAP = Board(screen, 3906 // size_cell, 2047 // size_cell, font,
                      size_cell, parametrs=file.read())
    zoom_images = [None for i in range(6)]

    main_objects_bar = Object(screen, get_image_main_objectsbar(
        (width, ps_height(5.6))), 0, 0, width, ps_height(5.6))
    objects_map['objects'].append(main_objects_bar)
    main_btn_bar = Object(screen, get_image_main_btnbar(
        (width, ps_height(11.2))), 0, ps_height(88.8), width, ps_height(11.2))
    objects_map['objects'].append(main_btn_bar)

    texts_of_options_player = []
    font = pygame.font.Font(None, ps_width(2.5))

    text = Text(screen, ps_width(10), 15, player.exhaustion, font)
    texts_of_options_player.append(text)
    text = Text(screen, ps_width(19.5), 15, player.hunger, font)
    texts_of_options_player.append(text)
    text = Text(screen, ps_width(29), 15, player.water, font)
    texts_of_options_player.append(text)
    text = Text(screen, ps_width(39), 15, player.poison, font)
    texts_of_options_player.append(text)
    text = Text(screen, ps_width(49), 15, player.radiation, font)
    texts_of_options_player.append(text)
    text = Text(screen, ps_width(58), 15, player.energy, font)
    texts_of_options_player.append(text)
    text = Text(screen, ps_width(68), 15, inventory.get_ps_of_load(), font)
    texts_of_options_player.append(text)
    text = Text(screen, ps_width(78.3), 15, player.bleeding, font)
    texts_of_options_player.append(text)
    text = Text(screen, ps_width(87.7), 15, player.temperature, font)
    texts_of_options_player.append(text)

    image = get_image_btn_inventory_on_location((ps_width(7.5), ps_height(17.9)))
    btn = Button(screen, image, ps_width(0.7), ps_height(8), ps_width(7.5), ps_height(17.9))
    btn.add_function(opening_inventory)
    objects_inventory['buttons'].append(btn)

    image = get_image_btn_search((ps_width(14), ps_height(5)))
    btn_searching = Button(screen, image, ps_width(60), ps_height(50), ps_width(14), ps_height(5))
    btn_searching.add_function(searching_on_call)




FPS = 100
ratio = 3 / 5
zoom = 2
zoom_plus = 1.2
timer_between_clicks = 0
size_cell = 10
old_mouse_x, old_mouse_y = 0, 0
map_x, map_y = 0, 0
BOARD_MAP = None


player_x, player_y = 0, 0
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
objects_map = {'objects': [], 'buttons': []}
objects_inventory = {'objects': [], 'buttons': []}
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
install_size(size)

game_time = GameTime(0, screen)
player = Player(screen, player_x, player_y, game_time)
player.deathing = the_end
inventory = Inventory(screen, None, player)
location = Inventory(screen, None, player)

create_all_objects()
update_image_map()

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
            save()

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if type_window == 'main_window':
                for button in objects_main['buttons']:
                    if button.check_tip(x, y):
                        button.status = True
            if type_window != 'main_window':
                for button in objects_map['buttons']:
                    if button.check_tip(x, y):
                        button.status = True
            if type_window == 'inventory':
                for button in objects_inventory['buttons']:
                    if button.check_tip(x, y):
                        button.status = True
                if location.visibility and btn_searching.check_tip(x, y):
                    btn_searching.status = True

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

            if type_window == 'inventory':
                if event.button == 5:  # скрол вниз
                    if inventory.window.check_tip(x, y) and inventory.visibility:
                        inventory.window.pag(inventory.window.shift_y - 50)
                if event.button == 5:
                    if location.window.check_tip(x, y) and location.visibility:
                        location.window.pag(location.window.shift_y - 50)

                if event.button == 4:  # скрол вниз
                    if inventory.window.check_tip(x, y) and inventory.visibility:
                        inventory.window.pag(inventory.window.shift_y + 50)
                if event.button == 4:
                    if location.window.check_tip(x, y) and location.visibility:
                        location.window.pag(location.window.shift_y + 50)

                if event.button == 1:   # левое нажатие мыши
                    if inventory.window.check_tip(x, y) and inventory.visibility:
                        inventory.window.paging = True
                if event.button == 1:
                    if location.window.check_tip(x, y) and location.visibility:
                        location.window.paging = True


        if event.type == pygame.MOUSEBUTTONUP:
            x, y = event.pos
            if type_window == 'main_window':
                for button in objects_main['buttons']:
                    if button.status and button.check_tip(x, y):
                        button.click()
                    button.status = False
            if type_window != 'main_window':
                for button in objects_map['buttons']:
                    if button.status and button.check_tip(x, y):
                        button.click()
                    button.status = False
            if type_window == 'inventory':
                for button in objects_inventory['buttons']:
                    if button.status and button.check_tip(x, y):
                        button.click()
                    button.status = False

                if location.visibility and btn_searching.check_tip(x, y):
                    btn_searching.click()
                    btn_searching.status = False

            inventory.window.paging = False
            location.window.paging = False
            moving_map = False

        if event.type == pygame.MOUSEMOTION:
            x, y = event.pos
            shift_x = old_mouse_x - x
            shift_y = old_mouse_y - y
            old_mouse_x, old_mouse_y = x, y

            if moving_map:
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

            if inventory.window.paging:
                inventory.window.pag(inventory.window.shift_y - shift_y)
            if location.window.paging:
                location.window.pag(location.window.shift_y - shift_y)


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
                player.check_condition(call)

                if not player.moving:
                    # вызывается если игрок остановился после
                    # своего последнего шага
                    player_x_on_map = player.x - map_x_on_main_map
                    player_y_on_map = player.y - map_y_on_main_map
                    if (player_x_on_map < 50 or player_y_on_map < 50 or
                            player_x_on_map > width_map - 150 or player_y_on_map > height_map - 150):
                        update_map()


    if type_window == 'inventory':
        inventory.show()
        location.show()
        for object in objects_inventory['objects']:
            object.show()
        for object in objects_inventory['buttons']:
            object.show()
        if location.visibility:
            btn_searching.show()

    if type_window != 'main_window':
        for object in objects_map['objects']:
            object.show()
        for object in objects_map['buttons']:
            object.show()
        show_and_change_all_options()
        game_time.show()
        game_time.update_time_on_real_time()

    pygame.display.flip()

pygame.quit()
