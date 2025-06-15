from .Base_Menu import BaseMenu
import pygame_gui
from pygame import Rect
class OptionsMenu(BaseMenu):
    def __init__(self, interface):
        super().__init__(interface)
        self.buttons = {}
    def setup_buttons(self):pass
    def render(self):pass