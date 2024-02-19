import socket
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()                        
port = 9999
s.connect((host, port))                              
outp = ""

def receive_msg():
    while True:  
        outp=s.recv(1024)
        outp = outp.decode('ascii')
        print(outp)

def send_msg():
    while True:
        text = input().split("\n")[-1]
        s.send(text.encode('ascii'))

threading.Thread(target=receive_msg).start()
threading.Thread(target=send_msg).start()

while True:
    continue

   
s.close()
