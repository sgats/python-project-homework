import pygame
from pygame.sprite import Sprite


class Rain(Sprite):
    def __init__(self, rain_game):
        """设置雨滴的初始位置"""
        super().__init__()
        self.screen = rain_game.screen
        # self.screen_rect = rain_game.screen.get_rect()
        """加载雨滴图像并设置其矩阵位置"""
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        """每个雨滴都放在最上角"""
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # self.rect.topleft = self.screen_rect.topleft

        self.x = float(self.rect.x)
        self.settings = rain_game.settings

    def check_edges(self):
        """如果雨滴位于屏幕边缘，就返回True"""
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)

    def update(self):
        """向左或向右移动雨滴"""
        self.x += self.settings.rain_speed * self.settings.fleet_direction
        self.rect.x = self.x

