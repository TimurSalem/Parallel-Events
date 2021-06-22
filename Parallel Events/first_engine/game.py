"""
Модуль с основным классом-конструктором Game - для создания игры.
"""
import pygame


class Game:
    """
    Класс-конструктор, содержит основные методы и переменные для написания игр
    """
    RUNNER = True
    __clock = pygame.time.Clock()  # счетчик FPS

    def __init__(self, width: int = 400, height: int = 300, color: tuple = (0, 0, 0)):
        """
        :param width: высота окна
        :param height: ширина окна
        """
        self.color = color

        self.surface = pygame.display.set_mode(
            size=(width, height)
        )  # родительское окно
        self.surface.fill(color)
        self.body = self.surface.get_rect()

    @staticmethod
    def display_update() -> None:
        """
        Метод для обновления окна
        :return None:
        """
        pygame.display.update()

    def set_capture(self, capture):
        """
        Метод для переименовки окна
        :return None:
        """
        pygame.display.set_caption(capture)

    def set_icon(self, path):
        """
        Метод для переименовки окна
        :return None:
        """
        icon = pygame.image.load(path)

        pygame.display.set_icon(icon)

    @staticmethod
    def events() -> list:
        """
        Метод содержащий отслеживантель событий
        :return list: возвращает список событий
        """
        return pygame.event.get()

    def window_fill(self) -> pygame.Rect:
        """
        Метод при вызове которого заливается родительское окно
        :return None:
        """
        return self.surface.fill(self.color)  # заливаем родительское окно

    def fps_counter(self, FPS: int = 30) -> int:
        """
        Метод управляущий частотой обновления кадров
        :param FPS: число кадров в секунду
        :return None:
        """
        return self.__clock.tick(FPS)

    def close(self, event: {type, pygame.key}) -> None:
        """
        Метод для закрытия окна
        :param event: событие для закрытия окна
        :return None:
        """
        if event.type == 256 or (event.type == 768 and event.key == 27):  # если нажал крестик или ESC
            pygame.quit()  # деинициализируем pygame
            self.RUNNER = False  # отключаем цикл

    def window_borders(self, objects: list):
        """
        Метод для ограничения передвижения объектов в паределах экрана
        :param objects: список объектов, которые будет ограничены экраном
        :return sides: dict
        """
        for obj in objects:
            if obj.body.left < self.body.left:
                obj.body.left = self.body.left
            elif obj.body.right > self.body.right:
                obj.body.right = self.body.right

            if obj.body.top < self.body.top:
                obj.body.top = self.body.top
            elif obj.body.bottom > self.body.bottom:
                obj.body.bottom = self.body.bottom

    def cycle_init(self, objects: list = None, FPS: int = 60) -> None:
        """
        Метод для инициализации игрового цикла. Вместо того, что бы запусткать каждый метод по отдельности и думать о
        правильной последовательности методов, можно просто запустить этот метод.
        Содержит в себе все страндартные методы в правильной последовательности для запуска цикла: счетчик FPS, можно
        добавить объекты, которые нужно ограничить в пределах экрана, содержит в себе метод обновления окна и заливка
        окна.
        :param objects: список объектов, которые будет ограничены экраном
        :param FPS: число кадров в секунду
        :return None:
        """
        self.fps_counter(FPS)
        if objects:
            self.window_borders(objects=objects)
        self.display_update()
        self.window_fill()
