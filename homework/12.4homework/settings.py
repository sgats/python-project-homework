"""存储火箭中所有涉及到的类"""


class Settings:
    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (255, 225, 255)
        """调整飞船的速度"""
        self.rocket_speed = 1.5
