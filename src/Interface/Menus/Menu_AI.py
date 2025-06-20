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
        self.buttons['play'] = pygame_gui.elements.UIButton(relative_rect=Rect(self.WIDTH-110, self.HEIGHT-50, 100, 50),text='Play',manager=self.interface.manager,command=lambda:self.change_mains(-1,run=True,command=lambda:self.type_game(mode_one=True),command2=lambda:self.more_options([self.interface.population,lambda:self.on_off_sound(self.interface.sound_menu,"sound_menu",False,game=True)])))
        self.buttons['restar_config_ai'] = pygame_gui.elements.UIButton(relative_rect=Rect(self.WIDTH-120, 280, 110, 50),text="Press",object_id="#button_on",manager=self.interface.manager,command=lambda:self.more_options([lambda:self.config.config(AI=True),self.config.save_config,lambda:self.change_mains(8,fade=False)]))
        self.buttons['increase_generation'] = pygame_gui.elements.UIButton(relative_rect=Rect(self.WIDTH-60, 80, 50, 40),text='+',manager=self.interface.manager,command=lambda:self.increase_decrease_variable(8,"generation_value",1,dic=self.config.config_AI))
        self.buttons['decrease_generation'] = pygame_gui.elements.UIButton(relative_rect=Rect(self.WIDTH-120, 80, 50, 40),text='-',manager=self.interface.manager,command=lambda:self.increase_decrease_variable(8,"generation_value",-1,dic=self.config.config_AI)) if self.config.config_AI["generation_value"]>1 else None
        self.buttons['increase_population'] = pygame_gui.elements.UIButton(relative_rect=Rect(self.WIDTH-60, 120, 50, 40),text='+',manager=self.interface.manager,command=lambda:self.increase_decrease_variable(8,"population_value",1,True,dic=self.config.config_AI))
        self.buttons['decrease_population'] = pygame_gui.elements.UIButton(relative_rect=Rect(self.WIDTH-120, 120, 50, 40),text='-',manager=self.interface.manager,command=lambda:self.increase_decrease_variable(8,"population_value",-1,True,dic=self.config.config_AI)) if self.config.config_AI["population_value"]>1 else None
        self.buttons['increase_try_for_ai'] = pygame_gui.elements.UIButton(relative_rect=Rect(self.WIDTH-60, 160, 50, 40),text='+',manager=self.interface.manager,command=lambda:self.increase_decrease_variable(8,"try_for_ai",1,dic=self.config.config_AI))
        self.buttons['decrease_try_for_ai'] = pygame_gui.elements.UIButton(relative_rect=Rect(self.WIDTH-120, 160, 50, 40),text='-',manager=self.interface.manager,command=lambda:self.increase_decrease_variable(8,"try_for_ai",-1,dic=self.config.config_AI)) if self.config.config_AI["try_for_ai"]>1 else None
        self.buttons['type_training_ai'] = pygame_gui.elements.UIButton(relative_rect=Rect(self.WIDTH-120, 200, 110, 50),text="Change",object_id="#button_on",manager=self.interface.manager,command=lambda:self.more_options([lambda:self.change_mains(8,fade=False)]))
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