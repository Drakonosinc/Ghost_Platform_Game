from pyforgeui import *
from Loaders.Load_elements import *
from .Menus import *
class interface(load_elements,BaseMenu):
    def __init__(self,width=0, height=0):
        load_elements.__init__(self,"Ghost Platform",width,height)
        self.WIDTH:int = width
        self.HEIGHT:int = height
        BaseMenu.__init__(self,self)
        self.main:int=0 #-1=game, 0=menu, 1=game over, 2=game menu, 3=pausa, 4=options, 5=visuals, 6=menu keys, 7=sound menu, 8=menu AI
        self.active_buttons:list = []
        self.play_music()
        self.initialize_menus()
        self.draw_buttons()
    def initialize_menus(self):
        self.main_menu = MainMenu(self)
        self.game_over_menu = GameOver(self)
        self.game_mode_menu = GameMode(self)
        self.pause_menu = Pause(self)
        self.options_menu = OptionsMenu(self)
        self.visuals_menu = VisualsMenu(self)
        self.keys_menu = KeysMenu(self)
        self.sounds_menu = SoundsMenu(self)
        self.menu_AI = AIMenu(self)
    def draw_buttons(self):
        self.button_factory_f2_5 = ElementsFactory({"screen": self.screen, "font": self.font2_5, "hover_color": self.GOLDEN, "sound_hover": self.sound_buttonletters, "sound_touch": self.sound_touchletters})
        self.main_menu.setup_buttons()
        self.game_over_menu.setup_buttons()
        self.game_mode_menu.setup_buttons()
        self.pause_menu.setup_buttons()
        self.options_menu.setup_buttons()
        self.visuals_menu.setup_buttons()
        self.keys_menu.setup_buttons()
        self.sounds_menu.setup_buttons()
        self.menu_AI.setup_buttons()
    def draw_menus(self):
        menu_routes = {
            0: self.main_menu.render,
            1: self.game_over_menu.render,
            2: self.game_mode_menu.render,
            3: self.pause_menu.render,
            4: self.options_menu.render,
            5: self.visuals_menu.render,
            6: self.keys_menu.render,
            7: self.sounds_menu.render,
            8: self.menu_AI.render}
        if self.main in menu_routes:menu_routes[self.main]()
    def play_music(self):self.sound_menu.play(loops=-1) if self.config.config_sounds["sound_menu"] else self.sound_menu.stop()
