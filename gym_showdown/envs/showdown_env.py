#main body of the showdownEnv class

import gym
import asyncio

class ShowdownEnv(gym.Env):


    metadata = {'render.modes':['human']}
    reward_range = [-1,1]
    action_space = [0,1,2,3,4,5,6,7,8,9,10] 
    #4 moves, 6 switches, 1 forfeit, 11 possible actions in total
    observation_space = None

    async def __init__(self):
        #login and start battle
        #preferrably using the ladder
        from helpers.mywebsocket import showdownWebsocket as ws
        pass

    async def _step(self, action):
        #take action
        pass

    async def _reset(self):
        #end epoch and start a new one
        pass

    def _render(self, mode):
        #render current situation
        pass

    def _close(self):
        #close everything
        pass

