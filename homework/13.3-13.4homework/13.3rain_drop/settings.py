class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        """设置雨滴的速度"""
        self.rain_speed = 1.0
        self.fleep_drop_speed = 10
        """fleet_direction 为1 表示向右移动，为-1 表示向左移动"""
        self.fleet_direction = 1

    def update(self):
        """向右移动雨滴"""
        self.x += self.settings.rain_speed
        self.rect.x = self.x
