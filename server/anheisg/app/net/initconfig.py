#coding:utf8
'''
Created on 2013-8-14

@author: lan
'''
from firefly.server.globalobject import GlobalObject
from firefly.netconnect.datapack import DataPackProtoc


def callWhenConnLost(conn):
    dynamicId = conn.transport.sessionno
    GlobalObject().remote['gate'].callRemote("netconnlost",dynamicId)

GlobalObject().netfactory.doConnectionLost = callWhenConnLost
dataprotocl = DataPackProtoc(78,37,38,48,9,0)
GlobalObject().netfactory.setDataProtocl(dataprotocl)



def loadModule():
    import netapp
    import gatenodeapp