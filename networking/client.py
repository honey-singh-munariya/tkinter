import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
Host_name = socket.gethostname()

port = 12345
s.connect((Host_name,port))

