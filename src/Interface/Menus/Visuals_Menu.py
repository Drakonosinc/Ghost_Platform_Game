import pygame_gui
from .Base_Menu import BaseMenu
from pygame import Rect
class VisualsMenu(BaseMenu):
    def __init__(self, interface):
        super().__init__(interface)
        self.buttons = {}
    def setup_buttons(self):
        self.buttons['back'] = pygame_gui.elements.UIButton(relative_rect=Rect(10, self.HEIGHT-50, 100, 50),text='Back',manager=self.manager)
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