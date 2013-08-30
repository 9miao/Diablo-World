#coding:utf8
'''
Created on 2013-8-14

@author: lan
'''
from firefly.dbentrust.dbpool import dbpool
from twisted.python import log
from firefly.dbentrust import util


def updatePlayerDB(player):
    '''更新角色的数据库信息'''
    characterId = player.baseInfo.id
    props = {'level':player.level.getLevel(),'coin':player.finance.getCoin(),
             'exp':player.level.getExp(),'hp':player.attribute.getHp()}
    sqlstr = util.forEachUpdateProps('tb_character',props, {'id':characterId})
    conn = dbpool.connection()
    cursor = conn.cursor()
    count = cursor.execute(sqlstr)
    conn.commit()
    cursor.close()
    conn.close()
    if count >= 1:
        return True
    else:
        log.err(sqlstr)
        return False
    
def getCharacterIdByNickName(nickname):
    '''根据昵称获取角色的id
    @param nickname: string 角色的昵称
    '''
    sql = "select id from `tb_character` where nickname ='%s'"%nickname
    conn = dbpool.connection()
    cursor = conn.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result
    
    
    