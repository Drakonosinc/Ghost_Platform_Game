import pygame_gui
from Loaders.Load_elements import *
from .Menus import *
class interface(load_elements,BaseMenu):
    def __init__(self,width=0, height=0):
        load_elements.__init__(self,"Ghost Platform",width,height)
        self.WIDTH:int = width
        self.HEIGHT:int = height
        BaseMenu.__init__(self,self)
        self.manager = pygame_gui.UIManager((self.WIDTH,self.HEIGHT),theme_path=os.path.join(self.config.config_path,"theme_buttons.json"))
        self.main:int=0 #-1=game, 0=menu, 1=game over, 2=game menu, 3=pausa, 4=options, 5=visuals, 6=menu keys, 7=sound menu, 8=menu AI
        self.active_buttons:list = []
        self.play_music()
        self.initialize_menus()
        self.draw_menus()
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
    def draw_menus(self):
        menu_routes = {
            0: self.main_menu.render,
            1: self.game_over_menu.render,
            2: self.game_mode_menu.render,
            3: self.pause_menu.render,
            4: self.options_menu.render,
            5: self.visuals_menu.render,
            6: self.keys_menu.render,
            7: self.self.sounds_menu.render,
            8: self.menu_AI.render}
        if self.main in menu_routes:menu_routes[self.main]()
    def play_music(self):self.sound_menu.play(loops=-1) if self.config.config_sounds["sound_menu"] else self.sound_menu.stop()
    def sounds_menu(self):
        
        
        
        
        
        on_off_game_over=pygame_gui.elements.UIButton(relative_rect=Rect(220, 240, 50, 40),text=f"{self.config.config_sounds["game_over"]}",object_id="#button_on" if self.config.config_sounds["game_over"] else "#button_off",manager=self.interface.manager,command=lambda:self.on_off(7,self.config.config_sounds,False,"game_over",command=self.config.save_config))
        
        on_off_damage=pygame_gui.elements.UIButton(relative_rect=Rect(220, 280, 50, 40),text=f"{self.config.config_sounds["sound_damage"]}",object_id="#button_on" if self.config.config_sounds["sound_damage"] else "#button_off",manager=self.interface.manager,command=lambda:self.on_off(7,self.config.config_sounds,False,"sound_damage",command=self.config.save_config))
        
        on_off_potion=pygame_gui.elements.UIButton(relative_rect=Rect(220, 320, 50, 40),text=f"{self.config.config_sounds["sound_potion"]}",object_id="#button_on" if self.config.config_sounds["sound_potion"] else "#button_off",manager=self.interface.manager,command=lambda:self.on_off(7,self.config.config_sounds,False,"sound_potion",command=self.config.save_config))
        
        on_off_shield=pygame_gui.elements.UIButton(relative_rect=Rect(220, 360, 50, 40),text=f"{self.config.config_sounds["sound_shield"]}",object_id="#button_on" if self.config.config_sounds["sound_shield"] else "#button_off",manager=self.interface.manager,command=lambda:self.on_off(7,self.config.config_sounds,False,"sound_shield",command=self.config.save_config))
        
        restar_config_sound=pygame_gui.elements.UIButton(relative_rect=Rect(360, 400, 80, 50),text="Press",object_id="#button_on",manager=self.interface.manager,command=lambda:self.more_options([lambda:self.config.config(sounds=True),self.config.save_config,lambda:self.change_mains(7,fade=False)]))
        
    def menu_AI(self):
        self.screen.fill(self.BLACK)
        self.screen.blit(self.font3.render("Config AI", True, "White"),(3,10))
        self.screen.blit(self.font3_5.render(f"Generation Size {self.config.config_AI["generation_value"]}", True, "White"),(10,80))
        increase_generation=pygame_gui.elements.UIButton(relative_rect=Rect(self.WIDTH-60, 80, 50, 40),text='+',manager=self.manager,command=lambda:self.increase_decrease_variable(8,"generation_value",1,dic=self.config.config_AI))
        decrease_generation=pygame_gui.elements.UIButton(relative_rect=Rect(self.WIDTH-120, 80, 50, 40),text='-',manager=self.manager,command=lambda:self.increase_decrease_variable(8,"generation_value",-1,dic=self.config.config_AI)) if self.config.config_AI["generation_value"]>1 else None
        self.screen.blit(self.font3_5.render(f"Population Size {self.config.config_AI["population_value"]}", True, "White"),(10,120))
        increase_population=pygame_gui.elements.UIButton(relative_rect=Rect(self.WIDTH-60, 120, 50, 40),text='+',manager=self.manager,command=lambda:self.increase_decrease_variable(8,"population_value",1,True,dic=self.config.config_AI))
        decrease_population=pygame_gui.elements.UIButton(relative_rect=Rect(self.WIDTH-120, 120, 50, 40),text='-',manager=self.manager,command=lambda:self.increase_decrease_variable(8,"population_value",-1,True,dic=self.config.config_AI)) if self.config.config_AI["population_value"]>1 else None
        self.screen.blit(self.font3_5.render(f"Number of try for AI {self.config.config_AI["try_for_ai"]}", True, "White"),(10,160))
        increase_try_for_ai=pygame_gui.elements.UIButton(relative_rect=Rect(self.WIDTH-60, 160, 50, 40),text='+',manager=self.manager,command=lambda:self.increase_decrease_variable(8,"try_for_ai",1,dic=self.config.config_AI))
        decrease_try_for_ai=pygame_gui.elements.UIButton(relative_rect=Rect(self.WIDTH-120, 160, 50, 40),text='-',manager=self.manager,command=lambda:self.increase_decrease_variable(8,"try_for_ai",-1,dic=self.config.config_AI)) if self.config.config_AI["try_for_ai"]>1 else None
        self.screen.blit(self.font3_5.render(f"Type Training AI", True, "White"),(10,200))
        type_training_ai=pygame_gui.elements.UIButton(relative_rect=Rect(self.WIDTH-120, 200, 110, 50),text="Change",object_id="#button_on",manager=self.manager,command=lambda:self.more_options([lambda:self.change_mains(8,fade=False)]))
        self.screen.blit(self.font3_5.render(f"Type Model", True, "White"),(10,240))
        type_model_ai=pygame_gui.elements.UIButton(relative_rect=Rect(self.WIDTH-120, 240, 110, 50),text="Change",object_id="#button_on",manager=self.manager,command=lambda:self.more_options([lambda:self.change_mains(8,fade=False)]))
        self.screen.blit(self.font3_5.render(f"To Restart Config", True, "White"),(10,280))
        restar_config_ai=pygame_gui.elements.UIButton(relative_rect=Rect(self.WIDTH-120, 280, 110, 50),text="Press",object_id="#button_on",manager=self.manager,command=lambda:self.more_options([lambda:self.config.config(AI=True),self.config.save_config,lambda:self.change_mains(8,fade=False)]))
        play=pygame_gui.elements.UIButton(relative_rect=Rect(self.WIDTH-110, self.HEIGHT-50, 100, 50),text='Play',manager=self.manager,command=lambda:self.change_mains(-1,run=True,command=lambda:self.type_game(mode_one=True),command2=lambda:self.more_options([self.population,lambda:self.on_off_sound(self.sound_menu,"sound_menu",False,game=True)])))
        save=pygame_gui.elements.UIButton(relative_rect=Rect(self.WIDTH-160,10, 150, 50),text=f"Save model {self.config.config_AI["model_save"]}",object_id="#button_on" if self.config.config_AI["model_save"] else "#button_off",manager=self.manager,command=lambda:self.on_off(8,self.config.config_AI,False,"model_save",command=self.config.save_config))
        back_game_menu=pygame_gui.elements.UIButton(relative_rect=Rect(10, self.HEIGHT-50, 100, 50),text='Back',manager=self.manager,command=lambda:self.change_mains(2))
        self.active_buttons.extend([play,save,back_game_menu,increase_generation,decrease_generation,increase_population,decrease_population,increase_try_for_ai,decrease_try_for_ai,restar_config_ai,type_training_ai,type_model_ai])