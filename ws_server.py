#!/usr/bin/python3
import asyncio
import random
import websockets
import json
from os import listdir
from os.path import isfile, join

images = [f for f in listdir("assets/images") if isfile(join("assets/images", f))]

sessions = dict()

# URL format /token/userid
async def server(websocket, path):
    print("Connect with: " + path)

    token = path.split('/')[1] 
    user  = path.split('/')[2] 

    if token not in sessions:
        sessions[token] = dict()
    if user not in sessions[token]:
        sessions[token][user] = websocket

    try:
        async for command in websocket:
            print(f"Got command: {command} from {user} in session {token}")

            if command == 'UN':
               new_images = random.choices(images, k=3)
               ret = {
                        "command": "update",
                        "imgset": {
                            "img1": new_images[0],
                            "img2": new_images[1],
                            "img3": new_images[2]
                        }
                }
               for i in sessions[token]:
                   await sessions[token][i].send(json.dumps(ret))
    finally:
        del sessions[token][user]
        if len(sessions[token]) == 0:
            del sessions[token]

start_server = websockets.serve(server, "0.0.0.0", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
