# 将位图存在在屏幕最中间，底色设置成一致的
import pygame
import sys


class ScreenShow:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((200, 180))
        pygame.display.set_caption("背景图")
        self.bg_color = (255, 255, 255)
        self.bitmap = BitMap(self)

    def close_window(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                pygame.display.flip()
                self.screen.fill(self.bg_color)
                self.bitmap.bitme()


class BitMap:
    def __init__(self, bit_game):
        self.screen = bit_game.screen
        self.screen_rect = bit_game.screen.get_rect()

        self.image = pygame.image.load('ship.bmp')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

    def bitme(self):
        self.screen.blit(self.image, self.rect)


show = ScreenShow()
show.close_window()
