import pygame, os, pygame_gui
class BaseMenu:
    def __init__(self, interface=None):
        self.interface = interface
        if interface:
            self.screen = interface.screen
            self.WIDTH = interface.WIDTH
            self.HEIGHT = interface.HEIGHT
            self.config = interface.config
    def fade_transition(self,fade_in,color=(0,0,0),limit=255):
        overlay = pygame.Surface((self.WIDTH, self.HEIGHT))
        overlay.fill(color)
        alpha=0
        while not fade_in and alpha <= limit:
            overlay.set_alpha(alpha)
            self.screen.blit(overlay, (0, 0))
            pygame.display.flip()
            self.interface.clock.tick(20)
            alpha += -15 if fade_in else 15
    def change_mains(self,main=0,color=(0,0,0),limit=255,command=None,command2=None,sound=None,run=False,fade=True,recursive=False):
        self.sounds_play(sound=self.interface.sound_touchletters if sound==None else sound)
        if fade:self.fade_transition(False,color,limit)
        self.clear_buttons()
        self.interface.main=main
        self.interface.draw_menus()
        if command!=None:command()
        if command2!=None:command2()
        if recursive:self.change_mains(main,fade=fade)
        if run:setattr(self,"running",False),setattr(self, "game_over", True)
    def sounds_play(self,sound,repeat=True):
        if repeat:
            sound.play(loops=0)
            repeat=False
        else:repeat=True
    def clear_buttons(self):
        try:
            for button in self.interface.active_buttons:button.kill()
            self.interface.active_buttons=[]
        except:
            self.interface.active_buttons=[]
            self.clear_buttons()
    def filt(self,width,height,number,color=(0,0,0),position=(0,0)):
        background=pygame.Surface((width,height),pygame.SRCALPHA)
        background.fill((*color, number))
        self.screen.blit(background,position)
    def on_off(self,main,variable,fade=True,dic=None,command=None):
        if dic is None:setattr(self, variable, not getattr(self, variable))
        else:variable[dic] = not variable[dic]
        self.change_mains(main,fade=fade,command=command)
    def increase_decrease_variable(self,main,variable,number,population=False,fade=False,dic=None,length=None,command=None,recu=False):
        if dic!=None and length!=None:dic[variable]=((dic[variable] + number) % len(dic[length]))
        elif dic!=None:dic[variable]+=number
        else:setattr(self,variable,getattr(self,variable)+number)
        self.change_mains(main=main,fade=fade,command=self.config.save_config,command2=command,recursive=recu)
        if population:self.interface.population()
    def more_options(self,command=[]):
        try:
            for command in command:
                if callable(command):command()
        except TypeError:return None
    def type_game(self,mode_one=False,mode_two=False,mode_three=False):
        self.mode_game["Training AI"]=mode_one
        self.mode_game["Player"]=mode_two
        if os.path.exists(self.model_path):self.mode_game["AI"]=mode_three