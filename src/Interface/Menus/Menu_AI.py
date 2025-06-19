from pygame import Rect
from .Base_Menu import BaseMenu
import pygame_gui
class AIMenu(BaseMenu):
    def __init__(self, interface):
        super().__init__(interface)
        self.buttons = {}
    def setup_buttons(self):pass
    def render(self):
        self.screen.fill(self.interface.BLACK)
        self.screen.blit(self.interface.font3.render("Config AI", True, "White"),(3,10))
        self.setup_buttons()
        self.interface.active_buttons = [button for button in self.buttons.values()]