import torch
import numpy as np
class AIHandler:
    def __init__(self, game):
        self.game = game
        self.models = []
    def get_state(self, player):
        distances_y = [abs(player.rect.y - self.object2.y),abs(player.rect.y - self.platarforms_nexts[0].y),
                    abs(player.rect.y - self.platarforms_nexts[1].y),abs(player.rect.y - self.platarforms_nexts[2].y),
                    abs(player.rect.y - self.platarforms_nexts[3].y),abs(player.rect.y - self.object3.y),
                    abs(player.rect.y - self.object4.y),abs(player.rect.y - self.object5.y)]
        return np.array([player.rect.x, player.rect.y, self.object2.x, self.object2.y,self.platarforms_nexts[0].x,self.platarforms_nexts[0].y,self.platarforms_nexts[1].x,self.platarforms_nexts[1].y,self.platarforms_nexts[2].x,self.platarforms_nexts[2].y,self.platarforms_nexts[3].x,self.platarforms_nexts[3].y,self.object3.x,self.object3.y,self.object4.x,self.object4.y,self.object5.x,self.object5.y,*distances_y])
    def softmax(self, x):
        exp_x = np.exp(x - np.max(x))
        return exp_x / exp_x.sum()
    def AI_actions(self,player,action):
        probabilities = self.softmax(action)
        chosen_action = np.argmax(probabilities)
        if chosen_action == 0:player.rect.x -= 5
        elif chosen_action == 1:player.rect.x += 5
        elif chosen_action == 2 and player.isjumper:player.jump(self.physics.jump_force,self.sound_jump)
    def actions_AI(self, models):
        def actions(player, model):
            state = self.get_state(player)
            action = model(torch.tensor(state, dtype=torch.float32)).detach().numpy()
            self.AI_actions(player, action)
        try:
            for player, model in zip(self.game.players, models):
                if player.active:actions(player, model)
        except:actions(self.game.players[0], models)
    def get_reward(self, reward: list) -> list:
        for player in self.game.players:
            reward.append(player.reward)
            player.reward = 0
            player.reset(40, 40)
        return reward