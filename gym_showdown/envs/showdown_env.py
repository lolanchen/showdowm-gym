import gym
import time
import websockets
from helper_socket import ShowdownSocket

class ShowdownEnv(gym.Env):

    def __init__(self, agent_name):

        metadata = {'render.modes':['human']}
        reward_range = [-1,1]
        action_space = [0,1,2,3,4,5,6,7,8,9,10] 
        #4 moves, 6 switches, 1 forfeit
        observation_space = None #?

        self.ss = ShowdownSocket(agent_name)
        self.ss.login()
        self.ss.challenge_available_player() #not implemented

    def _step(self, action):

        #fight
        if action in [0,1,2,3]:
            self.ss.pick_move(action)
        #switch
        elif action in [4,5,6,7,8,9]:
            switch_target = action - 4
            self.ss.switch_pokemon(switch_target)#not implemented
        #forfeit
        else:
            self._reset
        
        state = self.ss.get_state()
        ob = self.observe(state)
        reward = self.ss.get_reward()
        done = self.ss.if_done()

        return  ob, reward, done
        pass

    def _reset(self):
        self.ss.leave_battle()
        time.sleep(1)
        self.ss.challenge_available_player

    def _render(self, mode):
        #render current situation
        pass

    def _close(self):
        #close everything
        pass

    def _observe(raw_state):
        pass