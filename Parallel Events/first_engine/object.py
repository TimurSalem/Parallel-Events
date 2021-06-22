"""
Модуль для создания объектов типа:
Character - класс для создания персонажей
Barrier - класс для создания непроходимых препятствий
"""
from first_engine.game import *

import pygame
import os


class Object:
    """
    Основной класс на основе которого строятся другие классы, представляющие разные типы объектов
    Содержит в себе основные методы для управление всеми объектами
    :var sprites: Dict - сохраняет спрайты созданного на его основе объекта
    :var last_action: str - информация о последнем действии объекта
    :var time_to_sprite_update: int - вряме до смены спрайта, если предполагается анимация
    :var sprite_id: int - индекс спрайта
    """
    sprites = {}

    time_to_sprite_update = 6
    sprite_id = 0

    action = None
    actions = {}

    drop_speed = 1

    def __init__(self, parent: pygame.Surface, width=40, height=40, x=0, y=0, color: tuple = (255, 255, 255)):
        """
        Метод для построения объекта
        :param parent: pygame.Surface - родимтельское окно
        :param width: int
        :param height: int
        :param x: int
        :param y: int
        :param color: tuple - цвет в RGB
        :var skin: pygame.Surface - скин объекта - по умолчанию
        :var body: Rect - тело объекта - по умолчанию
        """
        self.parent = parent
        self.x, self.y = x, y
        self.color = color
        self.width = width
        self.height = height

        self.skin = pygame.Surface(size=(width, height))
        self.skin.fill(color=color)
        self.body = self.skin.get_rect(topleft=(x, y))

    def resize(self, x, y):
        self.width = x
        self.height = y
        self.skin = pygame.Surface(size=(self.width, self.height))
        self.skin.fill(color=self.color)
        self.body = self.skin.get_rect(topleft=(self.x, self.y))






    def blit(self):
        """
        Метод для отображения объекта
        :return: pygame.Surface
        """
        self.parent.blit(source=self.skin, dest=self.body)
        return self.parent

    def recolor(self, color):
        """
        Метод для сметы цвета
        :return: RGB
        """
        self.skin.fill(color=color)
        return color

    def drop(self, speed_up=1, max_speed=15):
        """
        Падение персонажа
        :return: int положение тела
        """
        self.body.y += self.drop_speed
        if self.drop_speed < max_speed:
            self.drop_speed += speed_up
        return self.drop_speed

    def load_sprites(self, name: str, path: str, update: int = 6):
        """
        Метод для загрузки спрайтов в sprites
        :param update: частота обновления спрайта
        :param name: str - имя под которым будем хранить загруженные скины и созданные тела, необходимые именя:
        run_left, run_right, stand_left, stand_right, jump_left, jum_right, attack_left, attack_right
        :param path: str - путь до папки с файлами
        :return skins: dict - возвращаем только что загруженные скины и созданные тела
        """
        skins = [pygame.image.load(path + i) for i in os.listdir(path)]

        self.sprites[name] = {'skins': skins, 'update': update}
        return skins

    def __sprite_update(self, name):
        """
        Метод обновляющий спрайты по очереди
        :param name: str - принимает имя спрайтов сохраненных в словаре sprites
        :return: int - возвращает id текущего спрайта
        """
        self.time_to_sprite_update -= 1
        if self.time_to_sprite_update == 0:
            self.sprite_id += 1
            self.time_to_sprite_update = self.sprites[name]['update']
            if self.sprite_id == len(self.sprites[name]['skins']):
                self.sprite_id = 0
        return self.sprite_id

    def __remake_for_skin(self, name: str):
        """
        Метод для переделывания скина и тела по индексу скина и его названия в sprites
        :param name: str название скинов
        :return: pygame.Surface
        """
        self.skin = self.sprites[name]['skins'][self.sprite_id]
        self.body = self.skin.get_rect(topleft=(self.body.x, self.body.y))
        return self.skin

    def play_animation(self, action):
        print(self.actions)
        self.__sprite_update(action)
        self.__remake_for_skin(action)

class Character(Object):
    """
    Класс для создания персонажей
    """

    def __init__(self, parent: pygame.Surface, width=40, height=40, x=0, y=0, color=(255, 255, 255),
                 speed=1, height_jump=20, sprite=None, health=230):
        """
        :param parent: pygame.Surface - родимтельское окно
        :param width: int
        :param height: int
        :param x: int
        :param y: int
        :param color: tuple - цвет в RGB
        :param speed: int - скорость персонажа
        """
        super().__init__(parent, width, height, x, y, color)
        self.speed = speed
        self.height_jump = height_jump
        self.sprite = sprite
        self.health = health

        self.action = 'stand_right'

    def sprite_blit(self):
        sp = self.sprite
        self.skin = pygame.image.load(sp)

    def __motions(self):
        left = pygame.key.get_pressed()[97]
        right = pygame.key.get_pressed()[100]
        up = pygame.key.get_pressed()[119]
        down = pygame.key.get_pressed()[115]
        jump = pygame.key.get_pressed()[32]

        stand = not(left + right + up + down + jump)
        if stand and 'left' in self.action:
            self.action = 'stand_left'
        elif stand and 'right' in self.action:
            self.action = 'stand_right'

        self.actions = {'left': left, 'right': right, 'up': up, 'down': down, 'jump': jump, 'default': stand}

        return self.actions

    def motion_left(self):
        """
        Метод для движения влево, можно подключить загруженные спрайты
        :return: int - скорость
        """
        left = self.__motions()['left']
        if left:
            self.body.x -= left * self.speed
            self.action = 'run_left'
        return left

    def motion_right(self):
        """
        Метод для движения вправо, можно подключить загруженные спрайты
        :return: int - скорость
        """
        right = self.__motions()['right']
        if right:
            self.body.x += right * self.speed
            self.action = 'run_right'
        return right

    def motion_up(self):
        """
        Метод для движения вверх, можно подключить загруженные спрайты
        :return: int - скорость
        """
        up = self.__motions()['up']
        if up:
            self.body.y -= up * self.speed
        return up

    def motion_down(self):
        """
        Метод для движения вниз, можно подключить загруженные спрайты
        :return: int - скорость
        """
        down = self.__motions()['down']
        if down:
            self.body.y += down * self.speed
        return down

    def action_jump(self):
        if self.y == self.body.y and self.drop_speed != 1:
            self.drop_speed = 1
            if self.__motions()['jump']:
                self.drop_speed = -self.height_jump
        # else:
        #      print(True)
        self.y = self.body.y


class Barrier(Object):
    """
    Класс для создания непроходимых объектов
    """

    def __init__(self, parent: pygame.Surface, objects: list, width=40, height=40, x=0, y=0, color=(255, 255, 255),
                 speed_x=0, speed_y=0, health=230):
        """
        :param parent: pygame.Surface - родимтельское окно
        :param objects:
        :param width: int
        :param height: int
        :param x: int
        :param y: int
        :param color: tuple - цвет в RGB
        """
        super().__init__(parent, width, height, x, y, color)
        self.objects = objects
        self.speed_x = speed_x
        self.speed_y = speed_y

    def motions_bullet_right(self):
        self.body.x += self.speed_x
        # if self.speed_y > 12:
        #     self.speed_y = 12
        # if self.speed_y < -12:
        #     self.speed_y = -12
        self.body.y -= self.speed_y

    def motions_bullet_left(self):
        self.body.x -= self.speed_x
        # if self.speed_y > 12:
        #     self.speed_y = 12
        # if self.speed_y < -12:
        #     self.speed_y = -12
        self.body.y += self.speed_y

    def resistance(self):
        """
        Метод, который отвечает за препятствывание передвижения
        :return: boolean - есть сопротивление или нету
        """
        for obj in self.objects:
            collision = self.body.colliderect(obj.body)
            if collision:
                resist_sides = {
                    'left': abs(self.body.left - obj.body.right),
                    'right': abs(self.body.right - obj.body.left),
                    'top': abs(self.body.top - obj.body.bottom),
                    'bottom': abs(self.body.bottom - obj.body.top)
                }
                min_dip = [key for key, val in resist_sides.items() if val == min(resist_sides.values())]

                if 'left' in min_dip:
                    obj.body.right = self.body.left
                elif 'right' in min_dip:
                    obj.body.left = self.body.right
                elif 'top' in min_dip:
                    obj.body.bottom = self.body.top
                elif 'bottom' in min_dip:
                    obj.body.top = self.body.bottom
                return collision

class Bullet(Object):
    """
    Класс для создания непроходимых объектов
    """

    def __init__(self, parent: pygame.Surface, objects: list, width=40, height=40, x=0, y=0, color=(255, 255, 255), speed_x=0, speed_y=0, sprite=None):
        """
        :param parent: pygame.Surface - родимтельское окно
        :param objects:
        :param width: int
        :param height: int
        :param x: int
        :param y: int
        :param color: tuple - цвет в RGB
        """
        super().__init__(parent, width, height, x, y, color)
        self.objects = objects
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.sprite = sprite

    def motions_bullet(self):
        self.body.x += self.speed_x
        self.body.y -= self.speed_y

    def sprite_blit(self):
        sp = self.sprite
        self.skin = pygame.image.load(sp)

    def resistance(self):
        """
        Метод, который отвечает за препятствывание передвижения
        :return: boolean - есть сопротивление или нету
        """
        for obj in self.objects:
            collision = self.body.colliderect(obj.body)
            if collision:
                resist_sides = {
                    'left': abs(self.body.left - obj.body.right),
                    'right': abs(self.body.right - obj.body.left),
                    'top': abs(self.body.top - obj.body.bottom),
                    'bottom': abs(self.body.bottom - obj.body.top)
                }
                min_dip = [key for key, val in resist_sides.items() if val == min(resist_sides.values())]

                if 'left' in min_dip:
                    obj.body.right = self.body.left
                elif 'right' in min_dip:
                    obj.body.left = self.body.right
                elif 'top' in min_dip:
                    obj.body.bottom = self.body.top
                elif 'bottom' in min_dip:
                    obj.body.top = self.body.bottom
                return collision

# class Bullet(Object):
#     def __init__(self, parent: pygame.Surface, x, y, width=40, height=40, color=(255, 255, 255)):
#         self.x = x
#         self.y = y
#         self.speed_x = 4
#         self.speed_y = 0
#         self.dest_x = 0
#         self.dest_y = 0
#         self.parent = parent
#         self.width = width
#         self.color = color
#
#         self.skin = pygame.Surface(size=(width, height))
#         self.skin.fill(color=color)
#         self.body = self.skin.get_rect(topleft=(x, y))
#
#     def path_finder(self, dest_x, dest_y):
#         self.dest_x = dest_x
#         self.dest_y = dest_y
#
#         delta_x = dest_x - self.x
#         count_up = delta_x // self.speed_x
#         delta_y = self.y - dest_y
#         self.speed_y = delta_y / count_up
#
#     def move_to(self):
#         self.x += self.speed_x
#         self.y -= self.speed_y
#
#         # if self.x <= self.dest_x and self.y >= self.dest_y:
#         #     pygame.Surface.blit()
#
#
#
#
#
#
#
