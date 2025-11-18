import json
from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):
    group_name = "chat_room"

    async def connect(self):
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )

        # Accept the WebSocket connection
        await self.accept()

    async def disconnect(self, close_code):
        # Called when the socket closes
        pass

    async def receive(self, text_data=None, bytes_data=None):
        # Convert the incoming text into a Python dict
        data = json.loads(text_data)

        message = data.get("message", "")

        # Build a response
        response = {
            "type": "echo",
            "message": message,
        }

        # Echo back whatever message the client sent
        await self.send(text_data=json.dumps(response))


# push issue test