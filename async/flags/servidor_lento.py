#!/usr/bin/env python
# coding: utf-8

"""
Este servidor introduz atrasos nas requisições GET.
"""

import SimpleHTTPServer
import SocketServer
import time

PORT = 8000

ATRASO = 2 # em segundos

class HandlerLento(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        print 'dormindo %ss...' % ATRASO
        time.sleep(ATRASO)
        SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

httpd = SocketServer.TCPServer(('', PORT), HandlerLento)

print 'servindo na porta', PORT
httpd.serve_forever()
