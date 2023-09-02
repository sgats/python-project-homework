import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """管理飞船说发射子弹的类"""
    def __init__(self, bullet_game):
        """在飞船的当前创建一个子弹对象"""
        super().__init__()
        self.screen = bullet_game.screen
        self.settings = bullet_game.settings
        self.color = self.settings.bullet_color

        """在0 0 处创建一个表示子弹的矩形，再设置正确的位置"""
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midleft = bullet_game.ship.rect.midleft
        """存储用浮点数表示的子弹位置"""
        self.x = float(self.rect.x)

    def update(self):
        """向右移动子弹"""
        self.x += self.settings.bullet_speed
        self.rect.x = self.x

    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)

