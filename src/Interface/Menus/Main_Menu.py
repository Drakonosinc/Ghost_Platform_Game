from .Base_Menu import BaseMenu
from pygame import *
import pygame_gui
class MainMenu(BaseMenu):
    def __init__(self, interface):
        super().__init__(interface)
        self.buttons = {}
    def setup_buttons(self):
        self.buttons['play'] = pygame_gui.elements.UIButton(relative_rect=Rect(10, 100, 100, 50),text="Play",manager=self.interface.manager)
        self.buttons['options'] = pygame_gui.elements.UIButton(relative_rect=Rect(10, 150, 100, 50),text='Option',manager=self.interface.manager)
    def render(self):
        self.screen.fill(self.interface.BLACK)
        self.screen.blit(self.interface.font3.render("Ghost Platform",True,self.interface.WHITE),(3,10))