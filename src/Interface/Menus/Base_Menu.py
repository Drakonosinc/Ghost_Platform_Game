import pygame
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
            self.clock.tick(20)
            alpha += -15 if fade_in else 15
    def change_mains(self,main=0,color=(0,0,0),limit=255,command=None,command2=None,sound=None,run=False,fade=True,recursive=False):
        self.sounds_play(sound=self.sound_touchletters if sound==None else sound)
        if fade:self.fade_transition(False,color,limit)
        self.clear_buttons()
        self.main=main
        self.draw_menus()
        if command!=None:command()
        if command2!=None:command2()
        if recursive:self.change_mains(main,fade=fade)
        if run:setattr(self,"running",False),setattr(self, "game_over", True)
    def sounds_play(self,sound,repeat=True):
        if repeat:
            sound.play(loops=0)
            repeat=False
        else:repeat=True
    