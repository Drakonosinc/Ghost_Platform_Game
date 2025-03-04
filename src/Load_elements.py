import pygame,os,json
from pygame.locals import *
from AI.Genetic_Algorithm import *
from Config_Loader import *
class load_elements():
    def __init__(self,title,width=0, height=0):
        pygame.init()
        pygame.display.set_caption(title)
        self.screen = pygame.display.set_mode((width, height))
        self.config=Config()
        self.config.load_config()
        self.define_colors()
        self.load_images()
        self.load_fonts()
        self.load_sounds()
        self.additional_events()
    def define_colors(self):
        self.GRAY=(127,127,127)
        self.WHITE=(255,255,255)
        self.BLACK=(0,0,0)
        self.GREEN=(0,255,0)
        self.BLUE=(0,0,255)
        self.SKYBLUE=(135,206,235)
        self.YELLOW=(255,255,0)
        self.RED=(255,0,0)
        self.GOLDEN=(255,199,51)
        self.background=self.GRAY
        self.life_color=self.GREEN
    def load_images(self):
        self.image_path=os.path.join(self.config.base_dir, "images")
        self.space=pygame.image.load(os.path.join(self.image_path,self.config_visuals["background"][self.config_visuals["background_value"]]))
        self.space=pygame.transform.scale(self.space,(700,400))
        self.player_ghost=pygame.image.load(os.path.join(self.image_path,self.config_visuals["player"][self.config_visuals["player_value"]])).convert_alpha()
        self.player_ghost=pygame.transform.scale(self.player_ghost,(35,35))
        self.floor=pygame.image.load(os.path.join(self.image_path,self.config_visuals["floor"][self.config_visuals["floor_value"]])).convert_alpha()
        self.floor=pygame.transform.scale(self.floor,(100,40))
        self.meteorite=pygame.image.load(os.path.join(self.image_path,self.config_visuals["meteorite"][self.config_visuals["meteorite_value"]])).convert_alpha()
        self.meteorite=pygame.transform.scale(self.meteorite,(50,85))
        self.potion=pygame.image.load(os.path.join(self.image_path,self.config_visuals["potion"][self.config_visuals["potion_value"]])).convert_alpha()
        self.potion=pygame.transform.scale(self.potion,(35,40))
        self.shield=pygame.image.load(os.path.join(self.image_path,self.config_visuals["shield"][self.config_visuals["shield_value"]])).convert_alpha()
        self.shield=pygame.transform.scale(self.shield,(50,50))
    def load_fonts(self):
        self.font_path=os.path.join(self.config.base_dir, "fonts")
        self.font=pygame.font.Font(None,25)
        self.font1=pygame.font.SysFont("times new roman", 80)
        self.font2=pygame.font.Font(None,35)
        self.font2_5=pygame.font.Font(os.path.join(self.font_path,"ka1.ttf"),30)
        self.font3=pygame.font.Font(os.path.join(self.font_path,"ka1.ttf"),60)
        self.font3_5=pygame.font.Font(os.path.join(self.font_path,"8bitOperatorPlusSC-Bold.ttf"),30)
        self.font4=pygame.font.Font(os.path.join(self.font_path,"ka1.ttf"),75)
        self.font5=pygame.font.Font(os.path.join(self.font_path,"ka1.ttf"),20)
        self.font6=pygame.font.Font(os.path.join(self.font_path,"ka1.ttf"),16)
    def load_sounds(self):
        pygame.mixer.init()
        self.sound_path=os.path.join(self.config.base_dir, "sounds")
        self.sound_jump=pygame.mixer.Sound(os.path.join(self.sound_path,"jump.aiff"))
        self.sound_meteorite=pygame.mixer.Sound(os.path.join(self.sound_path,"meteor.mp3"))
        self.sound_health=pygame.mixer.Sound(os.path.join(self.sound_path,"health.flac"))
        self.sound_menu=pygame.mixer.Sound(os.path.join(self.sound_path,"back_fo_menu.wav"))
        self.sound_game=pygame.mixer.Sound(os.path.join(self.sound_path,"back_fo_game.wav"))
        self.sound_game_lose=pygame.mixer.Sound(os.path.join(self.sound_path,"game_lose.flac"))
        self.sound_shield=pygame.mixer.Sound(os.path.join(self.sound_path,"shield.wav"))
        self.sound_exit=pygame.mixer.Sound(os.path.join(self.sound_path,"exitbutton.wav"))
        self.sound_touchletters=pygame.mixer.Sound(os.path.join(self.sound_path,"touchletters.wav"))
        self.sound_buttonletters=pygame.mixer.Sound(os.path.join(self.sound_path,"buttonletters.mp3"))
    def load_AI(self):
        self.model_path=os.path.join(self.config.base_dir, "AI/best_model.pth")
        self.model_training = load_model(self.model_path, 26, 3) if os.path.exists(self.model_path) else None
    def additional_events(self):
        self.speed_game=pygame.USEREVENT + 1
        pygame.time.set_timer(self.speed_game, 5000)