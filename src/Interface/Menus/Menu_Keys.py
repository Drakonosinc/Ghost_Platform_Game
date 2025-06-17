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
        self.screen.fill(self.interface.BLACK)
        self.screen.blit(self.interface.font3.render("Keys", True, "White"),(3,10))
        self.screen.blit(self.interface.font3_5.render(f"Jump One", True, "White"),(10,100))
        self.screen.blit(self.interface.font3_5.render(f"Jump Two", True, "White"),(10,150))
        self.screen.blit(self.interface.font3_5.render(f"Move Left", True, "White"),(10,200))
        self.screen.blit(self.interface.font3_5.render(f"Move Right", True, "White"),(10,250))
        self.screen.blit(self.interface.font3_5.render(f"To Restart Config", True, "White"),(10,300))
        self.setup_buttons()
        self.interface.active_buttons = [button for button in self.buttons.values()]