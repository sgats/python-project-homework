import pygame
from pygame.sprite import Sprite


class Star(Sprite):
    def __init__(self, star_game):
        super().__init__()
        """初始化星星并设置其rect位置"""
        self.screen = star_game.screen
        # 加载星星图片，并设置其外接矩阵
        self.image = pygame.image.load('image/star.bmp')
        self.rect = self.image.get_rect()
        """每个星星最初都在屏幕的左上角附近"""
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        """存储星星的精确水平位置"""
        self.x = float(self.rect.x)
