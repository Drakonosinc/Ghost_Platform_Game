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
        self.utils_keys:dict[str, bool]={"up1":False,"up2":False,"left":False,"right":False}
    def setup_buttons(self):
        self.buttons['back'] = pygame_gui.elements.UIButton(relative_rect=Rect(10, self.HEIGHT-50, 100, 50),text='Back',manager=self.interface.manager,command=lambda:self.change_mains(0))
        self.buttons['key_up1'] = pygame_gui.elements.UIButton(relative_rect=Rect(220, 100, 50, 50),text=f"{self.config.config_keys["name_up1"]}",manager=self.interface.manager,object_id="#button_on" if self.utils_keys["up1"] else None,command=lambda:self.change_keys("up1","name_up1"))
        self.buttons['key_up2'] = pygame_gui.elements.UIButton(relative_rect=Rect(220, 150, 50, 50),text=f"{self.config.config_keys["name_up2"]}",manager=self.interface.manager,object_id="#button_on" if self.utils_keys["up2"] else None,command=lambda:self.change_keys("up2","name_up2"))
        self.buttons['key_left'] = pygame_gui.elements.UIButton(relative_rect=Rect(220, 200, 50, 50),text=f"{self.config.config_keys["name_left"]}",manager=self.interface.manager,object_id="#button_on" if self.utils_keys["left"] else None,command=lambda:self.change_keys("left","name_left"))
        self.buttons['key_right'] = pygame_gui.elements.UIButton(relative_rect=Rect(220, 250, 50, 50),text=f"{self.config.config_keys["name_right"]}",manager=self.interface.manager,object_id="#button_on" if self.utils_keys["right"] else None,command=lambda:self.change_keys("right","name_right"))
        self.buttons['restar_config_key'] = pygame_gui.elements.UIButton(relative_rect=Rect(360, 300, 80, 50),text="Press",object_id="#button_on",manager=self.interface.manager,command=lambda:self.more_options([lambda:self.config.config(keys=True),self.config.save_config,lambda:self.change_mains(6,fade=False)]))
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
    def change_keys(self,key,key_name):
        self.key=key
        self.key_name=key_name
        for k in self.utils_keys.keys():self.utils_keys[k]=False if k!=self.key else not self.utils_keys[self.key]
        self.change_mains(6,fade=False)
    def event_change_keys(self,event):
        if self.key!=None and (self.utils_keys[self.key] and event.type==KEYDOWN):
            self.config.config_keys[self.key]=event.key
            self.config.config_keys[self.key_name]=event.unicode.upper() if self.config.config_keys[self.key]!=32 else "Space"
            self.utils_keys[self.key]= not self.utils_keys[self.key]
            self.change_mains(6,fade=False),self.config.save_config()