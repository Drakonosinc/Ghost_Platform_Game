import json,os
from pygame.locals import *
class Config():
    def __init__(self):self.base_dir = os.path.abspath(os.path.join(__file__, "../../.."))
    def load_config(self):
        try:
            self.config_path = os.path.join(self.base_dir, "Config")
            with open(os.path.join(self.config_path,"config.json"), 'r') as file:config = json.load(file)
            self.config_sounds = config["config_sounds"]
            self.config_keys = config["config_keys"]
            self.config_visuals = config["config_visuals"]
            self.config_AI = config["config_AI"]
        except:self.config(alls=True),self.save_config()
    def config(self,sounds=False,keys=False,visuals=False,AI=False,alls=False):
        self.config_path = os.path.join(self.base_dir, "Config")
        if sounds or alls:self.config_sounds={"sound_menu":True,"sound_game":True,"sound_jump":True,"game_over":True,
                            "sound_damage":True,"sound_potion":True,"sound_shield":True}
        if keys or alls:self.config_keys={"up1":K_SPACE,"name_up1":"Space","up2":K_w,"name_up2":"W",
                        "left":K_a,"name_left":"A","right":K_d,"name_right":"D"}
        if visuals or alls:self.config_visuals={"background":["espacio.png"],"background_value":0,
                                                "player":["flyghost.png"],"player_value":0,
                                                "floor":["suelo1.png"],"floor_value":0,
                                                "meteorite":["meteorito.png","fire.png"],"meteorite_value":0,
                                                "potion":["pocion1.png"],"potion_value":0,
                                                "shield":["shield1.png"],"shield_value":0}
        if AI or alls:self.config_AI={"generation_value":100,"population_value":20,"try_for_ai":3,"model_save":False}
    def save_config(self):
        config = {"config_sounds":self.config_sounds,"config_keys":self.config_keys,"config_visuals":self.config_visuals,"config_AI":self.config_AI}
        with open(os.path.join(self.config_path,"config.json"),"w") as file:json.dump(config, file, indent=4)