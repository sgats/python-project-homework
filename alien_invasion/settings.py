# 将新的一些设置存储在该模块中，用来统一管理
class Settings:
    """存储游戏《外星人入侵》中所有设置的类"""
    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.alien_points = None
        self.alien_speed = None
        self.bullet_speed = None
        self.ship_speed = None
        self.fleet_direction = None
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        # 飞船限制三次
        self.ship_limit = 3
        # 子弹设置
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        """限制子弹只能在屏幕上最多存在10个"""
        self.bullets_allowed = 10

        """设置外星人向下移动"""
        self.fleet_drop_speed = 5

        # 以什么速度加快游戏的节奏
        self.speedup_scale = 1.2
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        # 设置飞船的移动速度
        self.ship_speed = 2.5
        # 添加子弹的设置
        self.bullet_speed = 2.5
        """设置外星人的速度"""
        self.alien_speed = 1.5
        """fleet_direction 为 1表示向右移动， 为-1表示向左移动"""
        self.fleet_direction = 1
        "记分设置"
        self.alien_points = 50

    def increase_speed(self):
        """提高速度设置的值和外星人分数"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)

