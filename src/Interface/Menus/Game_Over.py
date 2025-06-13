from .Base_Menu import BaseMenu
from pygame import Rect
import pygame_gui
class GameOver(BaseMenu):
    def __init__(self, interface):
        super().__init__(interface)
        self.buttons = {}
    def setup_buttons(self):
        self.buttons['main'] = pygame_gui.elements.UIButton(relative_rect=Rect(10, 150, 150, 50),text='Exit The Menu',manager=self.interface.manager)
        self.buttons['reset'] = pygame_gui.elements.UIButton(relative_rect=Rect(10, 100, 150, 50),text="Press R to Restart",manager=self.interface.manager)
        self.buttons['exit'] = pygame_gui.elements.UIButton(relative_rect=Rect(10, 200, 150, 50),text='Exit The Game',manager=self.interface.manager)
    def render(self):
        self.filt(self.WIDTH,self.HEIGHT,150,self.interface.RED)
        self.screen.blit(self.interface.font4.render("Game Over", True, self.interface.BLACK),(3,10))
        self.interface.active_buttons = [button for button in self.buttons.values()]