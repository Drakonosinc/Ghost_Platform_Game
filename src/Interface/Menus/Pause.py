from .Base_Menu import BaseMenu
from pygame import Rect
import pygame_gui
class Pause(BaseMenu):
    def __init__(self, interface):
        super().__init__(interface)
        self.buttons = {}
    def setup_buttons(self):
        self.buttons['main'] = pygame_gui.elements.UIButton(relative_rect=Rect(10, 150, 150, 50),text='Exit The Menu',manager=self.interface.manager,command=lambda:self.change_mains(0,command=self.type_game,command2=lambda:[self.on_off_sound(x,y,False) for x,y in zip([self.sound_menu,self.sound_game],["sound_menu","sound_game"])],run=True))
        self.buttons['reset'] = pygame_gui.elements.UIButton(relative_rect=Rect(10, 100, 150, 50),text="Press R to Restart",manager=self.interface.manager,command=lambda:self.change_mains(-1,command=self.reset))
        self.buttons['exit'] = pygame_gui.elements.UIButton(relative_rect=Rect(10, 200, 150, 50),text='Exit The Game',manager=self.interface.manager,command=lambda: self.change_mains(command=self.close_game,sound=self.sound_exit))

    def render(self):
        self.filt(self.WIDTH,self.HEIGHT,150,self.interface.GRAY)
        self.screen.blit(self.interface.font3.render("Pause", True, "White"),(3,10))