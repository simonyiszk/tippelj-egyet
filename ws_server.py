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

    # path.splot('/')[1] == ws
    token = path.split('/')[2] 

    if token not in sessions:
        sessions[token] = []
    if websocket not in sessions[token]:
        sessions[token].append(websocket)

    try:
        async for command in websocket:
            print(f"Got command in session {token}")

            if command == 'UN':
               new_images = random.sample(images, k=3)
               ret = {
                        "command": "update",
                        "imgset": {
                            "img1": new_images[0],
                            "img2": new_images[1],
                            "img3": new_images[2]
                        }
                }
               for i in sessions[token]:
                   await i.send(json.dumps(ret))
    except websockets.exceptions.ConnectionClosedError:
        print(f"Connection closed in {token}")
    except:
        print(f"Unknown exception in {token}")
    finally:
        try:
            sessions[token].remove(websocket)
            if len(sessions[token]) == 0:
                del sessions[token]
        except KeyError:
            print(f"Unable to free session, KeyError {token}")
        except:
            print(f"Unable to free session, unknown error in {token}")


start_server = websockets.serve(server, "0.0.0.0", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
