import socket
import time

class UDPClient:

    def __init__(self,host, port):
        self.host = host    #server address
        self.port = port    #server port
        self.socket = None #socket

    def configure_client(self):
        print('Creating socket...')
        self.socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        print('Socket created')

    def handle_request(self, name):
        while(True):
            byteToSend = str.encode(name)
            self.socket.sendto(byteToSend, (self.host,self.port))

            result = self.socket.recvfrom(1024)

            mess = result[0].decode('utf-8')
            print(mess,'\n\n')
            time.sleep(0.55)

def main():

    udpClient = UDPClient('127.0.0.1',4444)
    udpClient.configure_client()
    udpClient.handle_request('Fudio')
    input("Press Enter to exit...")

if __name__ == '__main__':
    main()
