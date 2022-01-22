import requests
import base64


class SiptecoClient:

    def __init__(self, id, token, header):
        self.id = id
        self.token = token
        self.header = header

    def qr_code(self):
        link = f'https://dev.whatsapp.sipteco.ru/v3/instance{self.id}/status?full=1&token={self.token}'
        response = requests.get(link, headers=self.header)
        line = str(response.text)
        index_1 = line.find('base64,') + 7
        index_2 = line.find('","state"')
        string = line[index_1: index_2]
        with open("imageToSave.png", "wb") as fh:
            fh.write(base64.b64decode(string))

    def status(self):
        link = f'https://dev.whatsapp.sipteco.ru/v3/instance{self.id}/status?full=1&token={self.token}'
        payload = {}
        response = requests.request("GET", link, headers=self.header, data=payload)
        print(response.text)

    def send_message(self, code):
        link = f'https://dev.whatsapp.sipteco.ru/v3/instance{self.id}/sendMessage?token={self.token}'
        payload = {'chatId': '4915216896607@c.us',
                   'body': code,
                   'quotedMsgId': '',
                   'sendSeen': '1',
                   'typeMsg': 'text',
                   'latitude': '35.227221',
                   'longitude': '25.249377',
                   'title': 'Название ',
                   'footer': 'Подвал'}
        files = []
        response = requests.request("POST", link, headers=self.header, data=payload, files=files)
        print(response.text)

    def delete_chat(self):
        link = f'https://dev.whatsapp.sipteco.ru/v3/instance{self.id}/removeChat?token={self.token}'
        payload = {}
        files = {}
        response = requests.request("GET", link, headers=self.header, data=payload, files=files)
        print(response.text)

'''
header_init = {'X-Tasktest-Token': 'f62cdf1e83bc324ba23aee3b113c6249'}
path = 'chat/spare?crm=TEST&domain=test'
link = 'https://dev.wapp.im/v3/'
TOKEN = requests.get(link + path, headers=header_init)
print(TOKEN.text)
'''

'''
Получение TOKEN и ID - {"id":9,"instanceId":"2a01:4f8:c17:ac8:3::a","token":"Es7OhIYSuG2N-klS",
"chat_id":"2a01:4f8:c17:ac8:3::a","md":0,"chat_token":"Es7OhIYSuG2N-klS",
"chat_key":"f5197c79e97c1f1f7300d9c413af2e6a","apikey":"f5197c79e97c1f1f7300d9c413af2e6a",
"date_add":1642665847,"date_trial":1642882988,"date_pay":0,"date_subscription":0,"phone":"",
"name":"","platform":"","status":0,"is_premium":0}
'''


a = SiptecoClient('9', "Es7OhIYSuG2N-klS", {'X-Tasktest-Token': 'f62cdf1e83bc324ba23aee3b113c6249'})
a.qr_code()
a.status()
'''
Набор символов после сканирования QR-кода - 
1@hfX1m+MbqzwH1SLV9SbVG5GKxDXaAv8bzrGJoQ83GWmgpS/SNfPdmgES20nHlSNLNPoEwzM3YsP9Lg==,
ZWYff8gDzYyiQXvAxzrnGM1LTotyoEjUpV4IgSfJmiI=,sPiSaKQA0mCZ2lhZ2U8XoQ==
'''
a.send_message('1@hfX1m+MbqzwH1SLV9SbVG5GKxDXaAv8bzrGJoQ83GWmgpS/SNfPdmgES20nHlSNLNPoEwzM3YsP9Lg==,'
               'ZWYff8gDzYyiQXvAxzrnGM1LTotyoEjUpV4IgSfJmiI=,sPiSaKQA0mCZ2lhZ2U8XoQ==')
a.delete_chat()


