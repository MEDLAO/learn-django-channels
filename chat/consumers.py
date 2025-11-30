import json
from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Block anonymous users from opening WebSocket connections
        if self.scope["user"].is_anonymous:
            await self.close()
            return

        # Normal connection logic
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.group_name = f"chat_{self.room_name}"

        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )

        # Accept the WebSocket connection
        await self.accept()

    async def disconnect(self, close_code):  # Called when the socket closes
        # Remove connection from the group
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    async def receive(self, text_data=None, bytes_data=None):
        # Convert the incoming text into a Python dict
        data = json.loads(text_data)

        message = data.get("message", "")
        username = self.scope["user"].username  # real logged-in user

        # Broadcast the message to everyone in the group
        await self.channel_layer.group_send(
            self.group_name,
            {
                "type": "chat_message",  # calls the method named chat_message()
                "message": message,
                "username": username,
            }
        )

    async def chat_message(self, event):
        # Get the message that was broadcast to the group
        message = event["message"]
        username = event["username"]

        # Send the message to this Websocket client (browser)
        await self.send(
            text_data=json.dumps({
                "message": f"{username}: {message}"
            })
        )
