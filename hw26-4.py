__author__ = 'John'
# myserver.py for server
from socketserver import ThreadingTCPServer, StreamRequestHandler
import datetime
import threading
import time
import random
PORT = 12000


class MyRequestHandler(StreamRequestHandler):
    def handle(self):
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        conn = self.request

        buf = conn.recv(1024)
        if not buf:
            print('{0}, connection from {1}, message: nothing'.format(now, self.client_address))
        else:
            print('{0}, connection from {1}, message: {2}'.format(now, self.client_address, buf))


server = ThreadingTCPServer(('127.0.0.1', PORT), MyRequestHandler)
print('listening on port', PORT)
server.serve_forever()


class ClientThread(threading.Thread):
    def run(self):
        for n in range(0, 60):
            print('[{0}] Thread {1:03d}'.format(
                self.getName(),
                random.randrange(1, 999))
            )
            time.sleep(1)

th = []
for i in range(3):
    th.append(ClientThread())

for i in th:
    i.start()

for i in th:
    i.join()

if __name__ == "__main__":
    pass
