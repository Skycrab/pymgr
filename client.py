#!/usr/bin/env python
#-*-encoding:UTF-8-*-

import hmac
import gevent
from gevent import monkey
monkey.patch_socket()

addr = ('localhost', 6667)


def send_request(module_name,request_headers):
    SECRE_KEY = "YI-LUO-KEHAN"
    socket = gevent.socket.socket()
    socket.connect(addr)
    request_headers['module'] = module_name
    request_headers['signature'] = hmac.new(SECRE_KEY, module_name).hexdigest()
    h = ["%s:%s" %(k, v) for k,v in request_headers.iteritems()]
    h.append('\n')
    request = '\n'.join(h)
    socket.send(request)
    print socket.recv(8192)
    socket.close()

if __name__ =="__main__":
    import sys
    if sys.argv[1] == 'start':
        send_request('SCAN_MODULE',{'action':'start','task_ids':'1'})
    else:
        send_request('SCAN_MODULE',{'action':'stop','task_ids':'1'})

    
    
