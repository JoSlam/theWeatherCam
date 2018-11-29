import socket
import os
import shlex
from datetime import datetime
from functools import cmp_to_key
from subprocess import Popen


def getData():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '0.0.0.0'
    port = 4016
    SIZE = 4096
    s.bind((host, port))
    s.listen(5)

    while True:
        print('Waiting for connection on port: ', port)
        connection, client_address = s.accept()
        partCount = 1

        signal = connection.recv(SIZE).decode()                 #receive initial request
        if signal.startswith('READY'):
            connection.send(b'READY TO RECV')                   #send ready signal
            print('Ready to receive.')
            name = connection.recv(SIZE).decode()               #receive name
            writeF = open('api/static/weather_images/' + name, 'wb')       #open file with received name
            print('Filename: {0}'.format(name))

            #receive image data
            data = connection.recv(SIZE)
            while (data):
                print('Receiving image part: ', partCount)
                partCount += 1
                writeF.write(data)
                data = connection.recv(SIZE)
            writeF.close()
            line = 'python manage.py upload_img ' + name
            args = shlex.split(line)
            proc = Popen(args)





# def sortFolder():
#     filePath = 'images'
#     names = []
#     for file in os.listdir(filePath):       #error check for jpeg file ext on insert
#         file_dat = os.path.splitext(file)
#         print(file_dat)
#         names.append({'date': datetime.strptime(file_dat[0], "%d-%m-%Y-%H-%M"), 'file_name':file_dat[0], 'ext': file_dat[1]})
#     return sorted(names, key=cmp_to_key(comp_dates), reverse=True)

# def comp_dates(date1, date2):
#     return 1 if date1['date'] > date2['date'] else -1 if date2['date'] > date1['date'] else 0


getData()
