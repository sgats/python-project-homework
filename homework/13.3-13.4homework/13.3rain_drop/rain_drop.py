import pygame
import sys
from settings import Settings
from rain import Rain
"""雨滴往下落"""


class RainDrop:
    def __init__(self):
        """定义一个雨滴掉落的类"""
        self.settings = Settings()
        pygame.init()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("雨滴下落")
        self.clock = pygame.time.Clock()
        # self.rain = Rain(self)
        self.rains = pygame.sprite.Group()
        self._create_fleet()

    def _create_fleet(self):
        """创建一个雨滴舰队"""
        """不断添加外星人，直到没有空间添加外星人为止"""
        raining = Rain(self)
        # raining_width = raining.rect.width
        """雨滴的间距为雨滴的宽度和雨滴的搞定"""
        raining_width, raining_height = raining.rect.size

        current_x, current_y = raining_width, raining_height
        while current_y < (self.settings.screen_height - 3 * raining_height):
            while current_x < (self.settings.screen_width - 2 * raining_width):
                self._create_rain(current_x, current_y)
                current_x += 2 * raining_width
            """添加一行外星人后， 重置x值并递增y值"""
            current_x = raining_width
            current_y += 2 * raining_height

    def _create_rain(self, x_position, y_position):
        """创建一个雨滴并放在当前行中"""
        new_rain = Rain(self)
        new_rain.x = x_position
        new_rain.rect.x = x_position
        new_rain.rect.y = y_position
        self.rains.add(new_rain)

    def _update_rains(self):
        """更新雨滴舰队中所有雨滴的位置"""
        """检查是否有雨滴位于屏幕边缘，并更新整个雨滴舰队的位置"""
        self._check_fleet_edges()
        self.rains.update()

    def run_game(self):
        """开始游戏主循环"""
        while True:
            self._check_events()
            self._update_rains()
            self._update_screen()
            self.clock.tick(60)
            """但雨滴到达屏幕底部的下边缘后，删除已经消失的雨滴"""
            for raining in self.rains.copy():
                print("打印雨滴边距", raining.rect)
                if raining.rect.top >= self.screen.get_height():
                    self.rains.remove(raining)
                print("查看雨滴是否有变少", len(self.rains))

    @staticmethod
    def _check_events():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        """每次循环时绘制背景颜色"""
        self.screen.fill(self.settings.bg_color)
        # self.rain.bitme()
        self.rains.draw(self.screen)
        """让最近绘制的屏幕可见"""
        pygame.display.flip()

    def _check_fleet_edges(self):
        """在有雨滴到达边缘时采取响应的措施"""
        for raining in self.rains.sprites():
            if raining.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """改变雨滴舰队的位置,将整个雨滴舰队向下移动，并改变他们的方向"""
        for raining in self.rains.sprites():
            raining.rect.y += self.settings.fleep_drop_speed
        self.settings.fleet_direction *= -1


if __name__ == "__main__":
    rain = RainDrop()
    rain.run_game()

