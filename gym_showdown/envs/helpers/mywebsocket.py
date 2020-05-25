import asyncio
import websockets
import requests
import json


class showdownWebsocket():

    #attributes of class
    websocket = None
    login_uri = None
    username = None
    password = None
    login_uri = None
    last_challenge_time = 0
    login_uri = "https://localhost.psim.us/action.php"




    @classmethod
    async def create(cls, username, password):
        self = showdownWebsocket()
        self.username = username
        self.password = password
        self.websocket = await websockets.connect("ws://localhost:8000/showdown/websocket")
        self.connected = True
        return self

    async def get_id_and_challstr(self):
        while True:
            message = await self.websocket.recv()
            split_message = message.split('|')
            if split_message[1] == 'challstr':
                return split_message[2], split_message[3]

    async def login(self):

        client_id, challstr = await self.get_id_and_challstr()
        response = requests.post(
                self.login_uri,
                data={
                    'act': 'getassertion',
                    'userid': self.username,
                    'challstr': '|'.join([client_id, challstr]),
                }
            )
        if response.status_code == 200:
            assertion = response.text
            message = ["/trn " + self.username + ",0," + assertion]
            await self.send_message('', message)
            print(message)

           
    
    async def send_message(self, room, message_list):
        
        message = room + "|" + "|".join(message_list)
        await self.websocket.send(message)



    async def challenge_user(self, user_to_challenge):
        await self.websocket.send("/utm null")
        message = ["/challenge {},{}".format(user_to_challenge, "gen1randombattle")]
        await self.send_message('', message)

    async def disconnect(self):
        self.connected = False
        self.websocket.close()

