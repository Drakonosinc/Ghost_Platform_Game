from .Base_Menu import BaseMenu
class MainMenu(BaseMenu):
    def __init__(self, interface):
        super().__init__(interface)
        self.buttons = {}
    def setup_buttons(self):
        factory = self.interface.button_factory_f2_5
        self.buttons['play'] = factory.create_TextButton({"text": "Play", "position": (10, 100), "command1": lambda: self.change_mains(2)})
        self.buttons['options'] = factory.create_TextButton({"text": "Option", "position": (10, 150), "command1": lambda: self.change_mains(4)})
        self.buttons['quit'] = factory.create_TextButton({"text": "Exit", "position": (10, 200), "sound_touch": self.interface.sound_exit, "command1": lambda: self.change_mains(command=self.interface.close_game, sound=self.interface.sound_exit)})
    def render(self):
        self.screen.fill(self.interface.BLACK)
        self.screen.blit(self.interface.font3.render("Ghost Platform", True, self.interface.WHITE), (3, 10))
        self.execute_buttons(*self.buttons.values())
