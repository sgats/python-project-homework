import pygame
import sys
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien


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
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

    def _create_fleet(self):
        """创建一个外星舰队"""
        """创建一个外星人"""
        """创建一个外星人，再不断添加，直到没有空间添加外星人为止"""
        """外星人的间距为外星人的宽度"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        current_y, current_x = alien_height, alien_width
        while current_x < (self.settings.screen_width - 2 * alien_width):
            while current_y < (self.settings.screen_height - 2 * alien_height):
                self._create_alien(current_y, current_x)
                current_y += 2 * alien_height

            """添加一行外星人后， 重置y并递增x值"""
            current_y = alien_height
            current_x += 2 * alien_width

    def _create_alien(self, y_position, x_position):
        """创建一个外星人并放在当前行"""
        new_alien = Alien(self)
        new_alien.y = y_position
        new_alien.rect.y = y_position
        new_alien.rect.x = x_position
        self.aliens.add(new_alien)

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
            self._update_bullets()
            self._update_alien()
            self._update_screen()

    def _update_bullets(self):
        """更新子弹的位置并删除已经消失的子弹"""
        self.bullets.update()
        """删除已经消失的子弹"""
        for bullet in self.bullets.copy():
            if bullet.rect.left > self.settings.screen_width:
                self.bullets.remove(bullet)
        """检查是否有子弹击中了外星人"""
        """如果是，就删除相应的子弹和外星人"""
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

    def _update_alien(self):
        """更新外星舰队中所有外星人的位置"""
        self._check_fleet_edges()
        self.aliens.update()

    def _update_screen(self):
        """每次循环都重新绘制"""
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        """每次都重新绘制飞船"""
        self.ship.bitme()
        self.aliens.draw(self.screen)
        """让最近绘制的屏幕可见"""
        pygame.display.flip()
        self.clock.tick(60)

    def _fire_bullet(self):
        """创建一颗子弹，并加入到编组"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _check_fleet_edges(self):
        """再有外星人到达边缘时采取相应的措施"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """将整个外星舰队向左移动，并改变它们的方向"""
        for alien in self.aliens.sprites():
            alien.rect.x -= self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1


if __name__ == '__main__':
    """创建游戏实例并运行游戏"""
    run = BulletShip()
    run.run_game()
