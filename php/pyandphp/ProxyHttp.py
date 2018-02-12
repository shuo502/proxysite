# coding=utf-8
import socket
import requests
import datetime

# ProxyServerUrl = 'http://localhost/bass/proxy/Proxt.php'

try:
    import py.config
    url=py.config.phphost
except:
    pass
    url="127.0.0.1"


ProxyServerUrl = 'http://{}/php/pyandphp/index.php'.format(url)

print(ProxyServerUrl)
class Proxy:
    def __init__(self, addr):
        self.proxy = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.proxy.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.proxy.bind(addr)
        self.proxy.listen(50)
        self.inputs = [self.proxy]  # 一个异步通讯
        self.route = {}

    def start(self):
        print('strart http proxy')
        while 1:
            try:
                sock, addr = self.proxy.accept()
                self.handleData(sock)
                print(addr)
            except KeyboardInterrupt:
                print("Bye...")
                break

    def handleData(self, sock):
        rawdata = sock.recv(102400)
        req = requests.post(ProxyServerUrl, {'data': rawdata});
        sock.sendall(str.encode(req.text))

if __name__=='__main__':
    proxy = Proxy(('127.0.0.1', 8080))
    print( "proxy localhost  prot 8080" )
    proxy.start()
