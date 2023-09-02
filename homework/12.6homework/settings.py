"""专门对飞船进行设置"""


class Settings:
    def __init__(self):
        self.bg_color = (230, 230, 230)
        self.screen_width = 800
        self.screen_height = 600
        """设置飞船的速度"""
        self.ship_speed = 1.5
        """添加子弹设置"""
        self.bullet_speed = 2.0
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (60, 60, 60)
        """限制子弹的数量"""
        self.bullets_allowed = 5
