"""专门存放火箭图片，以及设置火箭位置的信息"""
import pygame


class Rocket:
    def __init__(self, ro_game):
        self.settings = ro_game.settings
        """初始化火箭并设置其初始位置"""
        self.screen = ro_game.screen
        self.screen_rect = ro_game.screen.get_rect()
        """加载图片，并且获取图片的外接矩阵"""
        self.image = pygame.image.load('image/ship.bmp')
        self.rect = self.image.get_rect()
        """每个火箭都放在屏幕的正中间"""
        self.rect.center = self.screen_rect.center
        """横坐标移动"""
        self.x = float(self.rect.x)
        """纵坐标移动"""
        self.y = float(self.rect.y)
        """火箭开始不运动"""
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False

    def bitme(self):
        """在指定位置绘制火箭"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """根据移动标志调整火箭的位置"""
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.rocket_speed
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.rocket_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.rocket_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.rocket_speed
        self.rect.x = self.x
        self.rect.y = self.y
