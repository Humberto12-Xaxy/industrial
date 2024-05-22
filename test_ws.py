import asyncio
import json
from time import sleep
from websockets.sync.client import connect

def main():
    uri = "ws://localhost:8001/ws/process"
    
    with connect(uri) as websocket:
        while True:
            sleep(5)
            data = websocket.recv()
            print(type(json.loads(data)))

main()