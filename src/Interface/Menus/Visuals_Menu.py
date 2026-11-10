from .Base_Menu import BaseMenu
class VisualsMenu(BaseMenu):
    def __init__(self, interface):
        super().__init__(interface)
        self.buttons = {}
    def setup_buttons(self):
        factory = self.interface.button_factory_f2_5
        self.buttons['back'] = factory.create_TextButton({"text": "Back", "position": (10, self.HEIGHT - 60), "command1": lambda: self.change_mains(4)})
        self.buttons['increase_floor'] = factory.create_TextButton({"font": self.interface.font3_5, "text": ">", "position": (290, 100), "command1": lambda: self.increase_decrease_variable(5, "floor_value", 1, dic=self.config.config_visuals, length="floor", command=self.interface.load_images, recu=False)})
        self.buttons['decrease_floor'] = factory.create_TextButton({"font": self.interface.font3_5, "text": "<", "position": (10, 100), "command1": lambda: self.increase_decrease_variable(5, "floor_value", -1, dic=self.config.config_visuals, length="floor", command=self.interface.load_images, recu=False)})
        self.buttons['increase_meteorite'] = factory.create_TextButton({"font": self.interface.font3_5, "text": ">", "position": (290, 200), "command1": lambda: self.increase_decrease_variable(5, "meteorite_value", 1, dic=self.config.config_visuals, length="meteorite", command=self.interface.load_images, recu=False)})
        self.buttons['decrease_meteorite'] = factory.create_TextButton({"font": self.interface.font3_5, "text": "<", "position": (10, 200), "command1": lambda: self.increase_decrease_variable(5, "meteorite_value", -1, dic=self.config.config_visuals, length="meteorite", command=self.interface.load_images, recu=False)})
        self.buttons['increase_potion'] = factory.create_TextButton({"font": self.interface.font3_5, "text": ">", "position": (290, 300), "command1": lambda: self.increase_decrease_variable(5, "potion_value", 1, dic=self.config.config_visuals, length="potion", command=self.interface.load_images, recu=False)})
        self.buttons['decrease_potion'] = factory.create_TextButton({"font": self.interface.font3_5, "text": "<", "position": (10, 300), "command1": lambda: self.increase_decrease_variable(5, "potion_value", -1, dic=self.config.config_visuals, length="potion", command=self.interface.load_images, recu=False)})
        self.buttons['increase_shield'] = factory.create_TextButton({"font": self.interface.font3_5, "text": ">", "position": (290, 400), "command1": lambda: self.increase_decrease_variable(5, "shield_value", 1, dic=self.config.config_visuals, length="shield", command=self.interface.load_images, recu=False)})
        self.buttons['decrease_shield'] = factory.create_TextButton({"font": self.interface.font3_5, "text": "<", "position": (10, 400), "command1": lambda: self.increase_decrease_variable(5, "shield_value", -1, dic=self.config.config_visuals, length="shield", command=self.interface.load_images, recu=False)})
        self.buttons['increase_player'] = factory.create_TextButton({"font": self.interface.font3_5, "text": ">", "position": (290, 500), "command1": lambda: self.increase_decrease_variable(5, "player_value", 1, dic=self.config.config_visuals, length="player", command=self.interface.load_images, recu=False)})
        self.buttons['decrease_player'] = factory.create_TextButton({"font": self.interface.font3_5, "text": "<", "position": (10, 500), "command1": lambda: self.increase_decrease_variable(5, "player_value", -1, dic=self.config.config_visuals, length="player", command=self.interface.load_images, recu=False)})
    def render(self):
        self.screen.fill(self.interface.BLACK)
        self.screen.blit(self.interface.font3.render("Visuals", True, "White"), (3, 10))
        self.screen.blit(self.interface.floor, (150, 100))
        self.screen.blit(self.interface.meteorite, (150, 150))
        self.screen.blit(self.interface.potion, (150, 300))
        self.screen.blit(self.interface.shield, (150, 400))
        self.screen.blit(self.interface.player_ghost, (150, 500))
        self.execute_buttons(*self.buttons.values())
