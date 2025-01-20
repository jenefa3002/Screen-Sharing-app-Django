import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ScreenShareConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = 'screenshare_room'
        self.room_group_name = 'screenshare_group'

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        # Broadcast message to group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'share_screen',
                'data': data
            }
        )

    async def share_screen(self, event):
        # Send data to WebSocket
        await self.send(text_data=json.dumps(event['data']))
