#Exercise 5: (Advanced) Change the socket program so that it only shows
#data after the headers and a blank line have been received. Remember
#that recv receives characters (newlines and all), not lines.

import socket
mysock= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1 : break
    x = data.decode()
    if '\r\n\r\n' in x:
        y = x.find('\r\n\r\n') + 4 # 4 is added to neglect the characters \r\n\r\n
        #print(y)
        print(data.decode()[y:])
    else :
        print(data.decode(), end= "")
mysock.close()
