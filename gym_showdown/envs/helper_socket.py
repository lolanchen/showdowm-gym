import websocket
import requests


class ShowdownSocket:
    def __init__(self, _username):
        super.__init__()
        self.ws = websocket.create_connection("ws://localhost:8000/showdown/websocket")
        self.username = _username

    def msg_to_room(self, room, message_list):
        message = room + "|" + "|".join(message_list)
        self.ws.send(message)

    def send_message(self, room, message_list):
        
        message = room + "|" + "|".join(message_list)
        self.ws.send(message)

    def get_id_and_challstr(self):
        while True:
            message = self.ws.recv()
            split_message = message.split('|')
            if split_message[1] == 'challstr':
                return split_message[2], split_message[3]

    def login(self):
        client_id, challstr = self.get_id_and_challstr()
        response = requests.post(
                "https://localhost.psim.us/action.php",
                data={
                    'act': 'getassertion',
                    'userid': self.username,
                    'challstr': '|'.join([client_id, challstr]),
                }
            )
        if response.status_code == 200:
            assertion = response.text
            message = ["/trn " + self.username + ",0," + assertion]
            self.send_message('', message)
            print(message)
        self.ws.send("|/join lobby")

    def send_message(self, room, message_list):
        message = room + "|" + "|".join(message_list)
        self.ws.send(message)

    def challenge_user(self, user_to_challenge):
        self.ws.send("/utm null")
        message_list = ["/challenge {},{}".format(user_to_challenge, "gen1randombattle")]
        self.send_message('', message_list)

    def challenge_available_player(self):
        # make agent pool 
        # only activate half at a time

        # 

        pass

    def get_state(self):
        while True:
            msg = self.ws.recv()
            if 'battle-gen' in msg:
                return msg

    def get_reward(self):
        pass

    def if_done(self):
        pass

    def get_battletag(self):
        while True:
            msg = self.ws.recv()
            if 'battle-gen' in msg:
                battletag = msg.split("|")[0].replace('>','')
                battletag = battletag.replace('\n','')
                return battletag

    def pick_move(self, move):
        tag = self.get_battletag
        msg = "{}|/choose move {}".format(tag, str(move))
        self.ws.send(msg)

    def switch_pokemon(self, switch_target):
        tag = self.get_battletag
        msg = "{}|/switch {}".format(tag, str(switch_target))
        self.ws.send(msg)


    def leave_battle(self):
        tag = self.get_battletag
        msg = '|/leave '.append(tag)
        self.ws.send(msg)




