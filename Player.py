from pygame import *
class Player:
    def __init__(self, x, y, width, height):
        self.rect = Rect(x, y, width, height)
        self.dy:float = 0
        self.life:int = 100
        self.is_jumper:bool = False
        self.state_life:list=[2,False]
        self.reward:int = 0
        self.scores:int=0
        self.floor_fall:bool=False
        self.active:bool = True
    def reset(self, x, y):
        self.rect.x, self.rect.y = x, y
        self.dy = 0
        self.isjumper = False
        self.life,self.scores = 100,0
        self.state_life=[2,False]
        self.floor_fall=False
        self.active = True
    def check_collision(self, other_rect):
        return self.rect.colliderect(other_rect)