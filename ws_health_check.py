#!/usr/bin/python3

import asyncio
import websockets
import sys

async def hello():
    uri = "ws://localhost:8765/ws/health_check_token"
    async with websockets.connect(uri) as websocket:
        await websocket.send("UN")
        ans = await websocket.recv()
        #print(ans)

try:
    asyncio.get_event_loop().run_until_complete(hello())
except:
    sys.exit(1)

sys.exit(0)
