from pygame import Rect
from .Base_Menu import BaseMenu
import pygame_gui
class KeysMenu(BaseMenu):
    def __init__(self, interface):
        super().__init__(interface)
        self.buttons = {}
    def setup_buttons(self):pass