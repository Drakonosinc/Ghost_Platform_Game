from .Base_Menu import BaseMenu
class GameOver(BaseMenu):
    def __init__(self, interface):
        super().__init__(interface)
        self.buttons = {}
    def setup_buttons(self):
        factory = self.interface.button_factory_f2_5
        self.buttons['reset'] = factory.create_TextButton({"text": "Press R to Restart", "position": (10, 100), "command1": lambda: self.change_mains(-1, command=self.interface.reset)})
        self.buttons['main'] = factory.create_TextButton({"text": "Exit The Menu", "position": (10, 150), "command1": lambda: self.change_mains(0, command=self.type_game, command2=lambda: [self.on_off_sound(x, y, False) for x, y in zip([self.interface.sound_menu, self.interface.sound_game], ["sound_menu", "sound_game"])], run=True)})
        self.buttons['exit'] = factory.create_TextButton({"text": "Exit The Game", "position": (10, 200), "sound_touch": self.interface.sound_exit, "command1": lambda: self.change_mains(command=self.interface.close_game, sound=self.interface.sound_exit)})
    def render(self):
        self.screen.fill(self.interface.BLACK)
        self.filt(self.WIDTH, self.HEIGHT, 150, self.interface.RED)
        self.screen.blit(self.interface.font4.render("Game Over", True, self.interface.BLACK), (3, 10))
        self.execute_buttons(*self.buttons.values())
