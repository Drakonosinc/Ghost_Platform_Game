import os, pygame, pygame_gui
from .Base_Menu import BaseMenu
class GameMode(BaseMenu):
    def __init__(self, interface):
        super().__init__(interface)
        self.buttons = {}
        self.inputs = {}
        self.config_buttons = {}
        self.training_ai_elements = {}