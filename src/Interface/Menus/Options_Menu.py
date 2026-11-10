from .Base_Menu import BaseMenu
class OptionsMenu(BaseMenu):
    def __init__(self, interface):
        super().__init__(interface)
        self.buttons = {}
    def setup_buttons(self):
        factory = self.interface.button_factory_f2_5
        self.buttons['visual'] = factory.create_TextButton({"text": "Visuals", "position": (10, 100), "command1": lambda: self.change_mains(5)})
        self.buttons['sound'] = factory.create_TextButton({"text": "Sounds", "position": (10, 150), "command1": lambda: self.change_mains(7)})
        self.buttons['keys'] = factory.create_TextButton({"text": "Keys", "position": (10, 200), "command1": lambda: self.change_mains(6)})
        self.buttons['main'] = factory.create_TextButton({"text": "Back", "position": (10, self.HEIGHT - 60), "command1": lambda: self.change_mains(0)})
    def render(self):
        self.screen.fill(self.interface.BLACK)
        self.screen.blit(self.interface.font3.render("Options", True, "White"), (3, 10))
        self.execute_buttons(*self.buttons.values())
