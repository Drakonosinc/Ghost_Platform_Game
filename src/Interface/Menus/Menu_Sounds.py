from .Base_Menu import BaseMenu
class SoundsMenu(BaseMenu):
    def __init__(self, interface):
        super().__init__(interface)
        self.buttons = {}
    def setup_buttons(self):
        factory = self.interface.button_factory_f2_5
        self.buttons['back'] = factory.create_TextButton({"text": "Back", "position": (10, self.HEIGHT - 60), "command1": lambda: self.change_mains(4)})
        self.buttons['sound_menu'] = factory.create_TextButton({"text": f"Sound Menu {'ON' if self.config.config_sounds['sound_menu'] else 'OFF'}", "position": (10, 100), "command1": lambda: self.on_off(7, self.config.config_sounds, False, "sound_menu", command=lambda: self.on_off_sound(self.interface.sound_menu, "sound_menu", True, command=True))})
        self.buttons['sound_game'] = factory.create_TextButton({"text": f"Sound Game {'ON' if self.config.config_sounds['sound_game'] else 'OFF'}", "position": (10, 150), "command1": lambda: self.on_off(7, self.config.config_sounds, False, "sound_game", command=lambda: self.on_off_sound(self.interface.sound_game, "sound_game", False, command=True))})
        self.buttons['on_off_jump'] = factory.create_TextButton({"text": f"{self.config.config_sounds['sound_jump']}", "position": (260, 200), "command1": lambda: self.on_off(7, self.config.config_sounds, False, "sound_jump", command=self.config.save_config)})
        self.buttons['on_off_game_over'] = factory.create_TextButton({"text": f"{self.config.config_sounds['game_over']}", "position": (260, 240), "command1": lambda: self.on_off(7, self.config.config_sounds, False, "game_over", command=self.config.save_config)})
        self.buttons['on_off_damage'] = factory.create_TextButton({"text": f"{self.config.config_sounds['sound_damage']}", "position": (260, 280), "command1": lambda: self.on_off(7, self.config.config_sounds, False, "sound_damage", command=self.config.save_config)})
        self.buttons['on_off_potion'] = factory.create_TextButton({"text": f"{self.config.config_sounds['sound_potion']}", "position": (260, 320), "command1": lambda: self.on_off(7, self.config.config_sounds, False, "sound_potion", command=self.config.save_config)})
        self.buttons['on_off_shield'] = factory.create_TextButton({"text": f"{self.config.config_sounds['sound_shield']}", "position": (260, 360), "command1": lambda: self.on_off(7, self.config.config_sounds, False, "sound_shield", command=self.config.save_config)})
        self.buttons['restar_config_sound'] = factory.create_TextButton({"text": "Reset", "color": self.interface.SKYBLUE, "position": (360, 400), "command1": lambda: self.more_options([lambda: self.config.config(sounds=True), self.config.save_config])})
    def _refresh_sound_buttons(self):
        self.buttons['sound_menu'].change_item({"text": f"Sound Menu {'ON' if self.config.config_sounds['sound_menu'] else 'OFF'}", "color": self.interface.SKYBLUE if self.config.config_sounds['sound_menu'] else self.interface.RED})
        self.buttons['sound_game'].change_item({"text": f"Sound Game {'ON' if self.config.config_sounds['sound_game'] else 'OFF'}", "color": self.interface.SKYBLUE if self.config.config_sounds['sound_game'] else self.interface.RED})
        for btn_key, cfg_key in [("on_off_jump", "sound_jump"), ("on_off_game_over", "game_over"), ("on_off_damage", "sound_damage"), ("on_off_potion", "sound_potion"), ("on_off_shield", "sound_shield")]:
            val = self.config.config_sounds[cfg_key]
            self.buttons[btn_key].change_item({"text": "ON" if val else "OFF", "color": self.interface.SKYBLUE if val else self.interface.RED})
    def render(self):
        self.screen.fill(self.interface.BLACK)
        self.screen.blit(self.interface.font3.render("Sounds", True, "White"), (3, 10))
        self.screen.blit(self.interface.font3_5.render("Sound Jump", True, "White"), (10, 200))
        self.screen.blit(self.interface.font3_5.render("Game Over", True, "White"), (10, 240))
        self.screen.blit(self.interface.font3_5.render("Damage", True, "White"), (10, 280))
        self.screen.blit(self.interface.font3_5.render("Potion", True, "White"), (10, 320))
        self.screen.blit(self.interface.font3_5.render("Shield", True, "White"), (10, 360))
        self.screen.blit(self.interface.font3_5.render("To Restart Config", True, "White"), (10, 400))
        self._refresh_sound_buttons()
        self.execute_buttons(*self.buttons.values())
