import pygame
from settings import Settings

"""添加飞船图像"""


class Ship:
    def __init__(self, bullet_game):
        """初始化飞船位置"""
        self.screen = bullet_game.screen
        self.settings = bullet_game.settings
        self.screen_rect = bullet_game.screen.get_rect()
        """加载飞船图像并获取其外接矩阵"""
        self.image = pygame.image.load('./ship.bmp')
        self.rect = self.image.get_rect()
        """每艘新飞船都放在屏幕的左屏幕中间位置"""
        self.rect.midleft = self.screen_rect.midleft
        """在飞船的属性y中存储一个浮点数"""
        self.y = float(self.rect.y)
        """增加飞船移动标志"""
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """根据移动标志调整飞船位置"""
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed
        self.rect.y = self.y

    def bitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
