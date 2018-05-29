import json
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 8888))
s.listen(5)

while True:
    client, addr = s.accept()
    print('Connected:', addr)

    data_b = client.recv(1024)
    obj_j = data_b.decode('utf-8')
    print('Obj:', obj_j)
    obj = json.loads(obj_j)

    if obj['action'] == 'authenticate':
        msg = 'RESPONSE: 200'
        client.send(msg.encode('utf-8'))
    else:
        msg = 'RESPONSE: 400 ERROR: Неверный запрос'
        client.send(msg.encode('utf-8'))
    print('Close')
    print('*' * 150)
    client.close()
