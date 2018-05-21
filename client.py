import socket
import json
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 8888))

obj = {
    "action": "authenticate",
    "time": time.ctime(time.time()),
    "user": {
        "account_name": "C0deMaver1ck",
        "password": "CorrectHorseBatteryStaple"
    }
}

print('Send:', obj)

data = json.dumps(obj)
data_b = data.encode('utf-8')
s.send(data_b)

status_b = s.recv(1024)

print('Close\n' + '*' * 25)
s.close()

print('Ответ сервера: %s' % status_b.decode('utf-8'))
