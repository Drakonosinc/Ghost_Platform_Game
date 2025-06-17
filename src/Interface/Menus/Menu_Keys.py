from pygame.locals import KEYDOWN
from pygame import Rect
from .Base_Menu import BaseMenu
import pygame_gui
class KeysMenu(BaseMenu):
    def __init__(self, interface):
        super().__init__(interface)
        self.buttons = {}
        self.key = None
        self.key_name = None
        self.button_key = None
    def setup_buttons(self):pass
    def render(self):
        self.setup_buttons()
        self.interface.active_buttons = [button for button in self.buttons.values()]