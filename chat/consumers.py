import json
from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Accept the WebSocket connection
        await self.accept()

    async def disconnect(self, close_code):
        # Called when the socket closes
        pass

    async def receive(self, text_data):
        # Echo back whatever message the client sent
        await self.send(text_data=text_data)

