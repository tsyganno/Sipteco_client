import requests
import base64


class Sipteco_client:

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


header_init = {'X-Tasktest-Token': 'f62cdf1e83bc324ba23aee3b113c6249'}
path = 'chat/spare?crm=TEST&domain=test'
link = 'https://dev.whatsapp.sipteco.ru/v3/'
TOKEN = requests.get(link + path, headers=header_init)
print(TOKEN.text)
''' Получение TOKEN и ID - {"id":9,"token":"Es7OhIYSuG2N-klS","instanceId":"2a01:4f8:c17:ac8:3::a"}'''

a = Sipteco_client('9', "Es7OhIYSuG2N-klS", {'X-Tasktest-Token': 'f62cdf1e83bc324ba23aee3b113c6249'})
a.qr_code()


'''Расшифровка qr-кода: 1@EBtGPr5o39eZt6KLMaMzFIb2Vb9nUOifOubFEcvQjkdi0sRWAJRasOdLOrdRjnNyTV/K3WFre9pk1w==,' \
'JyTHquzAOaolW++R3qOudjBICrstbpQLWPnaGDmB/wQ=,CTldrrL6n62L6t0c0OcEWQ=='''


