from pygame import Rect
class Player:
    def __init__(self, x, y, width, height):
        self.rect = Rect(x, y, width, height)
        self.down_gravity = 0
        self.isjumper = False
        self.life = 100
        self.reward = 0
        self.active = True
    def jump(self, jumper_value):
        if self.isjumper:
            self.down_gravity = jumper_value
            self.isjumper = False
    def fall(self, gravity):
        self.down_gravity += gravity
        self.rect.y += self.down_gravity
    def reset(self, x, y):
        self.rect.x, self.rect.y = x, y
        self.down_gravity = 0
        self.isjumper = False
        self.life = 100
        self.reward = 0
        self.active = True
    def check_collision(self, other_rect):
        return self.rect.colliderect(other_rect)