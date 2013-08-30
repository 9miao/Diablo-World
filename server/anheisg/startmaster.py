#coding:utf8

import os
if os.name!='nt' and os.name!='posix':
    from twisted.internet import epollreactor
    epollreactor.install()

if __name__=="__main__":
    from firefly.master.master import Master
    master = Master()
    master.config('config.json','appmain.py')
    master.start()
    
    