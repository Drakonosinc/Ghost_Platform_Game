import pygame_gui
from Load_elements import *
class interface(load_elements):
    def __init__(self,width=0, height=0):
        self.WIDTH = width
        self.HEIGHT = height
        super().__init__("Ghost Platform",self.WIDTH,self.HEIGHT)
        self.manager = pygame_gui.UIManager((self.WIDTH,self.HEIGHT),theme_path=os.path.join(self.config_path,"theme_buttons.json"))
        self.main=0 #-1=game, 0=menu, 1=game over, 2=game menu, 3=pausa, 4=options, 5=visuals, 6=menu keys, 7=sound menu, 8=menu AI
        self.active_buttons = []
        self.play_music()
        self.key=None
        self.utils_keys={"up1":False,"up2":False,"left":False,"right":False}
        self.draw_menus()
    def draw_menus(self):
        self.main_menu()
        self.game_over_menu()
        self.mode_game_menu()
        self.pausa_menu()
        self.menu_options()
        self.visuals_menu()
        self.keys_menu()
        self.sounds_menu()
        self.menu_AI()
    def play_music(self):self.sound_menu.play(loops=-1) if self.config_sounds["sound_menu"] else self.sound_menu.stop()
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
    def fade_transition(self,fade_in,color=(0,0,0),limit=255):
        overlay = pygame.Surface((self.WIDTH, self.HEIGHT))
        overlay.fill(color)
        alpha=0
        while not fade_in and alpha <= limit:
            overlay.set_alpha(alpha)
            self.screen.blit(overlay, (0, 0))
            pygame.display.flip()
            self.clock.tick(20)
            alpha += -15 if fade_in else 15
    def change_mains(self,main=0,color=(0,0,0),limit=255,command=None,command2=None,sound=None,run=False,fade=True):
        self.sounds_play(sound=self.sound_touchletters if sound==None else sound)
        if fade:self.fade_transition(False,color,limit)
        self.clear_buttons()
        self.main=main
        self.draw_menus()
        if command!=None:command()
        if command2!=None:command2()
        if run:setattr(self,"running",False),setattr(self, "game_over", True)
    def sounds_play(self,sound,repeat=True):
        if repeat:
            sound.play(loops=0)
            repeat=False
        else:repeat=True
    def type_game(self,mode_one=False,mode_two=False,mode_three=False):
        self.mode_game["Training AI"]=mode_one
        self.mode_game["Player"]=mode_two
        if os.path.exists(self.model_path):self.mode_game["AI"]=mode_three
    def clear_buttons(self):
        try:
            for button in self.active_buttons:button.kill()
            self.active_buttons=[]
        except:
            self.active_buttons=[]
            self.clear_buttons()
    def filt(self,width,height,number,color=(0,0,0),position=(0,0)):
        background=pygame.Surface((width,height),pygame.SRCALPHA)
        background.fill((*color, number))
        self.screen.blit(background,position)
    def on_off(self,main,variable,fade=True,dic=None,command=None):
        if dic is None:setattr(self, variable, not getattr(self, variable))
        else:variable[dic] = not variable[dic]
        self.change_mains(main,fade=fade,command=command)
    def main_menu(self):
        if self.main==0:
            self.screen.fill(self.BLACK)
            self.screen.blit(self.font3.render("Ghost Platform",True,self.WHITE),(3,10))
            self.play_button=pygame_gui.elements.UIButton(relative_rect=Rect(10, 100, 100, 50),text="Play",manager=self.manager)
            self.option_button=pygame_gui.elements.UIButton(relative_rect=Rect(10, 150, 100, 50),text='Option',manager=self.manager)
            self.exit_button=pygame_gui.elements.UIButton(relative_rect=Rect(10, 200, 100, 50),text='Exit',manager=self.manager)
            self.active_buttons.extend([self.play_button, self.option_button, self.exit_button])
    def game_over_menu(self):
        if self.main==1:
            self.filt(self.WIDTH,self.HEIGHT,150,self.RED)
            self.screen.blit(self.font4.render("Game Over", True, self.BLACK),(3,10))
            self.reset_button=pygame_gui.elements.UIButton(relative_rect=Rect(10, 100, 150, 50),text="Press R to Restart",manager=self.manager)
            self.back_button=pygame_gui.elements.UIButton(relative_rect=Rect(10, 150, 150, 50),text='Exit The Menu',manager=self.manager)
            self.exit_button=pygame_gui.elements.UIButton(relative_rect=Rect(10, 200, 150, 50),text='Exit The Game',manager=self.manager)
            self.active_buttons.extend([self.reset_button, self.back_button, self.exit_button])
    def mode_game_menu(self):
        if self.main==2:
            self.screen.fill(self.BLACK)
            self.screen.blit(self.font3.render("Mode Game", True, "White"),(3,10))
            self.training_ai=pygame_gui.elements.UIButton(relative_rect=Rect(10, 100, 100, 50),text='Training AI',manager=self.manager,command=lambda:self.change_mains(8))
            self.mode_player=pygame_gui.elements.UIButton(relative_rect=Rect(10, 150, 100, 50),text='Player',manager=self.manager,command=lambda:self.change_mains(-1,command=lambda:self.type_game(mode_two=True),run=True,command2=lambda:self.more_options(self.population,lambda:self.on_off_sound(self.sound_menu,"sound_menu",False,game=True))))
            self.mode_ai=pygame_gui.elements.UIButton(relative_rect=Rect(10, 200, 100, 50),text='AI',manager=self.manager,command=lambda:self.change_mains(-1,command=lambda:self.type_game(mode_three=True),run=True,command2=lambda:self.more_options(self.population,lambda:self.on_off_sound(self.sound_menu,"sound_menu",False,game=True))))
            back_button=pygame_gui.elements.UIButton(relative_rect=Rect(10, self.HEIGHT-50, 100, 50),text='Back',manager=self.manager,command=lambda:self.change_mains(0))
            self.active_buttons.extend([self.training_ai,self.mode_player,self.mode_ai,back_button])
    def pausa_menu(self):
        if self.main==3:
            self.filt(self.WIDTH,self.HEIGHT,150,self.GRAY)
            self.screen.blit(self.font3.render("Pause", True, "White"),(3,10))
            self.reset_button=pygame_gui.elements.UIButton(relative_rect=Rect(10, 100, 100, 50),text="Reset",manager=self.manager)
            self.option_button=pygame_gui.elements.UIButton(relative_rect=Rect(10, 150, 100, 50),text='Option',manager=self.manager)
            self.back_button=pygame_gui.elements.UIButton(relative_rect=Rect(10, 200, 100, 50),text='Menu',manager=self.manager)
            self.exit_button=pygame_gui.elements.UIButton(relative_rect=Rect(10, 250, 100, 50),text='Exit',manager=self.manager)
            self.active_buttons.extend([self.reset_button, self.option_button, self.back_button,self.exit_button])
    def menu_options(self):
        if self.main==4:
            self.screen.fill(self.BLACK)
            self.screen.blit(self.font3.render("Options", True, "White"),(3,10))
            self.visuals_button=pygame_gui.elements.UIButton(relative_rect=Rect(10, 100, 100, 50),text="Visuals",manager=self.manager)
            self.sounds_button=pygame_gui.elements.UIButton(relative_rect=Rect(10, 150, 100, 50),text='Sounds',manager=self.manager)
            self.keys_button=pygame_gui.elements.UIButton(relative_rect=Rect(10, 200, 100, 50),text='Keys',manager=self.manager)
            back_button=pygame_gui.elements.UIButton(relative_rect=Rect(10, self.HEIGHT-50, 100, 50),text='Back',manager=self.manager,command=lambda:self.change_mains(0))
            self.active_buttons.extend([self.visuals_button,self.sounds_button,self.keys_button,back_button])
    def visuals_menu(self):
        if self.main==5:
            self.screen.fill(self.BLACK)
            self.screen.blit(self.font3.render("Visuals", True, "White"),(3,10))
            self.screen.blit(self.player_ghost,(self.WIDTH/2,self.HEIGHT-50))
            self.screen.blit(self.player_ghost,(self.WIDTH/2,self.HEIGHT-50))
            self.screen.blit(self.player_ghost,(self.WIDTH/2,self.HEIGHT-50))
            self.screen.blit(self.player_ghost,(self.WIDTH/2,self.HEIGHT-50))
            self.screen.blit(self.player_ghost,(self.WIDTH/2,self.HEIGHT-50))
            self.option_button=pygame_gui.elements.UIButton(relative_rect=Rect(10, self.HEIGHT-50, 100, 50),text='Back',manager=self.manager)
            self.active_buttons.extend([self.option_button])
    def keys_menu(self):
        if self.main==6:
            self.screen.fill(self.BLACK)
            self.screen.blit(self.font3.render("Keys", True, "White"),(3,10))
            self.screen.blit(self.font3_5.render(f"Jump One", True, "White"),(10,100))
            key_up1=pygame_gui.elements.UIButton(relative_rect=Rect(220, 100, 50, 50),text=f"{self.config_keys["name_up1"]}",manager=self.manager,object_id="#button_on" if self.utils_keys["up1"] else None,command=lambda:self.change_keys("up1","name_up1"))
            self.screen.blit(self.font3_5.render(f"Jump Two", True, "White"),(10,150))
            key_up2=pygame_gui.elements.UIButton(relative_rect=Rect(220, 150, 50, 50),text=f"{self.config_keys["name_up2"]}",manager=self.manager,object_id="#button_on" if self.utils_keys["up2"] else None,command=lambda:self.change_keys("up2","name_up2"))
            self.screen.blit(self.font3_5.render(f"Move Left", True, "White"),(10,200))
            key_left=pygame_gui.elements.UIButton(relative_rect=Rect(220, 200, 50, 50),text=f"{self.config_keys["name_left"]}",manager=self.manager,object_id="#button_on" if self.utils_keys["left"] else None,command=lambda:self.change_keys("left","name_left"))
            self.screen.blit(self.font3_5.render(f"Move Right", True, "White"),(10,250))
            key_right=pygame_gui.elements.UIButton(relative_rect=Rect(220, 250, 50, 50),text=f"{self.config_keys["name_right"]}",manager=self.manager,object_id="#button_on" if self.utils_keys["right"] else None,command=lambda:self.change_keys("right","name_right"))
            self.screen.blit(self.font3_5.render(f"To Restart Config", True, "White"),(10,300))
            restar_config_key=pygame_gui.elements.UIButton(relative_rect=Rect(360, 300, 80, 50),text="Press",object_id="#button_on",manager=self.manager,command=lambda:self.more_options(command=lambda:self.config(keys=True),command2=self.save_config,command3=lambda:self.change_mains(6,fade=False)))
            self.option_button=pygame_gui.elements.UIButton(relative_rect=Rect(10, self.HEIGHT-50, 100, 50),text='Back',manager=self.manager)
            self.active_buttons.extend([self.option_button,key_up1,key_up2,key_left,key_right,restar_config_key])
    def sounds_menu(self):
        if self.main==7:
            self.screen.fill(self.BLACK)
            self.screen.blit(self.font3.render("Sounds", True, "White"),(3,10))
            sound_menu=pygame_gui.elements.UIButton(relative_rect=Rect(10, 100, 125, 50),text=f"Sound Menu {"ON" if self.config_sounds["sound_menu"] else "OFF"}",object_id="#button_on" if self.config_sounds["sound_menu"] else "#button_off",manager=self.manager,command=lambda:self.on_off(7,self.config_sounds,False,"sound_menu",command=lambda:self.on_off_sound(self.sound_menu,"sound_menu",True,command=True)))
            sound_game=pygame_gui.elements.UIButton(relative_rect=Rect(10, 150, 125, 50),text=f"Sound Game {"ON" if self.config_sounds["sound_game"] else "OFF"}",object_id="#button_on" if self.config_sounds["sound_game"] else "#button_off",manager=self.manager,command=lambda:self.on_off(7,self.config_sounds,False,"sound_game",command=lambda:self.on_off_sound(self.sound_game,"sound_game",False,command=True)))
            self.screen.blit(self.font3_5.render(f"Sound Jump", True, "White"),(10,200))
            on_off_jump=pygame_gui.elements.UIButton(relative_rect=Rect(220, 200, 50, 40),text=f"{self.config_sounds["sound_jump"]}",object_id="#button_on" if self.config_sounds["sound_jump"] else "#button_off",manager=self.manager,command=lambda:self.on_off(7,self.config_sounds,False,"sound_jump",command=self.save_config))
            self.screen.blit(self.font3_5.render(f"Game Over", True, "White"),(10,240))
            on_off_game_over=pygame_gui.elements.UIButton(relative_rect=Rect(220, 240, 50, 40),text=f"{self.config_sounds["game_over"]}",object_id="#button_on" if self.config_sounds["game_over"] else "#button_off",manager=self.manager,command=lambda:self.on_off(7,self.config_sounds,False,"game_over",command=self.save_config))
            self.screen.blit(self.font3_5.render(f"Damage", True, "White"),(10,280))
            on_off_damage=pygame_gui.elements.UIButton(relative_rect=Rect(220, 280, 50, 40),text=f"{self.config_sounds["sound_damage"]}",object_id="#button_on" if self.config_sounds["sound_damage"] else "#button_off",manager=self.manager,command=lambda:self.on_off(7,self.config_sounds,False,"sound_damage",command=self.save_config))
            self.screen.blit(self.font3_5.render(f"Potion", True, "White"),(10,320))
            on_off_potion=pygame_gui.elements.UIButton(relative_rect=Rect(220, 320, 50, 40),text=f"{self.config_sounds["sound_potion"]}",object_id="#button_on" if self.config_sounds["sound_potion"] else "#button_off",manager=self.manager,command=lambda:self.on_off(7,self.config_sounds,False,"sound_potion",command=self.save_config))
            self.screen.blit(self.font3_5.render(f"Shield", True, "White"),(10,360))
            on_off_shield=pygame_gui.elements.UIButton(relative_rect=Rect(220, 360, 50, 40),text=f"{self.config_sounds["sound_shield"]}",object_id="#button_on" if self.config_sounds["sound_shield"] else "#button_off",manager=self.manager,command=lambda:self.on_off(7,self.config_sounds,False,"sound_shield",command=self.save_config))
            self.screen.blit(self.font3_5.render(f"To Restart Config", True, "White"),(10,400))
            restar_config_sound=pygame_gui.elements.UIButton(relative_rect=Rect(360, 400, 80, 50),text="Press",object_id="#button_on",manager=self.manager,command=lambda:self.more_options(command=lambda:self.config(sounds=True),command2=self.save_config,command3=lambda:self.change_mains(7,fade=False)))
            self.option_button=pygame_gui.elements.UIButton(relative_rect=Rect(10, self.HEIGHT-50, 100, 50),text='Back',manager=self.manager)
            self.active_buttons.extend([self.option_button,sound_menu,sound_game,on_off_jump,on_off_game_over,on_off_damage,on_off_potion,on_off_shield,restar_config_sound])
    def menu_AI(self):
        if self.main==8:
            self.screen.fill(self.BLACK)
            self.screen.blit(self.font3.render("Config AI", True, "White"),(3,10))
            self.screen.blit(self.font3_5.render(f"Generation Size {self.config_AI["generation_value"]}", True, "White"),(10,80))
            increase_generation=pygame_gui.elements.UIButton(relative_rect=Rect(self.WIDTH-60, 80, 50, 40),text='+',manager=self.manager,command=lambda:self.increase_decrease_variable("generation_value",1,dic=self.config_AI))
            decrease_generation=pygame_gui.elements.UIButton(relative_rect=Rect(self.WIDTH-120, 80, 50, 40),text='-',manager=self.manager,command=lambda:self.increase_decrease_variable("generation_value",-1,dic=self.config_AI)) if self.config_AI["generation_value"]>1 else None
            self.screen.blit(self.font3_5.render(f"Population Size {self.config_AI["population_value"]}", True, "White"),(10,120))
            increase_population=pygame_gui.elements.UIButton(relative_rect=Rect(self.WIDTH-60, 120, 50, 40),text='+',manager=self.manager,command=lambda:self.increase_decrease_variable("population_value",1,True,dic=self.config_AI))
            decrease_population=pygame_gui.elements.UIButton(relative_rect=Rect(self.WIDTH-120, 120, 50, 40),text='-',manager=self.manager,command=lambda:self.increase_decrease_variable("population_value",-1,True,dic=self.config_AI)) if self.config_AI["population_value"]>1 else None
            self.screen.blit(self.font3_5.render(f"Number of try for AI {self.config_AI["try_for_ai"]}", True, "White"),(10,160))
            increase_try_for_ai=pygame_gui.elements.UIButton(relative_rect=Rect(self.WIDTH-60, 160, 50, 40),text='+',manager=self.manager,command=lambda:self.increase_decrease_variable("try_for_ai",1,dic=self.config_AI))
            decrease_try_for_ai=pygame_gui.elements.UIButton(relative_rect=Rect(self.WIDTH-120, 160, 50, 40),text='-',manager=self.manager,command=lambda:self.increase_decrease_variable("try_for_ai",-1,dic=self.config_AI)) if self.config_AI["try_for_ai"]>1 else None
            self.screen.blit(self.font3_5.render(f"To Restart Config", True, "White"),(10,200))
            restar_config_ai=pygame_gui.elements.UIButton(relative_rect=Rect(self.WIDTH-120, 200, 110, 50),text="Press",object_id="#button_on",manager=self.manager,command=lambda:self.more_options(command=lambda:self.config(AI=True),command2=self.save_config,command3=lambda:self.change_mains(8,fade=False)))
            play=pygame_gui.elements.UIButton(relative_rect=Rect(self.WIDTH-110, self.HEIGHT-50, 100, 50),text='Play',manager=self.manager,command=lambda:self.change_mains(-1,run=True,command=lambda:self.type_game(mode_one=True),command2=lambda:self.more_options(self.population,lambda:self.on_off_sound(self.sound_menu,"sound_menu",False,game=True))))
            save=pygame_gui.elements.UIButton(relative_rect=Rect(self.WIDTH-160,10, 150, 50),text=f"Save model {self.config_AI["model_save"]}",object_id="#button_on" if self.config_AI["model_save"] else "#button_off",manager=self.manager,command=lambda:self.on_off(8,self.config_AI,False,"model_save",command=self.save_config))
            back_game_menu=pygame_gui.elements.UIButton(relative_rect=Rect(10, self.HEIGHT-50, 100, 50),text='Back',manager=self.manager,command=lambda:self.change_mains(2))
            self.active_buttons.extend([play,save,back_game_menu,increase_generation,decrease_generation,increase_population,decrease_population,increase_try_for_ai,decrease_try_for_ai,restar_config_ai])
    def increase_decrease_variable(self,variable,number,population=False,fade=False,dic=None):
        if dic!=None:dic[variable]+=number
        else:setattr(self,variable,getattr(self,variable)+number)
        self.change_mains(8,fade=fade),self.save_config()
        if population:self.population()
    def on_off_sound(self,sound,type_sound,play=True,game=False,command=False):
        sound.play(loops=-1) if play and self.config_sounds[type_sound] else sound.stop()
        if game:self.on_off_sound(self.sound_game,"sound_game")
        if command:self.save_config()
    def more_options(self,command=False,command2=False,command3=False):
        if command:command()
        if command2:command2()
        if command3:command3()
    def change_keys(self,key,key_name):
        self.key=key
        self.key_name=key_name
        for k in self.utils_keys.keys():self.utils_keys[k]=False if k!=self.key else not self.utils_keys[self.key]
        self.change_mains(6,fade=False)
    def event_change_keys(self,event):
        if self.key!=None and (self.utils_keys[self.key] and event.type==KEYDOWN):
            self.config_keys[self.key]=event.key
            self.config_keys[self.key_name]=event.unicode.upper() if self.config_keys[self.key]!=32 else "Space"
            self.utils_keys[self.key]= not self.utils_keys[self.key]
            self.change_mains(6,fade=False),self.save_config()