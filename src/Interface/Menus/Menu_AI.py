from pygame import Rect
from .Base_Menu import BaseMenu
import pygame_gui
class AIMenu(BaseMenu):
    def __init__(self, interface):
        super().__init__(interface)
        self.buttons = {}
    def setup_buttons(self):
        self.buttons['back'] = pygame_gui.elements.UIButton(relative_rect=Rect(10, self.HEIGHT-50, 100, 50),text='Back',manager=self.interface.manager,command=lambda:self.change_mains(2))
        self.buttons['save'] = pygame_gui.elements.UIButton(relative_rect=Rect(self.WIDTH-160,10, 150, 50),text=f"Save model {self.config.config_AI["model_save"]}",object_id="#button_on" if self.config.config_AI["model_save"] else "#button_off",manager=self.interface.manager,command=lambda:self.on_off(8,self.config.config_AI,False,"model_save",command=self.config.save_config))
    def render(self):
        self.screen.fill(self.interface.BLACK)
        self.screen.blit(self.interface.font3.render("Config AI", True, "White"),(3,10))
        self.screen.blit(self.interface.font3_5.render(f"Generation Size {self.config.config_AI["generation_value"]}", True, "White"),(10,80))
        self.screen.blit(self.interface.font3_5.render(f"Population Size {self.config.config_AI["population_value"]}", True, "White"),(10,120))
        self.screen.blit(self.interface.font3_5.render(f"Number of try for AI {self.config.config_AI["try_for_ai"]}", True, "White"),(10,160))
        self.screen.blit(self.interface.font3_5.render(f"Type Training AI", True, "White"),(10,200))
        self.screen.blit(self.interface.font3_5.render(f"Type Model", True, "White"),(10,240))
        self.screen.blit(self.interface.font3_5.render(f"To Restart Config", True, "White"),(10,280))
        self.setup_buttons()
        self.interface.active_buttons = [button for button in self.buttons.values()]