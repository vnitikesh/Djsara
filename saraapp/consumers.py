from cgitb import text
import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import requests
import os
from gtts import gTTS
class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()
        # self.language = 'hi'
        # self.text = 'Hi ' + str(self.room_name) + " This is djsaara, your assistant powered by RASA, under Scifi production. Please search the weather for different Indian states."
        # self.tts_obj = gTTS(text = self.text, lang = self.language, slow = False)
        # self.tts_obj.save("welcome.mp3")
        # os.system("mpg321 welcome.mp3")
        # exit
        

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        print(text_data)
        message = text_data_json['message']
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    def chat_message(self, event):
        message = event['message']
        print("*"*30)
        
        payload = {"sender":"test_user", "message":message}
        print("payload:- ",payload)
        headers = {"content-type": "application/json"}
        r = json.loads(requests.post('http://localhost:5005/webhooks/rest/webhook', json = payload, headers = headers).text)
        print("request content:- ",r)
        bot_reply = ''
        
        
        try:
            bot_reply = json.loads(r[1]['text'])
            print(bot_reply)
            result = 1
        except:
            bot_reply = "Oo ohh! Couldn't understand"
            result = 0
            pass
        # message += "\n \n" + str(bot_reply)
        print(message,' ',type(message))
        self.send(text_data = json.dumps({
            'message': message,
            'bot_reply': bot_reply,
            'result': result
        }))
        # try:
        #     self.language = 'hi' #Hindi
        #     print(r, ' ', type(r))
        #     text = json.loads(r[1]['text'])
        #     self.text = "Here is the Weather report of " + str(text['city'])
        #     self.text += ".We can see " + str(text['condition']) + "ski"
        #     self.text += ".Wind is blowing at " + str(text['wind_speed']) + "miles an hour having " + str(text['humidity']) + "percentage of air humidity"
        #     self.tts_obj = gTTS(text = self.text, lang = self.language, slow = False)
        #     self.tts_obj.save("bot_reply.mp3")
        #     os.system("mpg321 bot_reply.mp3")
        # except Exception as e:
        #     print('Exception:- ',e)
        # exit