#coding:utf8

import os
if os.name!='nt' and os.name!='posix':
    from twisted.internet import epollreactor
    epollreactor.install()

import json,sys
from firefly.server.server import FFServer

if __name__=="__main__":
    args = sys.argv
    servername = None
    config = None
    if len(args)>2:
        servername = args[1]
        config = json.load(open(args[2],'r'))
    else:
        raise ValueError
    dbconf = config.get('db')
    memconf = config.get('memcached')
    sersconf = config.get('servers',{})
    masterconf = config.get('master',{})
    serconfig = sersconf.get(servername)
    ser = FFServer()
    ser.config(serconfig, dbconfig=dbconf, memconfig=memconf,masterconf=masterconf)
    ser.start()
    
    