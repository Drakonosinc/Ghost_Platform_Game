from pygame import Rect
from .Base_Menu import BaseMenu
import pygame_gui
class SoundsMenu(BaseMenu):
    def __init__(self, interface):
        super().__init__(interface)
        self.buttons = {}
    def setup_buttons(self):
        self.buttons['back'] = pygame_gui.elements.UIButton(relative_rect=Rect(10, self.HEIGHT-50, 100, 50),text='Back',manager=self.interface.manager,command=lambda:self.change_mains(0))
        self.buttons['sound_menu'] = pygame_gui.elements.UIButton(relative_rect=Rect(10, 100, 125, 50),text=f"Sound Menu {"ON" if self.config.config_sounds["sound_menu"] else "OFF"}",object_id="#button_on" if self.config.config_sounds["sound_menu"] else "#button_off",manager=self.interface.manager,command=lambda:self.on_off(7,self.config.config_sounds,False,"sound_menu",command=lambda:self.on_off_sound(self.interface.sound_menu,"sound_menu",True,command=True)))
        self.buttons['sound_game'] = pygame_gui.elements.UIButton(relative_rect=Rect(10, 150, 125, 50),text=f"Sound Game {"ON" if self.config.config_sounds["sound_game"] else "OFF"}",object_id="#button_on" if self.config.config_sounds["sound_game"] else "#button_off",manager=self.interface.manager,command=lambda:self.on_off(7,self.config.config_sounds,False,"sound_game",command=lambda:self.on_off_sound(self.interface.sound_game,"sound_game",False,command=True)))
        self.buttons['on_off_jump'] = pygame_gui.elements.UIButton(relative_rect=Rect(220, 200, 50, 40),text=f"{self.config.config_sounds["sound_jump"]}",object_id="#button_on" if self.config.config_sounds["sound_jump"] else "#button_off",manager=self.interface.manager,command=lambda:self.on_off(7,self.config.config_sounds,False,"sound_jump",command=self.config.save_config))
        self.buttons['on_off_game_over'] = pygame_gui.elements.UIButton(relative_rect=Rect(220, 240, 50, 40),text=f"{self.config.config_sounds["game_over"]}",object_id="#button_on" if self.config.config_sounds["game_over"] else "#button_off",manager=self.interface.manager,command=lambda:self.on_off(7,self.config.config_sounds,False,"game_over",command=self.config.save_config))
        self.buttons['on_off_damage'] = pygame_gui.elements.UIButton(relative_rect=Rect(220, 280, 50, 40),text=f"{self.config.config_sounds["sound_damage"]}",object_id="#button_on" if self.config.config_sounds["sound_damage"] else "#button_off",manager=self.interface.manager,command=lambda:self.on_off(7,self.config.config_sounds,False,"sound_damage",command=self.config.save_config))
        self.buttons['on_off_potion'] = pygame_gui.elements.UIButton(relative_rect=Rect(220, 320, 50, 40),text=f"{self.config.config_sounds["sound_potion"]}",object_id="#button_on" if self.config.config_sounds["sound_potion"] else "#button_off",manager=self.interface.manager,command=lambda:self.on_off(7,self.config.config_sounds,False,"sound_potion",command=self.config.save_config))
        self.buttons['on_off_shield'] = pygame_gui.elements.UIButton(relative_rect=Rect(220, 360, 50, 40),text=f"{self.config.config_sounds["sound_shield"]}",object_id="#button_on" if self.config.config_sounds["sound_shield"] else "#button_off",manager=self.interface.manager,command=lambda:self.on_off(7,self.config.config_sounds,False,"sound_shield",command=self.config.save_config))
        
    def render(self):
        self.screen.fill(self.interface.BLACK)
        self.screen.blit(self.interface.font3.render("Sounds", True, "White"),(3,10))
        self.screen.blit(self.interface.font3_5.render(f"Sound Jump", True, "White"),(10,200))
        self.screen.blit(self.interface.font3_5.render(f"Game Over", True, "White"),(10,240))
        self.screen.blit(self.interface.font3_5.render(f"Damage", True, "White"),(10,280))
        self.screen.blit(self.interface.font3_5.render(f"Potion", True, "White"),(10,320))
        self.screen.blit(self.interface.font3_5.render(f"Shield", True, "White"),(10,360))
        self.screen.blit(self.interface.font3_5.render(f"To Restart Config", True, "White"),(10,400))
        self.setup_buttons()
        self.interface.active_buttons = [button for button in self.buttons.values()]
    def on_off_sound(self,sound,type_sound,play=True,game=False,command=False):
        sound.play(loops=-1) if play and self.config.config_sounds[type_sound] else sound.stop()
        if game:self.on_off_sound(self.interface.sound_game,"sound_game")
        if command:self.config.save_config()