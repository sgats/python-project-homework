"""让星星在页面上显示一行"""
import pygame
import sys
from settings import Settings
from star import Star
from random import randint


class ShowStar:
    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("乱序小星星")
        self.bg_color = self.settings.bg_color
        self.starts = pygame.sprite.Group()
        self._create_star_fleet()

    def _create_star_fleet(self):
        """创建星星舰队"""
        star = Star(self)
        self.starts.add(star)
        """创建一个星星，再不断添加，直到没有空间添加星星为止，星星的间距为星星的宽度"""
        star_width = star.rect.width
        current_x = star_width
        while current_x < (self.settings.screen_width - 2 * star_width):
            random_number = randint(180, 900)
            new_star = Star(self)
            # new_star.x = current_x
            new_star.x = random_number
            new_star.rect.x = random_number
            # new_star.rect.x = current_x
            self.starts.add(new_star)
            current_x += 2 * star_width
            print(random_number, current_x)

    def run_game(self):
        """开始游戏主循环"""
        while True:
            """侦听键盘和鼠标事件"""
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.settings.bg_color)

            self.starts.draw(self.screen)

            """让最新绘制的屏幕可见"""
            pygame.display.flip()


if __name__ == '__main__':
    show = ShowStar()
    show.run_game()
