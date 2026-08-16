import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
Host_name = socket.gethostname()
port = 12345

s.bind((Host_name,port))

s.listen(4)
while True:
    client, address = s.accept()
    print(address)
    


