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
        self.key=None
        self.utils_keys:dict[str, bool]={"up1":False,"up2":False,"left":False,"right":False}
        self.initialize_menus()
        self.draw_menus()
    def initialize_menus(self):
        self.main_menu = MainMenu(self)
    def draw_menus(self):
        if self.main==0:self.main_menu()
        elif self.main==1:self.game_over_menu()
        elif self.main==2:self.mode_game_menu()
        elif self.main==3:self.pausa_menu()
        elif self.main==4:self.menu_options()
        elif self.main==5:self.visuals_menu()
        elif self.main==6:self.keys_menu()
        elif self.main==7:self.sounds_menu()
        elif self.main==8:self.menu_AI()
    def play_music(self):self.sound_menu.play(loops=-1) if self.config.config_sounds["sound_menu"] else self.sound_menu.stop()
    def event_buttons(self,event):
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if hasattr(event, 'ui_element'):
                if self.main!=-1:self.buttons_repetitive(event)
                if self.main==0:self.buttons_main_menu(event)
                if self.main==4:self.buttons_options_menu(event)
    def buttons_repetitive(self,event):
        if (self.main==1 or self.main==3) and event.ui_element == self.back_button:self.change_mains(0,command=self.type_game,command2=lambda:[self.on_off_sound(x,y,False) for x,y in zip([self.sound_menu,self.sound_game],["sound_menu","sound_game"])],run=True)
        if (self.main!=2 and self.main!=4) and event.ui_element == self.option_button:self.change_mains(4)
        if (self.main!=2 and self.main!=4) and event.ui_element == self.exit_button:self.change_mains(command=self.close_game,sound=self.sound_exit)
        if (self.main!=0 and self.main!=4) and event.ui_element == self.reset_button:self.change_mains(-1,command=self.reset)
    def buttons_main_menu(self,event):
        if event.ui_element == self.play_button:self.change_mains(2)
    def buttons_options_menu(self,event):
        if event.ui_element == self.visuals_button:self.change_mains(5)
        if event.ui_element == self.sounds_button:self.change_mains(7)
        if event.ui_element == self.keys_button:self.change_mains(6)
    def main_menu(self):
        self.option_button=pygame_gui.elements.UIButton(relative_rect=Rect(10, 150, 100, 50),text='Option',manager=self.manager)
        self.exit_button=pygame_gui.elements.UIButton(relative_rect=Rect(10, 200, 100, 50),text='Exit',manager=self.manager)
        self.active_buttons.extend([self.play_button, self.option_button, self.exit_button])
    def game_over_menu(self):
        self.filt(self.WIDTH,self.HEIGHT,150,self.RED)
        self.screen.blit(self.font4.render("Game Over", True, self.BLACK),(3,10))
        self.reset_button=pygame_gui.elements.UIButton(relative_rect=Rect(10, 100, 150, 50),text="Press R to Restart",manager=self.manager)
        self.back_button=pygame_gui.elements.UIButton(relative_rect=Rect(10, 150, 150, 50),text='Exit The Menu',manager=self.manager)
        self.exit_button=pygame_gui.elements.UIButton(relative_rect=Rect(10, 200, 150, 50),text='Exit The Game',manager=self.manager)
        self.active_buttons.extend([self.reset_button, self.back_button, self.exit_button])
    def mode_game_menu(self):
        self.screen.fill(self.BLACK)
        self.screen.blit(self.font3.render("Mode Game", True, "White"),(3,10))
        self.training_ai=pygame_gui.elements.UIButton(relative_rect=Rect(10, 100, 100, 50),text='Training AI',manager=self.manager,command=lambda:self.change_mains(8))
        self.mode_player=pygame_gui.elements.UIButton(relative_rect=Rect(10, 150, 100, 50),text='Player',manager=self.manager,command=lambda:self.change_mains(-1,command=lambda:self.type_game(mode_two=True),run=True,command2=lambda:self.more_options([self.population,lambda:self.on_off_sound(self.sound_menu,"sound_menu",False,game=True)])))
        self.mode_ai=pygame_gui.elements.UIButton(relative_rect=Rect(10, 200, 100, 50),text='AI',manager=self.manager,command=lambda:self.change_mains(-1,command=lambda:self.type_game(mode_three=True),run=True,command2=lambda:self.more_options([self.population,lambda:self.on_off_sound(self.sound_menu,"sound_menu",False,game=True)])))
        back_button=pygame_gui.elements.UIButton(relative_rect=Rect(10, self.HEIGHT-50, 100, 50),text='Back',manager=self.manager,command=lambda:self.change_mains(0))
        self.active_buttons.extend([self.training_ai,self.mode_player,self.mode_ai,back_button])
    def pausa_menu(self):
        self.filt(self.WIDTH,self.HEIGHT,150,self.GRAY)
        self.screen.blit(self.font3.render("Pause", True, "White"),(3,10))
        self.reset_button=pygame_gui.elements.UIButton(relative_rect=Rect(10, 100, 100, 50),text="Reset",manager=self.manager)
        self.option_button=pygame_gui.elements.UIButton(relative_rect=Rect(10, 150, 100, 50),text='Option',manager=self.manager)
        self.back_button=pygame_gui.elements.UIButton(relative_rect=Rect(10, 200, 100, 50),text='Menu',manager=self.manager)
        self.exit_button=pygame_gui.elements.UIButton(relative_rect=Rect(10, 250, 100, 50),text='Exit',manager=self.manager)
        self.active_buttons.extend([self.reset_button, self.option_button, self.back_button,self.exit_button])
    def menu_options(self):
        self.screen.fill(self.BLACK)
        self.screen.blit(self.font3.render("Options", True, "White"),(3,10))
        self.visuals_button=pygame_gui.elements.UIButton(relative_rect=Rect(10, 100, 100, 50),text="Visuals",manager=self.manager)
        self.sounds_button=pygame_gui.elements.UIButton(relative_rect=Rect(10, 150, 100, 50),text='Sounds',manager=self.manager)
        self.keys_button=pygame_gui.elements.UIButton(relative_rect=Rect(10, 200, 100, 50),text='Keys',manager=self.manager)
        back_button=pygame_gui.elements.UIButton(relative_rect=Rect(10, self.HEIGHT-50, 100, 50),text='Back',manager=self.manager,command=lambda:self.change_mains(0))
        self.active_buttons.extend([self.visuals_button,self.sounds_button,self.keys_button,back_button])
    def visuals_menu(self):
        self.screen.fill(self.BLACK)
        self.screen.blit(self.font3.render("Visuals", True, "White"),(3,10))
        self.screen.blit(self.floor,(150,100))
        increase_floor=pygame_gui.elements.UIButton(relative_rect=Rect(290, 100, 50, 40),text='>',manager=self.manager,command=lambda:self.increase_decrease_variable(5,"floor_value",1,dic=self.config.config_visuals,length="floor",command=self.load_images,recu=True))
        decrease_floor=pygame_gui.elements.UIButton(relative_rect=Rect(10, 100, 50, 40),text='<',manager=self.manager,command=lambda:self.increase_decrease_variable(5,"floor_value",-1,dic=self.config.config_visuals,length="floor",command=self.load_images,recu=True))
        self.screen.blit(self.meteorite,(150,150))
        increase_meteorite=pygame_gui.elements.UIButton(relative_rect=Rect(290, 200, 50, 40),text='>',manager=self.manager,command=lambda:self.increase_decrease_variable(5,"meteorite_value",1,dic=self.config.config_visuals,length="meteorite",command=self.load_images,recu=True))
        decrease_meteorite=pygame_gui.elements.UIButton(relative_rect=Rect(10, 200, 50, 40),text='<',manager=self.manager,command=lambda:self.increase_decrease_variable(5,"meteorite_value",-1,dic=self.config.config_visuals,length="meteorite",command=self.load_images,recu=True))
        self.screen.blit(self.potion,(150,300))
        increase_potion=pygame_gui.elements.UIButton(relative_rect=Rect(290, 300, 50, 40),text='>',manager=self.manager,command=lambda:self.increase_decrease_variable(5,"potion_value",1,dic=self.config.config_visuals,length="potion",command=self.load_images,recu=True))
        decrease_potion=pygame_gui.elements.UIButton(relative_rect=Rect(10, 300, 50, 40),text='<',manager=self.manager,command=lambda:self.increase_decrease_variable(5,"potion_value",-1,dic=self.config.config_visuals,length="potion",command=self.load_images,recu=True))
        self.screen.blit(self.shield,(150,400))
        increase_shield=pygame_gui.elements.UIButton(relative_rect=Rect(290, 400, 50, 40),text='>',manager=self.manager,command=lambda:self.increase_decrease_variable(5,"shield_value",1,dic=self.config.config_visuals,length="shield",command=self.load_images,recu=True))
        decrease_shield=pygame_gui.elements.UIButton(relative_rect=Rect(10, 400, 50, 40),text='<',manager=self.manager,command=lambda:self.increase_decrease_variable(5,"shield_value",-1,dic=self.config.config_visuals,length="shield",command=self.load_images,recu=True))
        self.screen.blit(self.player_ghost,(150,500))
        increase_player=pygame_gui.elements.UIButton(relative_rect=Rect(290, 500, 50, 40),text='>',manager=self.manager,command=lambda:self.increase_decrease_variable(5,"player_value",1,dic=self.config.config_visuals,length="player",command=self.load_images,recu=True))
        decrease_player=pygame_gui.elements.UIButton(relative_rect=Rect(10, 500, 50, 40),text='<',manager=self.manager,command=lambda:self.increase_decrease_variable(5,"player_value",-1,dic=self.config.config_visuals,length="player",command=self.load_images,recu=True))
        self.option_button=pygame_gui.elements.UIButton(relative_rect=Rect(10, self.HEIGHT-50, 100, 50),text='Back',manager=self.manager)
        self.active_buttons.extend([self.option_button,increase_floor,decrease_floor,increase_meteorite,decrease_meteorite,increase_potion,decrease_potion,increase_shield,decrease_shield,increase_player,decrease_player])
    def keys_menu(self):
        self.screen.fill(self.BLACK)
        self.screen.blit(self.font3.render("Keys", True, "White"),(3,10))
        self.screen.blit(self.font3_5.render(f"Jump One", True, "White"),(10,100))
        key_up1=pygame_gui.elements.UIButton(relative_rect=Rect(220, 100, 50, 50),text=f"{self.config.config_keys["name_up1"]}",manager=self.manager,object_id="#button_on" if self.utils_keys["up1"] else None,command=lambda:self.change_keys("up1","name_up1"))
        self.screen.blit(self.font3_5.render(f"Jump Two", True, "White"),(10,150))
        key_up2=pygame_gui.elements.UIButton(relative_rect=Rect(220, 150, 50, 50),text=f"{self.config.config_keys["name_up2"]}",manager=self.manager,object_id="#button_on" if self.utils_keys["up2"] else None,command=lambda:self.change_keys("up2","name_up2"))
        self.screen.blit(self.font3_5.render(f"Move Left", True, "White"),(10,200))
        key_left=pygame_gui.elements.UIButton(relative_rect=Rect(220, 200, 50, 50),text=f"{self.config.config_keys["name_left"]}",manager=self.manager,object_id="#button_on" if self.utils_keys["left"] else None,command=lambda:self.change_keys("left","name_left"))
        self.screen.blit(self.font3_5.render(f"Move Right", True, "White"),(10,250))
        key_right=pygame_gui.elements.UIButton(relative_rect=Rect(220, 250, 50, 50),text=f"{self.config.config_keys["name_right"]}",manager=self.manager,object_id="#button_on" if self.utils_keys["right"] else None,command=lambda:self.change_keys("right","name_right"))
        self.screen.blit(self.font3_5.render(f"To Restart Config", True, "White"),(10,300))
        restar_config_key=pygame_gui.elements.UIButton(relative_rect=Rect(360, 300, 80, 50),text="Press",object_id="#button_on",manager=self.manager,command=lambda:self.more_options([lambda:self.config.config(keys=True),self.config.save_config,lambda:self.change_mains(6,fade=False)]))
        self.option_button=pygame_gui.elements.UIButton(relative_rect=Rect(10, self.HEIGHT-50, 100, 50),text='Back',manager=self.manager)
        self.active_buttons.extend([self.option_button,key_up1,key_up2,key_left,key_right,restar_config_key])
    def sounds_menu(self):
        self.screen.fill(self.BLACK)
        self.screen.blit(self.font3.render("Sounds", True, "White"),(3,10))
        sound_menu=pygame_gui.elements.UIButton(relative_rect=Rect(10, 100, 125, 50),text=f"Sound Menu {"ON" if self.config.config_sounds["sound_menu"] else "OFF"}",object_id="#button_on" if self.config.config_sounds["sound_menu"] else "#button_off",manager=self.manager,command=lambda:self.on_off(7,self.config.config_sounds,False,"sound_menu",command=lambda:self.on_off_sound(self.sound_menu,"sound_menu",True,command=True)))
        sound_game=pygame_gui.elements.UIButton(relative_rect=Rect(10, 150, 125, 50),text=f"Sound Game {"ON" if self.config.config_sounds["sound_game"] else "OFF"}",object_id="#button_on" if self.config.config_sounds["sound_game"] else "#button_off",manager=self.manager,command=lambda:self.on_off(7,self.config.config_sounds,False,"sound_game",command=lambda:self.on_off_sound(self.sound_game,"sound_game",False,command=True)))
        self.screen.blit(self.font3_5.render(f"Sound Jump", True, "White"),(10,200))
        on_off_jump=pygame_gui.elements.UIButton(relative_rect=Rect(220, 200, 50, 40),text=f"{self.config.config_sounds["sound_jump"]}",object_id="#button_on" if self.config.config_sounds["sound_jump"] else "#button_off",manager=self.manager,command=lambda:self.on_off(7,self.config.config_sounds,False,"sound_jump",command=self.config.save_config))
        self.screen.blit(self.font3_5.render(f"Game Over", True, "White"),(10,240))
        on_off_game_over=pygame_gui.elements.UIButton(relative_rect=Rect(220, 240, 50, 40),text=f"{self.config.config_sounds["game_over"]}",object_id="#button_on" if self.config.config_sounds["game_over"] else "#button_off",manager=self.manager,command=lambda:self.on_off(7,self.config.config_sounds,False,"game_over",command=self.config.save_config))
        self.screen.blit(self.font3_5.render(f"Damage", True, "White"),(10,280))
        on_off_damage=pygame_gui.elements.UIButton(relative_rect=Rect(220, 280, 50, 40),text=f"{self.config.config_sounds["sound_damage"]}",object_id="#button_on" if self.config.config_sounds["sound_damage"] else "#button_off",manager=self.manager,command=lambda:self.on_off(7,self.config.config_sounds,False,"sound_damage",command=self.config.save_config))
        self.screen.blit(self.font3_5.render(f"Potion", True, "White"),(10,320))
        on_off_potion=pygame_gui.elements.UIButton(relative_rect=Rect(220, 320, 50, 40),text=f"{self.config.config_sounds["sound_potion"]}",object_id="#button_on" if self.config.config_sounds["sound_potion"] else "#button_off",manager=self.manager,command=lambda:self.on_off(7,self.config.config_sounds,False,"sound_potion",command=self.config.save_config))
        self.screen.blit(self.font3_5.render(f"Shield", True, "White"),(10,360))
        on_off_shield=pygame_gui.elements.UIButton(relative_rect=Rect(220, 360, 50, 40),text=f"{self.config.config_sounds["sound_shield"]}",object_id="#button_on" if self.config.config_sounds["sound_shield"] else "#button_off",manager=self.manager,command=lambda:self.on_off(7,self.config.config_sounds,False,"sound_shield",command=self.config.save_config))
        self.screen.blit(self.font3_5.render(f"To Restart Config", True, "White"),(10,400))
        restar_config_sound=pygame_gui.elements.UIButton(relative_rect=Rect(360, 400, 80, 50),text="Press",object_id="#button_on",manager=self.manager,command=lambda:self.more_options([lambda:self.config.config(sounds=True),self.config.save_config,lambda:self.change_mains(7,fade=False)]))
        self.option_button=pygame_gui.elements.UIButton(relative_rect=Rect(10, self.HEIGHT-50, 100, 50),text='Back',manager=self.manager)
        self.active_buttons.extend([self.option_button,sound_menu,sound_game,on_off_jump,on_off_game_over,on_off_damage,on_off_potion,on_off_shield,restar_config_sound])
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
    def on_off_sound(self,sound,type_sound,play=True,game=False,command=False):
        sound.play(loops=-1) if play and self.config.config_sounds[type_sound] else sound.stop()
        if game:self.on_off_sound(self.sound_game,"sound_game")
        if command:self.config.save_config()
    def change_keys(self,key,key_name):
        self.key=key
        self.key_name=key_name
        for k in self.utils_keys.keys():self.utils_keys[k]=False if k!=self.key else not self.utils_keys[self.key]
        self.change_mains(6,fade=False)
    def event_change_keys(self,event):
        if self.key!=None and (self.utils_keys[self.key] and event.type==KEYDOWN):
            self.config.config_keys[self.key]=event.key
            self.config.config_keys[self.key_name]=event.unicode.upper() if self.config.config_keys[self.key]!=32 else "Space"
            self.utils_keys[self.key]= not self.utils_keys[self.key]
            self.change_mains(6,fade=False),self.config.save_config()