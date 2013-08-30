#coding:utf8
'''
Created on 2013-8-14

@author: lan
'''
from firefly.server.globalobject import GlobalObject,remoteserviceHandle


@remoteserviceHandle('gate')
def pushObject(topicID,msg,sendList):
    GlobalObject().netfactory.pushObject(topicID, msg, sendList)