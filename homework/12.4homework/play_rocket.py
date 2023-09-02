# 编写一个火箭，让它放在屏幕中间，可以上下左右移动，但不能超过边框
import pygame
import sys
from rocket import Rocket
from settings import Settings


# 设置屏幕尺寸，并展示出来


class PlayRocket:
    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()
        self.settings = Settings()
        """设置屏幕尺寸"""
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        """设置屏幕的标题"""
        pygame.display.set_caption("火箭运动")
        """设置游戏帧率"""
        self.clock = pygame.time.Clock()
        """设置游戏背景色"""
        self.bg_color = self.settings.bg_color
        """初始化火箭"""
        self.rocket = Rocket(self)

    def run_rocket(self):
        """开始火箭的主循环"""
        while True:
            self._check_event()
            self._update_screen()
            self.clock.tick(60)
            self.rocket.update()

    def _check_event(self):
        """监听键盘和鼠标事件"""
        for event in pygame.event.get():
            """如果事件类型是退出，则退出游戏"""
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    """向左移动火箭"""
                    self.rocket.moving_left = True
                elif event.key == pygame.K_RIGHT:
                    """向右移动火箭"""
                    self.rocket.moving_right = True
                elif event.key == pygame.K_UP:
                    """向上移动火箭"""
                    self.rocket.moving_up = True
                elif event.key == pygame.K_DOWN:
                    self.rocket.moving_down = True
            elif event.type == pygame.KEYUP:
                """释放按键"""
                self.rocket.moving_left = False
                self.rocket.moving_right = False
                self.rocket.moving_up = False
                self.rocket.moving_down = False

    def _update_screen(self):
        """改变背景色"""
        self.screen.fill(self.bg_color)
        """添加火箭"""
        self.rocket.bitme()
        """让最近绘制的屏幕可见"""
        pygame.display.flip()


"""如果类是直接运行的，则运行下面的代码，如果类是被调用的，则不运行下面的代码块"""
if __name__ == '__main__':
    rocket = PlayRocket()
    rocket.run_rocket()

# 加载火箭图片  计算火箭图片在屏幕中的位置


# 移动的时候判断边缘位置
