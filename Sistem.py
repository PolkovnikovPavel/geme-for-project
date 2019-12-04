import pygame
import time
from game.images.images import *


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 0, 255)


def change_parametrs(id):
    if id[0] == 0:
        parametrs = '''0;(x,y);0;0;1
            NONE
            NONE
            NONE'''
    elif id[0] == 1:
        parametrs = '''1;(x,y);1000;0;0.02
            1:10000
            NONE
            NONE'''
    elif id[0] == 2:
        parametrs = '''2;(x,y);0;0;1
            2:75
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
            self.count = '0'
            self.rad = '0'
            self.speed = 1
            self.can_find = 'NONE'
            self.can_attack = 'NONE'
            self.lies = 'NONE'
        else:
            parametrs = parametrs.split()
            self.id = parametrs[0].split(';')[0]
            self.cor = (x, y)
            self.count = parametrs[0].split(';')[2]
            self.rad = parametrs[0].split(';')[3]
            self.speed = parametrs[0].split(';')[4]
            self.can_find = parametrs[1]
            self.can_attack = parametrs[2]
            self.lies = parametrs[3]

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
        self.objects = []
        self.shift_y = 0
        self.width_object = 70

    def add_object(self, object):
        object.visibility = self.visibility
        if len(self.objects) % self.column_count == 0:
            x = self.x + 5
        else:
            x = self.x + 5 + self.width // self.column_count
        x = (len(self.objects) - ((len(self.objects) // self.column_count) * self.column_count)) * (self.width // self.column_count) + self.x + 5
        y = (len(self.objects) // self.column_count) * self.width_object + self.shift_y + 5
        object.move_to(x, y)
        self.objects.append(object)

    def pag(self, y):
        self.shift_y = y
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
    def __init__(self, canvas,  x, y):
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
        self.inventory = []
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
        self.armor = 0
        self.xp_chemistry = 0
        self.xp_survival = 0
        self.xp_mechanics = 0
        self.xp_sewing = 0



        self.effect_radiation = 0
        self.effect_satiety = 0
        self.effect_energy = 0

    def set_cor(self, x, y):
        self.x = x
        self.y = y

    def move_to(self, x, y):
        self.end_x = int(x)
        self.end_y = int(y)
        self.start_x = self.x
        self.start_y = self.y
        self.path_length = ((self.x - x) ** 2 + (self.y - y) ** 2) ** 0.5
        self.length_x = abs(x - self.start_x)
        self.length_y = abs(y - self.start_y)

        self.passed_x = 0
        self.passed_y = 0

        self.time_for_way = self.path_length / self.speed
        self.timer = time.time()
        self.moving = True

    def made_step(self):
        delte_t = ((time.time() - self.timer))
        self.timer = time.time()
        shift_x = (self.end_x - self.start_x) * (delte_t / (self.path_length / self.speed))
        shift_y = (self.end_y - self.start_y) * (delte_t / (self.path_length / self.speed))

        self.length_x -= abs(shift_x)
        self.length_y -= abs(shift_y)
        self.passed_x += shift_x
        self.passed_y += shift_y

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



