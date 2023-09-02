import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien


class AlienInvasion:
    """管理游戏资源和行为的类"""

    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()
        """定义一个时钟，用来控制帧率"""
        self.clock = pygame.time.Clock()

        self.settings = Settings()

        """设置屏幕尺寸"""
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        """设置标题信息"""
        pygame.display.set_caption("打外星人游戏")
        self.ship = Ship(self)
        """创建存储子弹的编组"""
        self.bullets = pygame.sprite.Group()
        """创建存储外星人的编组"""
        self.aliens = pygame.sprite.Group()
        """调用外星舰队"""
        self._create_fleet()

    def run_game(self):
        """开始游戏的主循环"""
        while True:
            # 侦听键盘和鼠标事件
            self._check_events(self)
            # 调用飞船移动的方法
            self.ship.update()
            self._update_bullets()
            # 每次循环的时候都重绘屏幕
            self._update_screen()
            self.clock.tick(60)

    @staticmethod
    def _check_events(self):
        """重构：相应按键和鼠标事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            # 当玩家释放按键时
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """响应按下"""
        # 响应鼠标按键事件
        if event.key == pygame.K_RIGHT:
            # 向右移动飞船
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            # 向左移动飞船
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            """发射子弹"""
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """响应释放"""
        self.ship.moving_right = False
        self.ship.moving_left = False

    def _fire_bullet(self):
        """创建一颗子弹，并将其加入编组bullets"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _create_fleet(self):
        """创建一个外星舰队"""
        # 创建一个外星人
        alien = Alien(self)
        self.aliens.add(alien)
        """创建一个外星人，再不断添加，直到没有空间添加外星人，外星人的间距为外星人的宽度"""
        alien_width = alien.rect.width

        current_x = alien_width
        while current_x < (self.settings.screen_width - 2* alien_width):
            new_alien = Alien(self)
            new_alien.x = current_x
            new_alien.rect.x = current_x
            self.aliens.add(new_alien)
            current_x += 2 * alien_width

    def _update_bullets(self):
        """更新子弹的位置"""
        self.bullets.update()
        """删除已经消失的子弹，判断子弹的边缘是否过了屏幕最顶端"""
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _update_screen(self):
        """更新屏幕上的图像，并切换到新屏幕"""
        self.screen.fill(self.settings.bg_color)
        """绘制屏幕上的子弹"""
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        # 调用绘制的飞船
        self.ship.bitme()
        # 调用外星人
        self.aliens.draw(self.screen)
        # 让最近绘制的屏幕可见
        pygame.display.flip()


if __name__ == '__main__':
    # 创建游戏实例并运行实例
    ai = AlienInvasion()
    ai.run_game()
