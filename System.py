import pygame
import time
import sqlite3
from images.images import *


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 0, 255)
LIGHT_GREEN = (27, 65, 16)
BROWN = (74, 47, 4)
width, height = 0, 0


def install_size(size):
    global width, height
    width, height = size


def open_file():
    with open('data/SaveGame.txt', 'r') as f:
        read_data = f.read()
    return read_data


def change_parametrs(id):
    if id[0] == 0:
        parametrs = '''0;(x,y);0;-1;1
            NONE
            NONE
            NONE'''
    elif id[0] == 1:
        parametrs = '''1;(x,y);1000;0;0.05
            1:10000:0
            NONE
            NONE'''
    elif id[0] == 2:
        parametrs = '''2;(x,y);15;0;0.85
                    2:75:0;3:15:0
                    NONE
                    NONE'''
    elif id[0] == 3:
        parametrs = '''3;(x,y);0;0;1
            NONE
            NONE
            NONE'''
    elif id[0] == 4:
        parametrs = '''4;(x,y);0;0;1
            NONE
            NONE
            NONE'''
    elif id[0] == 5:
        parametrs = '''5;(x,y);0;0;1
            NONE
            NONE
            NONE'''
    elif id[0] == 6:
        parametrs = '''6;(x,y);0;0;1
            NONE
            NONE
            NONE'''
    elif id[0] == 7:
        parametrs = '''7;(x,y);0;0;1
            NONE
            NONE
            NONE'''
    elif id[0] == 8:
        parametrs = '''8;(x,y);0;0;1
            NONE
            NONE
            NONE'''
    elif id[0] == 9:
        parametrs = '''9;(x,y);0;0;1
            NONE
            NONE
            NONE'''
    elif id[0] == 10:
        parametrs = '''10;(x,y);0;0;1
            NONE
            NONE
            NONE'''
    elif id[0] == 11:
        parametrs = '''11;(x,y);0;0;1
            NONE
            NONE
            NONE'''
    elif id[0] == 12:
        parametrs = '''12;(x,y);0;0;1
            NONE
            NONE
            NONE'''
    elif id[0] == 13:
        parametrs = '''13;(x,y);0;0;1
            NONE
            NONE
            NONE'''
    elif id[0] == 14:
        parametrs = '''14;(x,y);0;0;1
            NONE
            NONE
            NONE'''
    elif id[0] == 15:
        parametrs = '''15;(x,y);0;0;1
            NONE
            NONE
            NONE'''
    elif id[0] == 16:
        parametrs = '''16;(x,y);0;0;1
            NONE
            NONE
            NONE'''
    elif id[0] == 17:
        parametrs = '''17;(x,y);0;0;1
            NONE
            NONE
            NONE'''
    elif id[0] == 18:
        parametrs = '''18;(x,y);0;0;1
            NONE
            NONE
            NONE'''
    elif id[0] == 19:
        parametrs = '''19;(x,y);0;0;1
            NONE
            NONE
            NONE'''
    elif id[0] == 20:
        parametrs = '''20;(x,y);0;0;1
            NONE
            NONE
            NONE'''
    elif id[0] == 21:
        parametrs = '''21;(x,y);0;0;1
            NONE
            NONE
            NONE'''
    elif id[0] == 22:
        parametrs = '''22;(x,y);0;0;1
            NONE
            NONE
            NONE'''
    elif id[0] == 23:
        parametrs = '''23;(x,y);0;0;1
            NONE
            NONE
            NONE'''
    elif id[0] == 24:
        parametrs = '''24;(x,y);0;0;1
            NONE
            NONE
            NONE'''
    elif id[0] ==25:
        parametrs = '''25;(x,y);0;0;1
            NONE
            NONE
            NONE'''
    elif id[0] == 26:
        parametrs = '''26;(x,y);0;0;1
            NONE
            NONE
            NONE'''
    elif id[0] == 27:
        parametrs = '''27;(x,y);0;0;1
            NONE
            NONE
            NONE'''
    elif id[0] == 28:
        parametrs = '''28;(x,y);0;0;1
            NONE
            NONE
            NONE'''
    elif id[0] == 29:
        parametrs = '''29;(x,y);0;0;1
            NONE
            NONE
            NONE'''
    elif id[0] == 30:
        parametrs = '''30;(x,y);0;0;1
            NONE
            NONE
            NONE'''
    elif id[0] == 31:
        parametrs = '''31;(x,y);0;0;1
            NONE
            NONE
            NONE'''
    elif id[0] == 32:
        parametrs = '''32;(x,y);0;0;1
            NONE
            NONE
            NONE'''
    elif id[0] == 33:
        parametrs = '''33;(x,y);0;0;1
            NONE
            NONE
            NONE'''
    elif id[0] == 34:
        parametrs = '''34;(x,y);0;0;1
            NONE
            NONE
            NONE'''
    elif id[0] == 35:
        parametrs = '''35;(x,y);0;0;1
            NONE
            NONE
            NONE'''
    elif id[0] == 36:
        parametrs = '''36;(x,y);0;0;1
            NONE
            NONE
            NONE'''
    elif id[0] == 37:
        parametrs = '''37;(x,y);0;0;1
            NONE
            NONE
            NONE'''
    elif id[0] == 38:
        parametrs = '''38;(x,y);0;0;1
            NONE
            NONE
            NONE'''
    elif id[0] == 39:
        parametrs = '''39;(x,y);0;0;1
            NONE
            NONE
            NONE'''
    elif id[0] == 40:
        parametrs = '''40;(x,y);0;0;1
            NONE
            NONE
            NONE'''
    elif id[0] == 41:
        parametrs = '''41;(x,y);0;0;1
            NONE
            NONE
            NONE'''
    elif id[0] == 42:
        parametrs = '''42;(x,y);0;0;1
            NONE
            NONE
            NONE'''
    elif id[0] == 43:
        parametrs = '''43;(x,y);0;0;1
            NONE
            NONE
            NONE'''
    elif id[0] == 44:
        parametrs = '''44;(x,y);0;0;1
            NONE
            NONE
            NONE'''
    elif id[0] == 45:
        parametrs = '''45;(x,y);0;0;1
            NONE
            NONE
            NONE'''
    else:
        parametrs = '''0;(x,y);0;0;1
            NONE
            NONE
            NONE'''
    return parametrs


def ps_height(percent):
    percent = percent / 100
    return int(height * percent)


def ps_width(percent):
    percent = percent / 100
    return int(width * percent)


class Object:
    def __init__(self, canvas, image, x, y, width, height):
        self.canvas = canvas
        self.image = image
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.visibility = True

    def move_to(self, x, y):
        self.x = x
        self.y = y

    def change_image(self, image):
        self.image = image

    def check_tip(self, x, y):
        if self.visibility:
            return (x >= self.x and x <= self.x + self.width and y >= self.y and
                    y <= self.y + self.height)

    def show(self):
        if self.visibility:
            self.canvas.blit(self.image, (self.x, self.y))


class Text(Object):
    def __init__(self, canvas, x, y, text, font):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.text = text
        self.font = font
        self.visibility = True

    def show(self):
        text = self.font.render(str(self.text), 1, WHITE)
        self.canvas.blit(text, (self.x, self.y))


class Button(Object):
    def __init__(self, canvas, image, x, y, width, height, function=None, image_animation=None):
        self.canvas = canvas
        self.image = image
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.function = [function]
        self.image_animation = image_animation
        self.visibility = True
        self.status = False

    def add_function(self, function):
        if self.function == [None]:
            self.function = [function]
        else:
            self.function.append(function)

    def get_function(self, function):
        self.function = [function]

    def del_function(self):
        self.function = [None]

    def get_image_animation(self, image):
        self.image_animation = image

    def show_animation(self):
        if self.image_animation is not None:
            self.canvas.blit(self.image_animation, (self.x, self.y))
        else:
            self.canvas.blit(self.image, (self.x, self.y))

    def click(self, *args):
        if self.function == [None] or not self.visibility:
            return False
        for function in self.function:
            try:
                return function(args)
            except:
                print('не удалось запустить функцию')
                return False

    def show(self):
        if self.visibility:
            if self.status:
                self.show_animation()
                return
            self.canvas.blit(self.image, (self.x, self.y))


class Call:
    def __init__(self, canvas, x, y, size, color=BLACK, parametrs=None):
        self.canvas = canvas
        self.size = size
        self.x = x
        self.y = y
        self.color = color
        self.visibility = True

        if parametrs is None:
            self.id = '0'
            self.cor = (x, y)
            self.count = 0
            self.rad = '-1'
            self.speed = 1
            self.can_find = 'NONE'
            self.can_attack = 'NONE'
            self.lies = 'NONE'
        else:
            parametrs = parametrs.split()
            self.id = parametrs[0].split(';')[0]
            self.cor = (x, y)
            self.count = int(parametrs[0].split(';')[2])
            self.rad = parametrs[0].split(';')[3]
            self.speed = parametrs[0].split(';')[4]
            self.can_find = parametrs[1]
            self.can_attack = parametrs[2]
            self.lies = parametrs[3]

    def find_things(self):
        if self.count == 0:
            return
        can_find = []
        lies = []
        all_things_ling = {}
        all_things_can_find = {}
        #new_things = {}
        if 'NONE' in self.lies:
            all_things_ling = {}
        else:
            for thing in self.lies.split(';'):
                id, count, strength = thing.split(':')
                count = int(count)
                strength = int(strength)
                all_things_ling[id] = [count, strength]

        if 'NONE' in self.can_find:
            all_things_can_find = {}
        else:
            for thing in self.can_find.split(';'):
                id, count, strength = thing.split(':')
                count = int(count)
                strength = int(strength)
                all_things_can_find[id] = [count, strength]


        for i in all_things_can_find.keys():
            id, count, strength = i, *all_things_can_find[i]
            if id in all_things_ling:
                all_things_ling[id][0] += count // self.count
                all_things_can_find[i][0] -= count // self.count
            else:
                all_things_ling[id] = [count // self.count, strength]
                all_things_can_find[i][0] -= count // self.count

        for i in all_things_ling.keys():
            lies.append(f'{i}:{all_things_ling[i][0]}:{all_things_ling[i][1]}')
        for i in all_things_can_find.keys():
            can_find.append(f'{i}:{all_things_can_find[i][0]}:{all_things_can_find[i][1]}')

        self.count -= 1
        self.lies = ';'.join(lies)
        self.can_find = ';'.join(can_find)




    def change_parametrs(self, parametrs):
        parametrs = parametrs.split()
        self.id = parametrs[0].split(';')[0]
        self.count = parametrs[0].split(';')[2]
        self.rad = parametrs[0].split(';')[3]
        self.speed = parametrs[0].split(';')[4]
        self.can_find = parametrs[1]
        self.can_attack = parametrs[2]
        self.lies = parametrs[3]

    def get_text_for_save(self):
        text = f'''{self.id};({self.cor[0]},{self.cor[1]});{self.count};{self.rad};{self.speed}
{self.can_find}
{self.can_attack}
{self.lies}</>
'''
        return text

    def draw(self, x, y, font):
        if not self.visibility or x < 0 or y < 0 or x > 1700 or y > 1000:
            return
        pygame.draw.rect(self.canvas, self.color, (x, y, self.size, self.size), 1)
        if self.id != '0':
            text = font.render(self.id, 1, WHITE)
            self.canvas.blit(text, (x + 2, y + 4))


class Board:
    def __init__(self, canvas, width, height, font, cell_size=10, visibility=True, parametrs=None):
        self.canvas = canvas
        self.width = width
        self.height = height
        self.font = font
        self.visibility = visibility
        if parametrs is not None:
            parametrs = parametrs.split('</>')

        self.board = []
        for j in range(height):
            self.board.append([])
            for i in range(width):
                param = None
                if parametrs is not None:
                    index = j * width + i
                    param = parametrs[index]
                self.board[j].append(Call(canvas, i, j, cell_size, parametrs=param))
        self.left = 0
        self.top = 0
        self.cell_size = cell_size

    def set_move(self, left, top):
        self.left = left
        self.top = top

    def change_size_call(self, new_size):
        self.cell_size = new_size
        for i in range(self.height):
            for j in range(self.width):
                self.board[i][j].size = new_size

    def render(self):
        if not self.visibility:
            return
        for i in range(self.height):
            for j in range(self.width):
                x = j * self.cell_size + self.left
                y = i * self.cell_size + self.top
                self.board[i][j].draw(x, y, self.font)

    def made_unvisibility_call(self, x, y, width, height):
        for i in range(self.height):
            for j in range(self.width):
                if (i >= y and i <= y + height and j >= x and j <= x + width):
                    self.board[i][j].visibility = True
                else:
                    self.board[i][j].visibility = False

    def get_cell(self, mouse_pos):
        x, y = mouse_pos
        height = self.height * self.cell_size + self.top
        width = self.width * self.cell_size + self.left
        if (x >= width or y >= height or x < self.left or y < self.top):
            return
        x = int((x - self.left) / self.cell_size)
        y = int((y - self.top) / self.cell_size)
        return x, y

    def get_call_in_bord(self, mouse_pos):
        x, y = mouse_pos
        height = self.height * self.cell_size + self.top
        width = self.width * self.cell_size + self.left
        if (x >= width or y >= height or x < self.left or y < self.top):
            return
        x = int((x - self.left) / self.cell_size)
        y = int((y - self.top) / self.cell_size)
        return self.board[y][x]


class Window(Object):
    def __init__(self, canvas, image, x, y, width, height, column_count):
        self.canvas = canvas
        self.image = image
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.column_count = column_count
        self.visibility = True
        self.paging = False
        self.mod = True
        self.objects = []
        self.shift_y = y
        self.width_object = 70

    def add_object(self, object):
        object.visibility = self.visibility
        if len(self.objects) % self.column_count == 0:
            x = self.x + 5
        else:
            x = self.x + 5 + self.width // self.column_count
        x = (len(self.objects) - ((len(self.objects) // self.column_count) * self.column_count)) * (self.width // self.column_count) + self.x
        y = (len(self.objects) // self.column_count) * self.width_object + self.shift_y
        object.move_to(x, y)
        self.objects.append(object)

    def pag(self, y):
        self.shift_y = y
        if self.mod:   # следующие действия делают так,
            # чтоб объекты не выходили за границы экрана
            if self.shift_y > self.y:
                self.shift_y = self.y
            if ((len(self.objects) // self.column_count) + 1) >= (
                    self.height // self.width_object):

                if self.shift_y < -((((len(self.objects) // self.column_count)) - (
                        self.height // self.width_object))) * self.width_object:

                    self.shift_y = -((((len(self.objects) // self.column_count)) - (
                            self.height // self.width_object))) * self.width_object
            else:
                self.shift_y = self.y

        for i in range(len(self.objects)):
            object = self.objects[i]
            y = (i // self.column_count) * self.width_object + self.shift_y + 5
            object.move_to(object.x, y)

    def render(self):
        self.show()
        if not self.visibility:
            return
        for object in self.objects:
            object.show()


class Player:
    def __init__(self, canvas,  x, y, game_time):
        self.canvas = canvas
        self.width = 50
        self.height = 50
        self.image = get_image_player_on_mao((self.width, self.height))
        self.x = x
        self.y = y
        self.end_x = x
        self.end_y = y
        self.start_x = x
        self.start_y = y
        self.game_time = game_time
        self.deathing = None

        self.start_speed = 100
        self.speed = self.start_speed
        self.path_length = 0
        self.time_for_way = 0
        self.moving = False
        self.timer = time.time()

        self.max_heft = 50000
        self.hunger = 100
        self.water = 100
        self.energy = 100
        self.poison = 0
        self.exhaustion = 0
        self.radiation = 0
        self.temperature = 36.6
        self.bleeding = 0

        self.change_hunger = 3
        self.change_water = 5
        self.change_energy = 2
        self.change_poison = 0
        self.change_exhaustion = 0
        self.change_radiation = 0
        self.change_temperature = 0
        self.change_bleeding = 0

        self.armor = 0
        self.xp_chemistry = 0
        self.xp_survival = 0
        self.xp_mechanics = 0
        self.xp_sewing = 0

        self.effect_radiation = 0
        self.effect_satiety = 0
        self.effect_energy = 0

    def set_inventory(self, inventory):
        self.inventory = inventory


    def set_parametrs(self, parametrs):
        parametrs = parametrs.split('</>')[0].split(';')

        self.exhaustion = int(parametrs[0])
        self.hunger = int(parametrs[1])
        self.water = int(parametrs[2])
        self.poison = int(parametrs[3])
        self.radiation = int(parametrs[4])
        self.energy = int(parametrs[5])
        self.bleeding = int(parametrs[6])
        self.temperature = float(parametrs[7])
        self.max_heft = int(parametrs[8])

        self.armor = int(parametrs[9])
        self.xp_chemistry = int(parametrs[10])
        self.xp_survival = int(parametrs[11])
        self.xp_mechanics = int(parametrs[12])
        self.xp_sewing = int(parametrs[13])
        self.x = int(parametrs[14])
        self.y = int(parametrs[15])

        self.change_exhaustion = float(parametrs[16])
        self.change_hunger = float(parametrs[17])
        self.change_water = float(parametrs[18])
        self.change_poison = float(parametrs[19])
        self.change_radiation = float(parametrs[20])
        self.change_energy = float(parametrs[21])
        self.change_bleeding = float(parametrs[22])
        self.change_temperature = float(parametrs[23])

        self.game_time.num_time = int(parametrs[24])
        self.game_time.update_time()


    def set_cor(self, x, y):
        self.x = x
        self.y = y

    def check_condition(self, call):
        self.change_radiation = float(call.rad)
        self.change_exhaustion = -0.5
        if self.hunger < 0:
            self.hunger = 0
            self.change_exhaustion += 0.6

        if self.water < 0:
            self.water = 0
            self.change_exhaustion += 0.8

        if self.energy < 0:
            self.energy = 100   # сделать так чтоб игрок сразу ложился спать

        if self.poison > 70:
            self.change_exhaustion += 1.5
        elif self.poison > 40:
            self.change_exhaustion += 0.7
        elif self.poison < 0:
            self.poison = 0

        if self.radiation < 0:
            self.radiation = 0
        elif self.radiation > 60:
            self.change_exhaustion += 1
        elif self.radiation > 40:
            self.change_exhaustion += 0.7
        elif self.radiation > 15:
            self.change_exhaustion += 0.4

        if self.temperature > 38:
            self.change_exhaustion += 1
            self.change_temperature += 0.1
        elif self.temperature > 37:
            self.change_exhaustion += 0.5
            self.change_temperature += 0.1
        elif self.temperature < 35:
            self.change_exhaustion += 0.2
            self.change_temperature -= 0.1
        elif self.temperature < 36:
            self.change_exhaustion += 0.1
            self.change_temperature -= 0.05

        if self.bleeding < 0:
            self.bleeding = 0
        elif self.bleeding > 70:
            self.change_exhaustion += 2.5
        elif self.bleeding > 50:
            self.change_exhaustion += 2
        elif self.bleeding > 20:
            self.change_exhaustion += 1
        if self.bleeding > 0:
            self.change_exhaustion += 0.1
            self.change_bleeding -= 0.2

        if self.exhaustion > 100:
            self.deathing()
        if self.exhaustion < 0:
            self.exhaustion = 0
        if self.exhaustion > 40:
            self.change_exhaustion -= 0.3


    def change_all_parametrs(self, delte_t):
        self.hunger -= self.change_hunger * delte_t
        self.water -= self.change_water * delte_t
        self.energy -= self.change_energy * delte_t
        self.poison += self.change_poison * delte_t
        self.exhaustion += self.change_exhaustion * delte_t
        self.radiation += self.change_radiation * delte_t
        self.temperature -= self.change_temperature * delte_t
        self.bleeding += self.change_bleeding * delte_t


    def move_to(self, x, y):
        if self.inventory.heft > self.max_heft:
            return
        self.end_x = int(x)
        self.end_y = int(y)
        self.start_x = self.x
        self.start_y = self.y
        self.path_length = ((self.x - x) ** 2 + (self.y - y) ** 2) ** 0.5
        self.length_x = abs(x - self.start_x)
        self.length_y = abs(y - self.start_y)

        self.passed_x = 0
        self.passed_y = 0

        #   self.time_for_way = self.path_length / self.speed
        self.game_time.start_thinktime()
        self.moving = True

    def stop(self):
        self.moving = False
        self.x = int(self.x)
        self.y = int(self.y)
        self.end_x = self.x
        self.end_y = self.y
        self.start_x = self.x
        self.start_y = self.y

    def made_step(self):
        delte_t = self.game_time.change_game_time() / 3600
        shift_x = (self.end_x - self.start_x) * (delte_t / (self.path_length / self.speed))
        shift_y = (self.end_y - self.start_y) * (delte_t / (self.path_length / self.speed))

        self.length_x -= abs(shift_x)
        self.length_y -= abs(shift_y)
        self.passed_x += shift_x
        self.passed_y += shift_y
        self.change_all_parametrs(delte_t)

        if self.length_x < 0 or self.length_y < 0:
            self.x = self.end_x
            self.y = self.end_y
            self.moving = False
            return

        self.x = self.start_x + self.passed_x
        self.y = self.start_y + self.passed_y

    def show(self, map_x_on_main_map=0, map_y_on_main_map=0, map_x=0, map_y=0, zoom=1):
        self.canvas.blit(self.image, ((self.x - map_x_on_main_map) * zoom + map_x - self.width // 2,
                                      (self.y - map_y_on_main_map) * zoom + map_y - self.height // 2))


class Thing(Button):
    def __init__(self, canvas, id, con, count, strength, font=None):
        self.canvas = canvas
        self.count = count
        self.font = font
        self.x = 0
        self.y = 0
        self.visibility = True

        cur = con.cursor()
        query = f'''SELECT * FROM things
            WHERE id = {id}'''
        result = cur.execute(query).fetchone()

        self.id = int(result[0])
        self.name = result[1]
        self.heft = int(result[2])
        self.type = int(result[3])
        self.start_strength = int(result[4])
        self.strength = int(strength)
        self.effect_hunger = int(result[5])
        self.effect_water = int(result[6])
        self.effect_energy = int(result[7])
        self.effect_poison = int(result[8])
        self.effect_bleeding = int(result[9])
        self.effect_exhaustion = int(result[10])
        self.effect_radiation = int(result[11])
        self.damage = int(result[12])
        self.armor = int(result[13])
        self.effect_satiety_ps = int(result[14])
        self.effect_energy_ps = int(result[15])
        self.effect_radiation_ps = int(result[16])
        self.effect_light = int(result[17])
        self.expenses = result[18]
        w = ps_width(8.9)
        h = w
        self.image = get_free_image(result[19], (w, h))
        self.width = w
        self.height = h

        self.functions = []

    def get_text_for_saving(self):
        return f'{self.id};{self.count};{self.strength}'



    def show(self):
        pygame.draw.rect(self.canvas, BROWN, (self.x, self.y, self.width, self.height), ps_height(0.6))

        self.canvas.blit(self.image, (self.x, self.y))
        if self.font is not None:
            text = self.font.render(str(self.count), 1, BLACK)
            self.canvas.blit(text, (self.x + self.width - ps_width(4),
                                    self.y + self.height - ps_height(4)))


class Inventory:
    def __init__(self, canvas, bg_image, player, parametrs=None, mod=1):
        self.canvas = canvas
        self.bg_image = bg_image
        self.con = sqlite3.connect("item_base.db")
        self.heft = 0
        self.player = player
        if mod == 1:
            player.set_inventory(self)

        self.visibility = False
        separator = ';'
        if parametrs is None:
            all_thinks = []
        elif mod == 1:
            all_thinks = parametrs.split('</>')[1].split(', ')
            x = all_thinks[0].split()
            if all_thinks == ['\n']:
                all_thinks = []
        else:
            if 'NONE' in parametrs.split('\n')[3]:
                all_thinks = []
            else:
                all_thinks = parametrs.split('\n')[3].split(';')
                separator = ':'


        self.all_thinks = self.convert_thinks_to_object(all_thinks, separator)
        self.showing_thinks = self.all_thinks

        x = ps_width(2)
        y = ps_height(28.51)
        w = ps_width(44.1)
        h = ps_height(56.8)

        image = get_bg_for_thinks_in_inventory((w, h))
        self.window = Window(canvas, image, x + 2, y, w, h, 5)
        self.window.visibility = True
        self.window.width_object = ps_width(8.9)
        for think in self.showing_thinks:
            self.window.add_object(think)

    def convert_thinks_to_object(self, all_thinks, sep=';'):
        ready_thinks = []
        font = pygame.font.Font(None, ps_height(5))
        self.heft = 0
        for think in all_thinks:
            id, count, strength = think.split(sep)
            if sep == ':':
                strength = strength.split('</>')[0]
            think = Thing(self.canvas, id, self.con, count, strength, font)
            self.heft += think.heft * int(count)

            ready_thinks.append(think)
        return ready_thinks

    def update_thinks(self, all_thinks):
        self.all_thinks = all_thinks
        self.showing_thinks = all_thinks
        self.window.objects = []
        for think in self.showing_thinks:
            self.window.add_object(think)

    def append_think(self, think):
        self.heft += think.heft * int(think.count)
        self.all_thinks.append(think)

    def get_text_for_saving(self):
        all_thinks = list(map(lambda x: x.get_text_for_saving(), self.all_thinks))
        all_thinks = ', '.join(all_thinks)
        text = all_thinks + '</>'
        return text

    def get_ps_of_load(self):
        ps =  int(100 * self.heft / self.player.max_heft)
        if ps > 999:
            ps = 999
        return ps

    def show(self):
        if self.visibility:
            self.window.render()
            self.canvas.blit(self.bg_image, (0, ps_height(5.6)))


class GameTime:
    def __init__(self, t, canvas):
        self.num_time = t
        self.canvas = canvas
        self.time = time.localtime(t)
        self.timer = 0
        self.real_timer = time.time()
        self.font = pygame.font.Font(None, ps_width(2))

    def start_thinktime(self):
        self.timer = time.time()

    def update_time(self):
        self.time = time.localtime(self.num_time)

    def change_game_time(self):
        delte_t = time.time() - self.timer
        self.num_time += delte_t * 3600
        self.time = time.localtime(self.num_time)
        self.timer = time.time()
        return delte_t * 3600

    def update_time_on_real_time(self):
        delte_t = time.time() - self.real_timer
        self.num_time += delte_t
        self.time = time.localtime(self.num_time)
        self.real_timer = time.time()
        return delte_t

    def get_string_of_time(self):
        hour = str(self.time.tm_hour).rjust(2, '0')
        min = str(self.time.tm_min).rjust(2, '0')
        sec = str(self.time.tm_sec).rjust(2, '0')
        string = f'''{self.time.tm_mday}.{self.time.tm_mon}.{self.time.tm_year
        } {hour}:{min}:{sec}'''
        return string

    def show(self):
        text = self.font.render(self.get_string_of_time(), 1, LIGHT_GREEN)
        self.canvas.blit(text, (ps_width(44), ps_height(91)))


