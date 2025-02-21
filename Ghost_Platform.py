import random,torch
import numpy as np
from Interface import *
from Player import *
class ghost_platform(interface):
    def __init__(self):
        super().__init__(width=700, height=600)
        self.load_AI()
        self.running:bool=True
        self.game_over:bool=False
        self.exit:bool=False
        self.clock=pygame.time.Clock()
        self.FPS:int=60
        self.objects()
        self.nuances()
        self.gravity:float=0.25
        self.jumper:int=-12
        self.mode_game:dict[str, bool]={"Training AI":False,"Player":False,"AI":False}
        self.generation:int=0
        self.population()
    def population(self):
        self.players = [Player(350, self.HEIGHT - 35, 25, 25) for _ in range(self.config_AI["population_value"] if self.mode_game["Training AI"] else 1)]
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
        self.next_position_platforms(player,matrix,object_name,width,height)
    def next_position_platforms(self,player,matrix,object_name,width,height,current_elements=None,next_elements1=None,next_elements2=None,next_elements3=None,next_elements4=None):
        sorted_elements = sorted(matrix, key=lambda t: t[1],reverse=True)
        for i, elements in enumerate(sorted_elements):
            if elements[1] < player.rect.y:
                current_elements = elements
                next_elements1 = sorted_elements[i + 1] if i + 1 < len(sorted_elements) else None
                next_elements2 = sorted_elements[i + 2] if i + 2 < len(sorted_elements) else None
                next_elements3 = sorted_elements[i + 3] if i + 3 < len(sorted_elements) else None
                next_elements4 = sorted_elements[i + 4] if i + 4 < len(sorted_elements) else None
                break
        if current_elements:setattr(self, object_name, Rect(current_elements[0],current_elements[1],width,height))
        if next_elements1:self.platarforms_nexts[0]=Rect(next_elements1[0],next_elements1[1],width,height)
        if next_elements2:self.platarforms_nexts[1]=Rect(next_elements2[0],next_elements2[1],width,height)
        if next_elements3:self.platarforms_nexts[2]=Rect(next_elements3[0],next_elements3[1],width,height)
        if next_elements4:self.platarforms_nexts[3]=Rect(next_elements4[0],next_elements4[1],width,height)
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
        if not player.isjumper:player.fall(self.gravity)
        if player.rect.y>=self.HEIGHT-35 and not player.floor_fall:self.repeat_in_events_collision(player,self.HEIGHT-35,jumper=True)
        elif not player.check_collision(self.object2):
            player.fall(self.gravity)
            if player.rect.y<=-20:self.repeat_in_events_collision(player,-15,self.gravity,True)
            if player.rect.y>=self.HEIGHT+50:self.sounddeath(player=player,sound_play=self.check_sound(self.sound_game_lose,"game_over"))
    def repeat_in_events_collision(self,player,number=0,number2=0,gravity=False,jumper=False,floor=False,reward=0,score=False):
        player.rect.y=number
        if gravity:player.down_gravity=number2
        if jumper:player.isjumper=True
        if floor:player.floor_fall=True
        if self.mode_game["Training AI"]:player.reward += reward
        if score:player.scores+=1
    def sounddeath(self,sound=True,player=None,sound_play=None):
        if sound:
            if self.mode_game["Training AI"]:player.reward -= 30
            player.active=False
            if sound_play!=None:sound_play.play(loops=0)
            self.restart()
            sound=False
    def handle_keys(self):
        for event in pygame.event.get():
            self.manager.process_events(event)
            self.event_quit(event)
            self.event_keydown(event)
            self.event_buttons(event)
            self.new_events(event)
            if self.main==6:self.event_change_keys(event)
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
            if (self.mode_game["Player"] and self.main==-1) and (event.key==self.config_keys["up1"] or event.key==self.config_keys["up2"]):self.players[0].jump(self.jumper,self.check_sound(self.sound_jump,"sound_jump"))
            if self.main==1 and event.key==K_r:self.change_mains(-1,command=self.reset)
    def press_keys(self):
        if self.mode_game["Player"] and self.main==-1:
            if self.pressed_keys[self.config_keys["right"]]:self.players[0].rect.x+=5
            if self.pressed_keys[self.config_keys["left"]]:self.players[0].rect.x-=5
    def new_events(self,event):
        if self.main==-1 and event.type==self.speed_game:
            self.FPS+=0.5
            if self.mode_game["Training AI"]:
                for player in self.players:
                    if player.active:player.floor_fall=True
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
        if player.life < 0:self.sounddeath(player=player,sound_play=self.check_sound(self.sound_game_lose,"game_over"))
        if self.main==-1:self.screen.blit(self.font6.render("Life",True,self.life_color),(0,9))
    def shield_draw(self,player):
        if player.state_life[1]:pygame.draw.ellipse(self.screen,self.life_color,(player.rect.x-11,player.rect.y-15,50,50),3)
    def check_sound(self,sound,type_sound):return sound if self.config_sounds[type_sound] else None
    def restart(self):
        if all(not player.active for player in self.players) and self.mode_game["Training AI"]:self.reset(False)
        if self.mode_game["Player"] or self.mode_game["AI"]:self.change_mains(1,self.RED,150,self.reset)
    def reset(self,running=True):
        self.running=running
        self.FPS=60
        self.objects()
        for player in self.players:player.reset(350, self.HEIGHT - 35)
        self.nuances()
        pygame.time.set_timer(self.speed_game, 0)
        pygame.time.set_timer(self.speed_game, 5000)
    def get_state(self,player=Player(350, 600 - 35, 25, 25)):
        distances_y = [abs(player.rect.y - self.object2.y),abs(player.rect.y - self.platarforms_nexts[0].y),
                    abs(player.rect.y - self.platarforms_nexts[1].y),abs(player.rect.y - self.platarforms_nexts[2].y),
                    abs(player.rect.y - self.platarforms_nexts[3].y),abs(player.rect.y - self.object3.y),
                    abs(player.rect.y - self.object4.y),abs(player.rect.y - self.object5.y)]
        return np.array([player.rect.x, player.rect.y, self.object2.x, self.object2.y,self.platarforms_nexts[0].x,self.platarforms_nexts[0].y,self.platarforms_nexts[1].x,self.platarforms_nexts[1].y,self.platarforms_nexts[2].x,self.platarforms_nexts[2].y,self.platarforms_nexts[3].x,self.platarforms_nexts[3].y,self.object3.x,self.object3.y,self.object4.x,self.object4.y,self.object5.x,self.object5.y,*distances_y])
    def type_mode(self):self.actions_AI(self.models if self.mode_game["Training AI"] else self.model_training)
    def actions_AI(self,models):
        def actions(player,model):
            state=self.get_state(player)
            action = model(torch.tensor(state, dtype=torch.float32)).detach().numpy()
            self.AI_actions(player,action)
        try:
            for player, model in zip(self.players, models):
                if player.active:actions(player,model)
        except:actions(self.players[0],models)
    def softmax(self, x):
        exp_x = np.exp(x - np.max(x))
        return exp_x / exp_x.sum()
    def AI_actions(self,player,action):
        probabilities = self.softmax(action)
        chosen_action = np.argmax(probabilities)
        if chosen_action == 0:player.rect.x -= 5
        elif chosen_action == 1:player.rect.x += 5
        elif chosen_action == 2 and player.isjumper:player.jump(self.jumper,self.sound_jump)
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
            if player.active:self.draw(player),self.events(player)
        self.calls_elements()
    def run_with_models(self):
        self.running = True
        for player in self.players:player.reward = 0
        while self.running and self.game_over == False:
            if self.main == -1:self.main_run()
            self.item_repeat_run()
        return [player.reward for player in self.players]