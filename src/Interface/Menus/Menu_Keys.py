from pygame.locals import KEYDOWN
from .Base_Menu import BaseMenu
class KeysMenu(BaseMenu):
    def __init__(self, interface):
        super().__init__(interface)
        self.buttons = {}
        self.key = None
        self.key_name = None
        self.utils_keys: dict[str, bool] = {"up1": False, "up2": False, "left": False, "right": False}
    def setup_buttons(self):
        factory = self.interface.button_factory_f2_5
        self.buttons['back'] = factory.create_TextButton({"text": "Back", "position": (10, self.HEIGHT - 60), "command1": lambda: self.change_mains(4)})
        self.buttons['key_up1'] = factory.create_TextButton({"text": f"{self.config.config_keys['name_up1']}", "position": (250, 100), "command1": lambda: self.change_keys("up1", "name_up1")})
        self.buttons['key_up2'] = factory.create_TextButton({"text": f"{self.config.config_keys['name_up2']}", "position": (250, 150), "command1": lambda: self.change_keys("up2", "name_up2")})
        self.buttons['key_left'] = factory.create_TextButton({"text": f"{self.config.config_keys['name_left']}", "position": (250, 200), "command1": lambda: self.change_keys("left", "name_left")})
        self.buttons['key_right'] = factory.create_TextButton({"text": f"{self.config.config_keys['name_right']}", "position": (250, 250), "command1": lambda: self.change_keys("right", "name_right")})
        self.buttons['restar_config_key'] = factory.create_TextButton({"text": "Reset", "color": self.interface.SKYBLUE, "position": (360, 300), "command1": lambda: self.more_options([lambda: self.config.config(keys=True), self.config.save_config, self._refresh_key_buttons])})
    def _refresh_key_buttons(self):
        mapping = [("key_up1", "up1", "name_up1"), ("key_up2", "up2", "name_up2"), ("key_left", "left", "name_left"), ("key_right", "right", "name_right")]
        for btn_key, util_key, cfg_name in mapping:
            if btn_key in self.buttons:
                self.buttons[btn_key].change_item({
                    "text": f"{self.config.config_keys[cfg_name]}",
                    "color": self.interface.SKYBLUE if self.utils_keys[util_key] else self.interface.WHITE,
                })
    def render(self):
        self.screen.fill(self.interface.BLACK)
        self.screen.blit(self.interface.font3.render("Keys", True, "White"), (3, 10))
        self.screen.blit(self.interface.font3_5.render("Jump One", True, "White"), (10, 100))
        self.screen.blit(self.interface.font3_5.render("Jump Two", True, "White"), (10, 150))
        self.screen.blit(self.interface.font3_5.render("Move Left", True, "White"), (10, 200))
        self.screen.blit(self.interface.font3_5.render("Move Right", True, "White"), (10, 250))
        self.screen.blit(self.interface.font3_5.render("To Restart Config", True, "White"), (10, 300))
        self._refresh_key_buttons()
        self.execute_buttons(*self.buttons.values())
    def change_keys(self, key, key_name):
        self.key = key
        self.key_name = key_name
        for k in self.utils_keys.keys():
            self.utils_keys[k] = False if k != self.key else not self.utils_keys[self.key]
        self._refresh_key_buttons()
    def event_change_keys(self, event):
        if self.key is not None and (self.utils_keys[self.key] and event.type == KEYDOWN):
            self.config.config_keys[self.key] = event.key
            self.config.config_keys[self.key_name] = event.unicode.upper() if self.config.config_keys[self.key] != 32 else "Space"
            self.utils_keys[self.key] = not self.utils_keys[self.key]
            self.config.save_config()
            self._refresh_key_buttons()
