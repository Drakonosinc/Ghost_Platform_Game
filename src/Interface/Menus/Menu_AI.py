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
        self.screen.blit(self.interface.font3_5.render(f"Generation Size {self.config.config_AI["generation_value"]}", True, "White"),(10,80))
        self.screen.blit(self.interface.font3_5.render(f"Population Size {self.config.config_AI["population_value"]}", True, "White"),(10,120))
        self.screen.blit(self.interface.font3_5.render(f"Number of try for AI {self.config.config_AI["try_for_ai"]}", True, "White"),(10,160))
        self.setup_buttons()
        self.interface.active_buttons = [button for button in self.buttons.values()]