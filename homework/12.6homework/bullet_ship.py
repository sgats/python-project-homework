import pygame
import sys
from settings import Settings
from ship import Ship
from bullet import Bullet


class BulletShip:
    def __init__(self):
        self.settings = Settings()
        """初始化游戏并创建游戏资源"""
        pygame.init()
        """屏幕尺寸和显示信息"""
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("子弹射击屏幕")
        self.ship = Ship(self)
        """控制帧率,游戏中所有系统都应以相同的帧率运行"""
        self.clock = pygame.time.Clock()
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        """游戏的主循环"""
        while True:
            """监听键盘和鼠标事件"""
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.K_q:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        """向上移动飞船"""
                        self.ship.moving_up = True
                    elif event.key == pygame.K_DOWN:
                        """向下移动飞船"""
                        self.ship.moving_down = True
                    elif event.key == pygame.K_SPACE:
                        self._fire_bullet()
                elif event.type == pygame.KEYUP:
                    self.ship.moving_up = False
                    self.ship.moving_down = False
            self.ship.update()
            self.bullets.update()
            """删除已经消失的子弹"""
            for bullet in self.bullets.copy():
                if bullet.rect.left > self.settings.screen_width:
                    self.bullets.remove(bullet)
            """每次循环都重新绘制"""
            self.screen.fill(self.settings.bg_color)
            for bullet in self.bullets.sprites():
                bullet.draw_bullet()
            """每次都重新绘制飞船"""
            self.ship.bitme()
            """让最近绘制的屏幕可见"""
            pygame.display.flip()
            self.clock.tick(60)

    def _fire_bullet(self):
        """创建一颗子弹，并加入到编组"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)


if __name__ == '__main__':
    """创建游戏实例并运行游戏"""
    run = BulletShip()
    run.run_game()
