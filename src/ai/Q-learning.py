import torch
import torch.nn as nn
import torch.optim as optim
import random
import numpy as np
from collections import deque
from Game.Space_Pong import Snake_Game
from AI.Ai_Controller import AIHandler
from AI.Neural_Network import SimpleNN