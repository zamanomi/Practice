#Exercise 2: Change your socket program so that it counts the number
#of characters it has received and stops displaying any text after it has
#shown 3000 characters. The program should retrieve the entire document and count the total
#number of characters and display the count of the number of characters at the end of the document.
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

length = 0
while True :
    data = mysock.recv(512)
    length = len(data) + length
    if len(data) < 1 or length >= 3000 :
        break
    print(data.decode(), end ="")
mysock.close()
print('Data length: ', length)
