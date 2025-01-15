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
        self.generation_value=100
        self.population_value=20
        self.model_save=False
        self.try_for_ai=3
        self.sounds={"sound menu":True,"sound game":True}
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
        self.change_sounds(*(self.sound_game,self.sounds["sound game"]) if self.main==-1 else (self.sound_menu,self.sounds["sound menu"]))
    def event_buttons(self,event):
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if hasattr(event, 'ui_element'):
                if self.main!=-1:self.buttons_repetitive(event)
                if self.main==0:self.buttons_main_menu(event)
                if self.main==4:self.buttons_options_menu(event)
    def buttons_repetitive(self,event):
        if self.main!=0 and event.ui_element == self.back_button:self.change_mains(0,command=self.type_game,run=True)
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
    def on_off(self,main,variable,fade=True,dic=None,command=False):
        if dic is None:setattr(self, variable, not getattr(self, variable))
        else:
            if isinstance(getattr(self, variable), dict):
                current_dict = getattr(self, variable)
                current_dict[dic] = not current_dict[dic]
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
            self.mode_player=pygame_gui.elements.UIButton(relative_rect=Rect(10, 150, 100, 50),text='Player',manager=self.manager,command=lambda:self.change_mains(-1,command=lambda:self.type_game(mode_two=True),run=True,command2=self.population))
            self.mode_ai=pygame_gui.elements.UIButton(relative_rect=Rect(10, 200, 100, 50),text='AI',manager=self.manager,command=lambda:self.change_mains(-1,command=lambda:self.type_game(mode_three=True),run=True,command2=self.population))
            self.back_button=pygame_gui.elements.UIButton(relative_rect=Rect(10, self.HEIGHT-50, 100, 50),text='Back',manager=self.manager)
            self.active_buttons.extend([self.training_ai,self.mode_player,self.mode_ai,self.back_button])
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
            self.back_button=pygame_gui.elements.UIButton(relative_rect=Rect(10, self.HEIGHT-50, 100, 50),text='Back',manager=self.manager)
            self.active_buttons.extend([self.visuals_button,self.sounds_button,self.keys_button,self.back_button])
    def visuals_menu(self):
        if self.main==5:
            self.screen.fill(self.BLACK)
            self.screen.blit(self.font3.render("Visuals", True, "White"),(3,10))
            self.option_button=pygame_gui.elements.UIButton(relative_rect=Rect(10, self.HEIGHT-50, 100, 50),text='Back',manager=self.manager)
            self.active_buttons.extend([self.option_button])
    def keys_menu(self):
        if self.main==6:
            self.screen.fill(self.BLACK)
            self.screen.blit(self.font3.render("Keys", True, "White"),(3,10))
            self.option_button=pygame_gui.elements.UIButton(relative_rect=Rect(10, self.HEIGHT-50, 100, 50),text='Back',manager=self.manager)
            self.active_buttons.extend([self.option_button])
    def sounds_menu(self):
        if self.main==7:
            self.screen.fill(self.BLACK)
            self.screen.blit(self.font3.render("Sounds", True, "White"),(3,10))
            sound_menu=pygame_gui.elements.UIButton(relative_rect=Rect(10, 100, 125, 50),text=f"Sound Menu {"ON" if self.sounds["sound menu"] else "OFF"}",object_id="#button_on" if self.sounds["sound menu"] else "#button_off",manager=self.manager,command=lambda:self.on_off(7,"sounds",fade=False,dic="sound menu",command=self.change_sounds(self.sound_menu,self.sounds["sound menu"])))
            sound_game=pygame_gui.elements.UIButton(relative_rect=Rect(10, 150, 125, 50),text=f"Sound Game {"ON" if self.sounds["sound game"] else "OFF"}",object_id="#button_on" if self.sounds["sound game"] else "#button_off",manager=self.manager,command=lambda:self.on_off(7,"sounds",fade=False,dic="sound game",command=self.change_sounds(self.sound_game,self.sounds["sound game"])))
            self.option_button=pygame_gui.elements.UIButton(relative_rect=Rect(10, self.HEIGHT-50, 100, 50),text='Back',manager=self.manager)
            self.active_buttons.extend([self.option_button,sound_menu,sound_game])
    def menu_AI(self):
        if self.main==8:
            self.screen.fill(self.BLACK)
            self.screen.blit(self.font3.render("Config AI", True, "White"),(3,10))
            self.screen.blit(self.font3_5.render(f"Generation Size {self.generation_value}", True, "White"),(10,80))
            increase_generation=pygame_gui.elements.UIButton(relative_rect=Rect(self.WIDTH-60, 80, 50, 40),text='+',manager=self.manager,command=lambda:self.increase_decrease_variable("generation_value",1))
            decrease_generation=pygame_gui.elements.UIButton(relative_rect=Rect(self.WIDTH-120, 80, 50, 40),text='-',manager=self.manager,command=lambda:self.increase_decrease_variable("generation_value",-1)) if self.generation_value>1 else None
            self.screen.blit(self.font3_5.render(f"Population Size {self.population_value}", True, "White"),(10,120))
            increase_population=pygame_gui.elements.UIButton(relative_rect=Rect(self.WIDTH-60, 120, 50, 40),text='+',manager=self.manager,command=lambda:self.increase_decrease_variable("population_value",1,True))
            decrease_population=pygame_gui.elements.UIButton(relative_rect=Rect(self.WIDTH-120, 120, 50, 40),text='-',manager=self.manager,command=lambda:self.increase_decrease_variable("population_value",-1,True)) if self.population_value>1 else None
            self.screen.blit(self.font3_5.render(f"Number of try for AI {self.try_for_ai}", True, "White"),(10,160))
            increase_try_for_ai=pygame_gui.elements.UIButton(relative_rect=Rect(self.WIDTH-60, 160, 50, 40),text='+',manager=self.manager,command=lambda:self.increase_decrease_variable("try_for_ai",1))
            decrease_try_for_ai=pygame_gui.elements.UIButton(relative_rect=Rect(self.WIDTH-120, 160, 50, 40),text='-',manager=self.manager,command=lambda:self.increase_decrease_variable("try_for_ai",-1)) if self.try_for_ai>1 else None
            self.play=pygame_gui.elements.UIButton(relative_rect=Rect(self.WIDTH-110, self.HEIGHT-50, 100, 50),text='Play',manager=self.manager,command=lambda:self.change_mains(-1,run=True,command=lambda:self.type_game(mode_one=True),command2=self.population))
            self.save=pygame_gui.elements.UIButton(relative_rect=Rect(self.WIDTH-160,10, 150, 50),text=f"Save model {self.model_save}",object_id="#button_on" if self.model_save else "#button_off",manager=self.manager,command=lambda:self.on_off(8,"model_save",fade=False))
            self.back_game_menu=pygame_gui.elements.UIButton(relative_rect=Rect(10, self.HEIGHT-50, 100, 50),text='Back',manager=self.manager,command=lambda:self.change_mains(2))
            self.active_buttons.extend([self.play,self.save,self.back_game_menu,increase_generation,decrease_generation,increase_population,decrease_population,increase_try_for_ai,decrease_try_for_ai])
    def increase_decrease_variable(self,variable,number,population=False,fade=False):
        setattr(self,variable,getattr(self,variable)+number)
        self.change_mains(8,fade=fade)
        if population:self.population()
    def change_sounds(self,sound,type_sound):sound.play(loops=-1) if type_sound else sound.stop()