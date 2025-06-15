from .Base_Menu import BaseMenu
import pygame_gui
from pygame import Rect
class OptionsMenu(BaseMenu):
    def __init__(self, interface):
        super().__init__(interface)
        self.buttons = {}
    def setup_buttons(self):
        self.buttons['visual'] = pygame_gui.elements.UIButton(relative_rect=Rect(10, 100, 100, 50),text="Visuals",manager=self.interface.manager,command=lambda:self.change_mains(5))
        self.buttons['keys'] = pygame_gui.elements.UIButton(relative_rect=Rect(10, 200, 100, 50),text='Keys',manager=self.interface.manager,command=lambda:self.change_mains(6))
        self.buttons['sound'] = pygame_gui.elements.UIButton(relative_rect=Rect(10, 150, 100, 50),text='Sounds',manager=self.interface.manager,command=lambda:self.change_mains(7))
        self.buttons['main'] = pygame_gui.elements.UIButton(relative_rect=Rect(10, self.HEIGHT-50, 100, 50),text='Back',manager=self.interface.manager,command=lambda:self.change_mains(0))
    def render(self):
        self.screen.fill(self.interface.BLACK)
        self.screen.blit(self.interface.font3.render("Options", True, "White"),(3,10))
        self.interface.active_buttons = [button for button in self.buttons.values()]