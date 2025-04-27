import torch
import torch.nn as nn
import torch.optim as optim
import random
import numpy as np
from collections import deque
from Game.Ghost_Platform import GhostPlatform
from AI.AI_Controller import AIHandler
from AI.Neural_Network import SimpleNN
class ReplayMemory:
    def __init__(self, capacity: int):
        self.memory = deque(maxlen=capacity)
    def push(self, transition: tuple):
        self.memory.append(transition)
    def sample(self, batch_size: int):
        return random.sample(self.memory, batch_size)
    def __len__(self) -> int:
        return len(self.memory)
class GhostPlatformEnv:
    """Wrapper del juego GhostPlatform para interfaz Gym-like."""
    def __init__(self):
        self.game = GhostPlatform()
        self.handler = AIHandler(self.game)
        self.prev_reward = 0
    @property
    def action_space(self) -> int:return 4
    def reset(self) -> np.ndarray:
        # Reinicia el juego y devuelve el estado inicial
        self.game.reset(True)
        self.prev_reward = 0
        return self.handler.get_state()
    def step(self, action: int) -> tuple:
        # Ejecuta la acción y retorna (next_state, reward, done)
        dir_map = ['UP', 'DOWN', 'LEFT', 'RIGHT']
        self.game.player.direction = dir_map[action]
        self.game.player.move()
        self.game.collision()
        state = self.handler.get_state()
        curr_reward = self.game.player.reward
        reward = curr_reward - self.prev_reward
        self.prev_reward = curr_reward
        done = not self.game.player.active
        if done:
            # Opcional: reiniciar internamente para la próxima llamada a reset
            pass
        return state, reward, done