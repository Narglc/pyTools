#coding:utf-8

import redis

class RedisHelper:
    def __init__(self,_db = 0) -> None:
        self.r      = redis.Redis(host='localhost',port=6379,db=_db)
        self.pipe   = self.r.pipeline(transaction=True)
    
    def hmset(self,key,dicts):
        for field,value in dicts.items():
            self.pipe.hset(key,field,value)
        self.pipe.execute()

    def exists(self,key):
        return self.r.exists(key)
    

'''
# 使用示例:
helper = RedisHelper()
helper.hmset("pics_test2",{"name":"cos_play_2", "count":66})
print(helper.exists("pics_test2"))
'''