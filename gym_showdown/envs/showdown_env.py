#main body of the showdownEnv class

import gym

class ShowdownEnv(gym.env):
    metadata = {'render.modes':['human']}
    reward_range = [-1,1]
    action_space = [0,1,2,3,4,5,6,7,8,9,10] 
    #4 moves, 6 switches, 1 forfeit, 11 possible actions in total
    observation_space = None

    def __init__(self):
        #initialize
        pass

    def _step(self, action):
        #take action
        pass

    def _reset(self):
        #end epoch and start a new one
        pass

    def _render(self, mode):
        #render current situation
        pass

    def _close(self):
        #close everything
        pass

