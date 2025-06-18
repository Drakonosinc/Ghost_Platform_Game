from pygame import Rect
from .Base_Menu import BaseMenu
import pygame_gui
class KeysMenu(BaseMenu):
    def __init__(self, interface):
        super().__init__(interface)
        self.buttons = {}
    def setup_buttons(self):pass
    def render(self):
        self.setup_buttons()
        self.interface.active_buttons = [button for button in self.buttons.values()]
    def on_off_sound(self,sound,type_sound,play=True,game=False,command=False):
        sound.play(loops=-1) if play and self.config.config_sounds[type_sound] else sound.stop()
        if game:self.on_off_sound(self.sound_game,"sound_game")
        if command:self.config.save_config()