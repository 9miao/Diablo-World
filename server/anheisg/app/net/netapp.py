#coding:utf8
'''
Created on 2013-8-14

@author: lan
'''
from firefly.server.globalobject import GlobalObject
from firefly.utils.services import CommandService
from twisted.python import log
from twisted.internet import defer

class NetCommandService(CommandService):
    
    def callTargetSingle(self,targetKey,*args,**kw):
        '''call Target by Single
        @param conn: client connection
        @param targetKey: target ID
        @param data: client data
        '''
        
        self._lock.acquire()
        try:
            target = self.getTarget(0)
            if not target:
                log.err('the command '+str(targetKey)+' not Found on service')
                return None
            if targetKey not in self.unDisplay:
                log.msg("call method %s on service[single]"%target.__name__)
            defer_data = target(targetKey,*args,**kw)
            if not defer_data:
                return None
            if isinstance(defer_data,defer.Deferred):
                return defer_data
            d = defer.Deferred()
            d.callback(defer_data)
        finally:
            self._lock.release()
        return d
    
netservice = NetCommandService("loginService")

def netserviceHandle(target):
    """
    """
    netservice.mapTarget(target)

GlobalObject().netfactory.addServiceChannel(netservice)


@netserviceHandle
def Forwarding_0(keyname,_conn,data):
    '''消息转发，将客户端发送的消息请求转发给gateserver分配处理
    '''
    dd = GlobalObject().remote['gate'].callRemote("forwarding",
                                                  keyname,_conn.transport.sessionno,data)
    return dd

