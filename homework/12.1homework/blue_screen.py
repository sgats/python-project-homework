# 创建一个蓝色背景的窗口
import sys
import pygame


class ShowWindows:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((200, 150))
        self.bg_color = (0, 0, 255)
        pygame.display.set_caption("显示屏幕")

    def showit(self):
        while True:
            """监听游戏窗口的类型，如果点击关闭，退出游戏窗口"""
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.bg_color)
            pygame.display.flip()


show = ShowWindows()
show.showit()
