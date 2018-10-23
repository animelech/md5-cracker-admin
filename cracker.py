import socket
import time


class Cracker:
    def __init__(self,socket):
        self.name = ''
        self.socket = socket
        self.chunk = None
        self.alive = time.time()

    def send(self):
        return self.socket.send()

    def recv(self):
        return self.socket.recv()



def return_chunk(self,cracker):
    self.chunks.append(cracker.chunk)
    del cracker.chunk

def keep_thread(self):
    for c in self.crackers:
        if(time.time()- c.alive > )
