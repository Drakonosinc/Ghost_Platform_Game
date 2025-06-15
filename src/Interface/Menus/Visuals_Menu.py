import pygame_gui
from .Base_Menu import BaseMenu
from pygame import Rect
class VisualsMenu(BaseMenu):
    def __init__(self, interface):
        super().__init__(interface)
        self.buttons = {}