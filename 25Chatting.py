# 25Chatting.py

from socket import *

PORT = 10000

def udpClient():
    client = socket(AF_INET, SOCK_DGRAM)  # UDP : User DataGram Protocol
    client.sendto('Hello I am Python'.encode(), ("127.0.0.1", PORT))
    s, addr = client.recvfrom(1024)
    print(s)

if __name__ == "__main__":
    udpClient()


