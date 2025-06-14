import os, pygame, pygame_gui
from pygame import Rect
from .Base_Menu import BaseMenu
class GameMode(BaseMenu):
    def __init__(self, interface):
        super().__init__(interface)
        self.buttons = {}
    def setup_buttons(self):
        self.buttons['training_ai'] = pygame_gui.elements.UIButton(relative_rect=Rect(10, 100, 100, 50),text='Training AI',manager=self.interface.manager,command=lambda:self.change_mains(8))
        self.buttons['player'] = pygame_gui.elements.UIButton(relative_rect=Rect(10, 150, 100, 50),text='Player',manager=self.manager,command=lambda:self.change_mains(-1,command=lambda:self.type_game(mode_two=True),run=True,command2=lambda:self.more_options([self.population,lambda:self.on_off_sound(self.sound_menu,"sound_menu",False,game=True)])))
        
    def render(self):pass