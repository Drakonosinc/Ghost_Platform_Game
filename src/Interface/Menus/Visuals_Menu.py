import pygame_gui
from .Base_Menu import BaseMenu
from pygame import Rect
class VisualsMenu(BaseMenu):
    def __init__(self, interface):
        super().__init__(interface)
        self.buttons = {}
    def setup_buttons(self):
        self.buttons['back'] = pygame_gui.elements.UIButton(relative_rect=Rect(10, self.HEIGHT-50, 100, 50),text='Back',manager=self.interface.manager)
        self.buttons['increase_floor'] = pygame_gui.elements.UIButton(relative_rect=Rect(290, 100, 50, 40),text='>',manager=self.interface.manager,command=lambda:self.increase_decrease_variable(5,"floor_value",1,dic=self.config.config_visuals,length="floor",command=self.interface.load_images,recu=True))
        self.buttons['decrease_floor'] = pygame_gui.elements.UIButton(relative_rect=Rect(10, 100, 50, 40),text='<',manager=self.interface.manager,command=lambda:self.increase_decrease_variable(5,"floor_value",-1,dic=self.config.config_visuals,length="floor",command=self.interface.load_images,recu=True))
        self.buttons['increase_meteorite'] = pygame_gui.elements.UIButton(relative_rect=Rect(290, 200, 50, 40),text='>',manager=self.interface.manager,command=lambda:self.increase_decrease_variable(5,"meteorite_value",1,dic=self.config.config_visuals,length="meteorite",command=self.interface.load_images,recu=True))
        self.buttons['decrease_meteorite'] = pygame_gui.elements.UIButton(relative_rect=Rect(10, 200, 50, 40),text='<',manager=self.interface.manager,command=lambda:self.increase_decrease_variable(5,"meteorite_value",-1,dic=self.config.config_visuals,length="meteorite",command=self.interface.load_images,recu=True))
        self.buttons['increase_potion'] = pygame_gui.elements.UIButton(relative_rect=Rect(290, 300, 50, 40),text='>',manager=self.interface.manager,command=lambda:self.increase_decrease_variable(5,"potion_value",1,dic=self.config.config_visuals,length="potion",command=self.interface.load_images,recu=True))
        self.buttons['decrease_potion'] = pygame_gui.elements.UIButton(relative_rect=Rect(10, 300, 50, 40),text='<',manager=self.interface.manager,command=lambda:self.increase_decrease_variable(5,"potion_value",-1,dic=self.config.config_visuals,length="potion",command=self.interface.load_images,recu=True))
        self.buttons['increase_shield'] = pygame_gui.elements.UIButton(relative_rect=Rect(290, 400, 50, 40),text='>',manager=self.interface.manager,command=lambda:self.increase_decrease_variable(5,"shield_value",1,dic=self.config.config_visuals,length="shield",command=self.interface.load_images,recu=True))
        self.buttons['decrease_shield'] = pygame_gui.elements.UIButton(relative_rect=Rect(10, 400, 50, 40),text='<',manager=self.interface.manager,command=lambda:self.increase_decrease_variable(5,"shield_value",-1,dic=self.config.config_visuals,length="shield",command=self.interface.load_images,recu=True))
    def render(self):
        self.screen.fill(self.interface.BLACK)
        self.screen.blit(self.interface.font3.render("Visuals", True, "White"),(3,10))
        self.screen.blit(self.interface.floor,(150,100))
        self.screen.blit(self.interface.meteorite,(150,150))
        self.screen.blit(self.interface.potion,(150,300))
        self.screen.blit(self.interface.shield,(150,400))
        self.screen.blit(self.interface.player_ghost,(150,500))
        self.setup_buttons()
        self.interface.active_buttons = [button for button in self.buttons.values()]