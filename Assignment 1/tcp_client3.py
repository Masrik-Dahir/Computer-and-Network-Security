import socket
server_name = '127.0.0.1'
server_port = 12000
# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((server_name, server_port))
sentence = input('Input: ')
client.send(sentence.encode())
modifiedSentence = client.recvfrom(2048)
print (modifiedSentence[0].decode())
client.close()