import pygame_gui
from pygame import Rect
from .Base_Menu import BaseMenu
class GameMode(BaseMenu):
    def __init__(self, interface):
        super().__init__(interface)
        self.buttons = {}
    def setup_buttons(self):
        self.buttons['training_ai'] = pygame_gui.elements.UIButton(relative_rect=Rect(10, 100, 100, 50),text='Training AI',manager=self.interface.manager,command=lambda:self.change_mains(8))
        self.buttons['player'] = pygame_gui.elements.UIButton(relative_rect=Rect(10, 150, 100, 50),text='Player',manager=self.interface.manager,command=lambda:self.change_mains(-1,command=lambda:self.type_game(mode_two=True),run=True,command2=lambda:self.more_options([self.interface.population,lambda:self.on_off_sound(self.interface.sound_menu,"sound_menu",False,game=True)])))
        self.buttons['ai'] = pygame_gui.elements.UIButton(relative_rect=Rect(10, 200, 100, 50),text='AI',manager=self.interface.manager,command=lambda:self.change_mains(-1,command=lambda:self.type_game(mode_three=True),run=True,command2=lambda:self.more_options([self.interface.population,lambda:self.on_off_sound(self.interface.sound_menu,"sound_menu",False,game=True)])))
        self.buttons['back'] = pygame_gui.elements.UIButton(relative_rect=Rect(10, self.HEIGHT-50, 100, 50),text='Back',manager=self.interface.manager,command=lambda:self.change_mains(0))
    def render(self):
        self.screen.fill(self.interface.BLACK)
        self.screen.blit(self.interface.font3.render("Mode Game", True, "White"),(3,10))
        self.setup_buttons()
        self.interface.active_buttons = [button for button in self.buttons.values()]