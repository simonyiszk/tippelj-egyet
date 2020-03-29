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
    token = path.split('/')[1] 
    user  = path.split('/')[2] 

    if token not in sessions:
        sessions[token] = dict()
    if user not in sessions[token]:
        sessions[token][user] = websocket

    try:
        async for command in websocket:
            print(f"Got command: {command} from {user} in session {token}")

            ret = {}

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
               
               ret = { "command": "show" }
               await websocket.send(json.dumps(ret))


            if command == 'UM':
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
                
               if len(sessions[token]) > 1:
                   others = list(sessions[token])
                   others.remove(user)
                   storyteller = random.choice(others)
                   
                   ret = { "command": "show" }
                   await sessions[token][storyteller].send(json.dumps(ret))

            if command == 'FF':
                ret = { "command": "show" }
                for i in sessions[token]:
                   await sessions[token][i].send(json.dumps(ret))


            
    finally:
        del sessions[token][user]
        if len(sessions[token]) == 0:
            del sessions[token]

start_server = websockets.serve(server, "0.0.0.0", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
