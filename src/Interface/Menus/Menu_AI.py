from .Base_Menu import BaseMenu
class AIMenu(BaseMenu):
    def __init__(self, interface):
        super().__init__(interface)
        self.buttons = {}
    def setup_buttons(self):
        factory = self.interface.button_factory_f2_5
        self.buttons['back'] = factory.create_TextButton({"text": "Back", "position": (10, self.HEIGHT - 60), "command1": lambda: self.change_mains(2)})
        self.buttons['save'] = factory.create_TextButton({"font": self.interface.font5, "text": f"Save model {'ON' if self.config.config_AI['model_save'] else 'OFF'}", "position": (self.WIDTH - 260, 25), "command1": lambda: self.on_off(8, self.config.config_AI, False, "model_save", command=self.config.save_config)})
        self.buttons['play'] = factory.create_TextButton({"text": "Play", "position": (self.WIDTH - 130, self.HEIGHT - 60), "command1": lambda: self.change_mains(-1, run=True, command=lambda: self.type_game(mode_one=True), command2=lambda: self.more_options([self.interface.population, lambda: self.on_off_sound(self.interface.sound_menu, "sound_menu", False, game=True)]))})
        self.buttons['restar_config_ai'] = factory.create_TextButton({"text": "Reset", "color": self.interface.SKYBLUE, "position": (self.WIDTH - 160, 280), "command1": lambda: self.more_options([lambda: self.config.config(AI=True), self.config.save_config])})
        self.buttons['increase_generation'] = factory.create_TextButton({"font": self.interface.font3_5, "text": "+", "position": (self.WIDTH - 60, 80), "command1": lambda: self.increase_decrease_variable(8, "generation_value", 1, dic=self.config.config_AI)})
        self.buttons['decrease_generation'] = factory.create_TextButton({"font": self.interface.font3_5, "text": "-", "position": (self.WIDTH - 120, 80), "command1": lambda: self.increase_decrease_variable(8, "generation_value", -1, dic=self.config.config_AI)})
        self.buttons['increase_population'] = factory.create_TextButton({"font": self.interface.font3_5, "text": "+", "position": (self.WIDTH - 60, 120), "command1": lambda: self.increase_decrease_variable(8, "population_value", 1, True, dic=self.config.config_AI)})
        self.buttons['decrease_population'] = factory.create_TextButton({"font": self.interface.font3_5, "text": "-", "position": (self.WIDTH - 120, 120), "command1": lambda: self.increase_decrease_variable(8, "population_value", -1, True, dic=self.config.config_AI)})
        self.buttons['increase_try_for_ai'] = factory.create_TextButton({"font": self.interface.font3_5, "text": "+", "position": (self.WIDTH - 60, 160), "command1": lambda: self.increase_decrease_variable(8, "try_for_ai", 1, dic=self.config.config_AI)})
        self.buttons['decrease_try_for_ai'] = factory.create_TextButton({"font": self.interface.font3_5, "text": "-", "position": (self.WIDTH - 120, 160), "command1": lambda: self.increase_decrease_variable(8, "try_for_ai", -1, dic=self.config.config_AI)})
    def render(self):
        self.screen.fill(self.interface.BLACK)
        self.screen.blit(self.interface.font3.render("Config AI", True, "White"), (3, 10))
        self.screen.blit(self.interface.font3_5.render(f"Generation Size {self.config.config_AI['generation_value']}", True, "White"), (10, 80))
        self.screen.blit(self.interface.font3_5.render(f"Population Size {self.config.config_AI['population_value']}", True, "White"), (10, 120))
        self.screen.blit(self.interface.font3_5.render(f"Number of try for AI {self.config.config_AI['try_for_ai']}", True, "White"), (10, 160))
        self.screen.blit(self.interface.font3_5.render("To Restart Config", True, "White"), (10, 280))
        self.buttons['save'].change_item({
            "text": f"Save model {'ON' if self.config.config_AI['model_save'] else 'OFF'}",
            "color": self.interface.SKYBLUE if self.config.config_AI['model_save'] else self.interface.RED,
        })
        self.execute_buttons(*self.buttons.values())
