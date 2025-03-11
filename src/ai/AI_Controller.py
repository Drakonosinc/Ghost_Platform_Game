import torch
import numpy as np
class AIHandler:
    def __init__(self, game):
        self.game = game
        self.models = []