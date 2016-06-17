# coding=utf-8
# dumps(obj, skipkeys=False, ensure_ascii=True, check_circular=True, 
# allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False, **kw)
import json
dic = {"Gold Reserve": {u"\u91d1\u5e01\u50a8\u5907": "",\
u"\u91d1\u5e01\u50a8\u5907": 5}}                        #行太长加"\"换行
print json.dumps(dic, sort_keys=False)
print json.dumps(dic, ensure_ascii=False, sort_keys=False)  

#输出
# {"Gold Reserve": {"\u91d1\u5e01\u50a8\u5907": 5}}
# {"Gold Reserve": {"金币储备": 5}}
# 请按任意键继续. . .