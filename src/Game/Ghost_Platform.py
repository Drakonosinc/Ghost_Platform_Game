import random
import numpy as np
from Interface.Interface import *
from Entities import *
from Physics import *
from AI import *
class ghost_platform(interface):
    def __init__(self):
        super().__init__(width=700, height=600)
        self.load_AI()
        self.physics = PhysicsHandler()
        self.ai_handler = AIHandler(self)
        self.collision_handler = CollisionHandler(self)
        self.running:bool=True
        self.game_over:bool=False
        self.exit:bool=False
        self.clock=pygame.time.Clock()
        self.FPS:int=60
        self.objects()
        self.nuances()
        self.mode_game:dict[str, bool]={"Training AI":False,"Player":False,"AI":False}
        self.generation:int=0
        self.active_floor:bool=False
        self.population()
    def population(self):
        self.players = [Player(350, self.HEIGHT - 35, 25, 25) for _ in range(self.config.config_AI["population_value"] if self.mode_game["Training AI"] else 1)]
        self.models = []
    def objects(self):
        self.object2=Rect(0,0,0,0)
        self.object3=Rect(0,0,0,0)
        self.object4=Rect(0,0,0,0)
        self.object5=Rect(0,0,0,0)
        self.platarforms_nexts=[Rect(0,0,0,0),Rect(0,0,0,0),Rect(0,0,0,0),Rect(0,0,0,0)]
    def generate_nuances(self):
        return np.column_stack((np.random.choice(np.arange(25, self.WIDTH-50, 115), 15),np.random.choice(np.arange(-500, 0, 200), 15))).tolist()
    def nuances(self):self.matrix=[self.generate_nuances(),self.generate_nuances()]
    def elements(self,matrix,speed_fall,object_name,width,height,type_object,image=None,restx=0,resty=0):
        for coords in matrix:
            coords[1]+=speed_fall
            for player in self.players:
                if player.active:
                    rect=Rect(coords[0],coords[1],width,height)
                    if coords[1]>=self.HEIGHT:self.reset_coords(coords)
                    self.collision(player,rect,type_object,coords)
                    self.screen.blit(image,(coords[0]-restx,coords[1]-resty))
            self.handle_obj_collision(player, object_name, width, height,matrix)
    def handle_obj_collision(self, player, objects, width, height,matrix):
        current_object, next_object1, next_object2, next_object3, next_object4 = self.collision_handler.get_next_object(player, matrix)
        self.collision_handler.update_objects(width, height, objects, current_object, next_object1, next_object2, next_object3, next_object4)
    def collision(self,player,objects,type_object,coords):
        if player.check_collision(objects):
            match type_object:
                case "platform":self.repeat_in_events_collision(player,objects.y-25,0,True,True,True,1,True)
                case "meteorite":self.repeat_in_collision(*(player,coords,self.sound_meteorite,"sound_damage",-20,0,0) if not player.state_life[1] else (player,coords,self.sound_meteorite,"sound_damage",-5,1,False))
                case "potion" if player.life<100:self.repeat_in_collision(player,coords,self.sound_health,"sound_potion",10,0,1)
                case "shield" if not player.state_life[1]:self.repeat_in_collision(player,coords,self.sound_shield,"sound_shield",15,1,True)
    def repeat_in_collision(self,player,coords,sound,type_sound,reward,statelife1,statelife2):
        player.state_life[statelife1]=statelife2
        self.reset_coords(coords)
        if (sound_touch:=self.check_sound(sound,type_sound)):sound_touch.play()
        if self.mode_game["Training AI"]:player.reward += reward
    def reset_coords(self,coords):
        coords[1]=random.choice(np.arange(-500, 0, 200))
        coords[0]=random.choice(np.arange(25, self.WIDTH-50, 115))
    def calls_elements(self):
        self.elements(self.matrix[0],3,"object2",100,25,"platform",self.floor,0,10)
        self.elements([self.matrix[1][0]],6,"object3",50,35,"meteorite",self.meteorite,0,45)
        self.elements([self.matrix[1][1]],2,"object4",35,25,"potion",self.potion,0,10)
        self.elements([self.matrix[1][2]],4,"object5",45,25,"shield",self.shield,5,10)
    def events(self,player):
        if player.rect.x < 0:player.rect.x=0
        if player.rect.x > self.WIDTH-player.rect.width:player.rect.x=self.WIDTH-player.rect.width
        if not player.isjumper:self.physics.apply_gravity(player)
        if player.rect.y>=self.HEIGHT-35 and not player.floor_fall:self.repeat_in_events_collision(player,self.HEIGHT-35,jumper=True)
        elif not player.check_collision(self.object2):
            self.physics.apply_gravity(player)
            if player.rect.y<=-20:self.repeat_in_events_collision(player,-15,self.physics.gravity,True)
            if player.rect.y>=self.HEIGHT+50:self.collision_handler.handle_collision(player)
    def repeat_in_events_collision(self,player,number=0,number2=0,gravity=False,jumper=False,floor=False,reward=0,score=False):
        player.rect.y=number
        if gravity:player.dy=number2
        if jumper:player.isjumper=True
        if floor:player.floor_fall=True
        if self.mode_game["Training AI"]:player.reward += reward
        if score:player.scores+=1
    def handle_keys(self):
        for event in pygame.event.get():
            self.manager.process_events(event)
            self.event_quit(event)
            self.event_keydown(event)
            self.new_events(event)
            if self.main==6:self.keys_menu.event_change_keys(event)
        self.pressed_keys=pygame.key.get_pressed()
        self.pressed_mouse=pygame.mouse.get_pressed()
        self.mouse_pos = pygame.mouse.get_pos()
        self.press_keys()
    def event_quit(self,event):
        if event.type==QUIT:self.change_mains(command=self.close_game,sound=self.sound_exit)
    def close_game(self):self.game_over,self.running,self.exit=True,False,True
    def event_keydown(self,event):
        if event.type==KEYDOWN:
            if self.main==3 and event.key==K_p:self.change_mains(-1,self.GRAY,20)
            elif self.main==-1 and event.key==K_p:self.change_mains(3,self.GRAY)
            if (self.mode_game["Player"] and self.main==-1) and (event.key in {self.config.config_keys["up1"], self.config.config_keys["up2"]}):self.players[0].jump(self.physics.jump_force,self.check_sound(self.sound_jump,"sound_jump"))
            if self.main==1 and event.key==K_r:self.change_mains(-1,command=self.reset)
    def press_keys(self):
        if self.mode_game["Player"] and self.main==-1:
            if self.pressed_keys[self.config.config_keys["right"]]:self.players[0].rect.x+=5
            if self.pressed_keys[self.config.config_keys["left"]]:self.players[0].rect.x-=5
    def new_events(self,event):
        if self.main==-1 and event.type==self.speed_game:
            self.FPS+=0.5
            if self.mode_game["Training AI"]:self.active_floor=True
    def draw(self,player):
        self.screen.blit(self.player_ghost,(player.rect.x-5,player.rect.y-5))
        self.bar_life(player),self.shield_draw(player),self.draw_score(player),self.draw_generations()
    def draw_generations(self):
        if self.mode_game["Training AI"]:self.screen.blit(self.font6.render(f"Generation: {self.generation}",True,self.YELLOW),(0,30))
    def draw_score(self,player):
        self.screen.blit(self.font6.render(f"Score: {int(player.scores)}",True,self.YELLOW),(0,self.HEIGHT-30))
    def bar_life(self,player):
        pygame.draw.rect(self.screen,self.BLACK,(50,8,105,20),4)
        pygame.draw.rect(self.screen,self.life_color,(52,11,player.life,15))
        player.life += 1 if player.state_life[0] == 1 else -1 if player.state_life[0] == 0 else 0
        states = {100: (2, self.GREEN),75: (2, self.SKYBLUE),50: (2, self.YELLOW),25: (2, self.RED),-1: (2, self.BLACK)}
        if player.life in states:player.state_life[0], self.life_color = states[player.life]
        if player.life < 0:self.collision_handler.handle_collision(player)
        if self.main==-1:self.screen.blit(self.font6.render("Life",True,self.life_color),(0,9))
    def shield_draw(self,player):
        if player.state_life[1]:pygame.draw.ellipse(self.screen,self.life_color,(player.rect.x-11,player.rect.y-15,50,50),3)
    def check_sound(self,sound,type_sound):return sound if self.config.config_sounds[type_sound] else None
    def restart(self):
        if all(not player.active for player in self.players) and self.mode_game["Training AI"]:self.reset(False,1)
        if self.mode_game["Player"] or self.mode_game["AI"]:self.change_mains(1,self.RED,150,self.reset)
    def reset(self,running=True,type_reset=0):
        self.running=running
        self.FPS=60
        self.objects()
        self.nuances()
        self.active_floor=False
        pygame.time.set_timer(self.speed_game, 0)
        pygame.time.set_timer(self.speed_game, 5000)
        if type_reset==0:self.players[0].reset(350, self.HEIGHT - 35)
    def type_mode(self):self.ai_handler.actions_AI(self.models if self.mode_game["Training AI"] else self.model_training)
    def get_reward(self, reward: list) -> list:return self.ai_handler.get_reward(reward)
    def item_repeat_run(self):
        self.handle_keys()
        self.time_delta = self.clock.tick(self.FPS)/1000.0
        self.manager.update(self.time_delta)
        self.manager.draw_ui(self.screen)
        pygame.display.flip()
    def run(self):
        self.running = True
        while self.running and (not self.mode_game["Training AI"] and not self.mode_game["Player"] and not self.mode_game["AI"]):
            self.item_repeat_run()
    def main_run(self):
        if self.mode_game["AI"] or self.mode_game["Training AI"]:self.type_mode()
        self.screen.fill(self.background)
        for player in self.players:
            if player.active:
                if self.active_floor:player.floor_fall=True
                self.draw(player),self.events(player)
        self.calls_elements()
    def run_with_models(self):
        self.running = True
        while self.running and self.game_over == False:
            if self.main == -1:self.main_run()
            self.item_repeat_run()
        return self.get_reward([])