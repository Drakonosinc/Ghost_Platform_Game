import numpy as np
import torch
from Game.Ghost_Platform import ghost_platform as GhostPlatform
from AI.AI_Controller import AIHandler
from pyforgeai import DQNAgent, ReplayMemory, SimpleNN


class GhostPlatformEnv:
    """Wrapper del juego GhostPlatform para interfaz Gym-like."""
    def __init__(self):
        self.game = GhostPlatform()
        self.handler = AIHandler(self.game)
        self.prev_reward = 0

    @property
    def action_space(self) -> int:
        return 3

    def reset(self) -> np.ndarray:
        self.game.reset(True)
        self.prev_reward = 0
        return self.handler.get_state(self.game.players[0])

    def step(self, action: int) -> tuple:
        player = self.game.players[0]
        if action == 0:
            player.rect.x -= 5
        elif action == 1:
            player.rect.x += 5
        elif action == 2 and player.isjumper:
            player.jump(self.game.physics.jump_force, None)
        self.game.events(player)
        state = self.handler.get_state(player)
        curr_reward = player.reward
        reward = curr_reward - self.prev_reward
        self.prev_reward = curr_reward
        done = not player.active
        return state, reward, done


def train_dqn(episodes: int = 500):
    env = GhostPlatformEnv()
    state = env.reset()
    agent = DQNAgent(state_size=len(state), action_size=env.action_space)
    for episode in range(1, episodes + 1):
        state = env.reset()
        total_reward = 0
        done = False
        while not done:
            action = agent.select_action(state)
            next_state, reward, done = env.step(action)
            agent.store_transition(state, action, reward, next_state, done)
            agent.optimize_model()
            state = next_state
            total_reward += reward
        print(f"Episodio {episode}/{episodes} - Recompensa total: {total_reward:.2f} - Epsilon: {agent.epsilon:.3f}")
    torch.save(agent.policy_net.state_dict(), 'qlearning_ghost_platform.pth')
    return agent


if __name__ == "__main__":
    train_dqn()
