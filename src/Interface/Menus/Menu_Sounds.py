from pygame import Rect
from .Base_Menu import BaseMenu
import pygame_gui
class SoundsMenu(BaseMenu):
    def __init__(self, interface):
        super().__init__(interface)
        self.buttons = {}
    def setup_buttons(self):pass
    def render(self):
        self.screen.fill(self.interface.BLACK)
        self.screen.blit(self.interface.font3.render("Sounds", True, "White"),(3,10))
        self.screen.blit(self.interface.font3_5.render(f"Sound Jump", True, "White"),(10,200))
        self.screen.blit(self.interface.font3_5.render(f"Game Over", True, "White"),(10,240))
        self.screen.blit(self.interface.font3_5.render(f"Damage", True, "White"),(10,280))
        self.screen.blit(self.interface.font3_5.render(f"Potion", True, "White"),(10,320))
        self.setup_buttons()
        self.interface.active_buttons = [button for button in self.buttons.values()]
    def on_off_sound(self,sound,type_sound,play=True,game=False,command=False):
        sound.play(loops=-1) if play and self.config.config_sounds[type_sound] else sound.stop()
        if game:self.on_off_sound(self.sound_game,"sound_game")
        if command:self.config.save_config()