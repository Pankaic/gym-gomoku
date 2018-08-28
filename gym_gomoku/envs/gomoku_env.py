import numpy as np

import gym
from gym import error, spaces, utils
from gym.utils import seeding

class GomokuEnv(gym.Env):
  metadata = {'render.modes': ['human']}

  def __init__(self, board_size):
  	self.board_size = board_size

    ...
  def step(self, action):
    ...
  def reset(self):
    ...
  def render(self, mode='human', close=False):
    ...

class GomokuLargeEnv(GomokuEnv):
	def __init__(self):
		GomokuEnv.__init__(self, 19)
	...

class GomokuMediumEnv(GomokuEnv):
	def __init__(self):
		GomokuEnv.__init__(self, 15)
	...

class GomokuSmallEnv(GomokuEnv):
	def __init__(self):
		GomokuEnv.__init__(self, 11)
	...