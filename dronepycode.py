import socket
import pynput

pynput.keyboard.Controller()
keyboard = pynput.keyboard.Controller() #initialize keyboard input

TCP_IP = '192.168.43.22' # setting up WiFi communication
TCP_PORT = 5005
BUFFER_SIZE = 20
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()
while 1:
    data = conn.recv(BUFFER_SIZE)
    if not data: break
    if data == b'goright':
        for i in range(75): #repeat a good amount for program to pick up
            keyboard.type('d') #simulate 'D' keypress to move right
    elif data == b'goleft':
        for i in range(75):
            keyboard.type('a') #simulate 'A' keypress to move left
    else:
        print('drone within range')
    print("received data:", data)
    conn.send(data)  # echo
conn.close()
