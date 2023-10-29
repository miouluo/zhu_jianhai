import json
import os
from config.setting import jd
def save_data(user_info):
    name = user_info['user_name' ]
    with open(fr'{jd}\{name}.json','w',encoding='utf-8')as f:
        json.dump(user_info,f)
def get_data(user_name):
    user = fr'{jd}\{user_name}.json'
    if os.path.exists(user):
        with open(user,'r',encoding='utf-8')as f:
            user_data = json.load(f)
            return user_data
