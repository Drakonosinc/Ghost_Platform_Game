import pygame, os
class BaseMenu:
    def __init__(self, interface=None):
        self.interface = interface
        if interface:
            self.screen = interface.screen
            self.WIDTH = interface.WIDTH
            self.HEIGHT = interface.HEIGHT
            self.config = interface.config
    def check_item(self,dic,is_true,is_false,item,**kwargs):
        for key,button in kwargs.items():button.change_item({item:(is_true if dic[key] else is_false)})
    def execute_buttons(self,*args):
        for button in args:
            if button is not None:
                button.draw()
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
        self.interface.main=main
        if command!=None:command()
        if command2!=None:command2()
        if recursive:self.change_mains(main,fade=fade)
        if run:setattr(self.interface,"running",False),setattr(self.interface, "game_over", True)
    def sounds_play(self,sound,repeat=True):
        if repeat and sound is not None:
            sound.play(loops=0)
            repeat=False
        else:repeat=True
    def clear_buttons(self):
        self.interface.active_buttons=[]
    def filt(self,width,height,number,color=(0,0,0),position=(0,0)):
        background=pygame.Surface((width,height),pygame.SRCALPHA)
        background.fill((*color, number))
        self.screen.blit(background,position)
    def on_off(self,main,variable,fade=True,dic=None,command=None):
        if dic is None:setattr(self, variable, not getattr(self, variable))
        else:variable[dic] = not variable[dic]
        self.change_mains(main,fade=fade,command=command)
    def on_off_sound(self,sound,type_sound,play=True,game=False,command=False):
        sound.play(loops=-1) if play and self.config.config_sounds[type_sound] else sound.stop()
        if game:self.on_off_sound(self.interface.sound_game,"sound_game")
        if command:self.config.save_config()
    def increase_decrease_variable(self,main,variable,number,population=False,fade=False,dic=None,length=None,command=None,recu=False):
        if dic!=None and length!=None:dic[variable]=((dic[variable] + number) % len(dic[length]))
        elif dic!=None:dic[variable]=max(1, dic[variable] + number)
        else:setattr(self,variable,getattr(self,variable)+number)
        self.change_mains(main=main,fade=fade,command=self.config.save_config,command2=command,recursive=recu)
        if population:self.interface.population()
    def more_options(self,command=[]):
        try:
            for cmd in command:
                if callable(cmd):cmd()
        except TypeError:return None
    def type_game(self,mode_one=False,mode_two=False,mode_three=False):
        self.interface.mode_game["Training AI"]=mode_one
        self.interface.mode_game["Player"]=mode_two
        if os.path.exists(self.interface.model_path):self.interface.mode_game["AI"]=mode_three
