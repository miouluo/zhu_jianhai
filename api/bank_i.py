import time
from DB import db_handle


def select_money(user_name):
    user_data = db_handle.get_data(user_name)
    return user_data['money']


now_time = time.strftime('%x %X')


def take_money(user_name, money):
    user_data = db_handle.get_data(user_name)
    if user_data['money'] >= money:
        user_data['money'] -= money
        acc_info = f'北京时间:{now_time},用户:{user_name},取款:{money}元,当前余额:{user_data["money"]}'
        user_data['account'].append(acc_info)
        db_handle.save_data(user_data)
        return True,acc_info
    else:
        return False, '取款失败，余额不足，请重新操作'

def resave(login_user, money):
    user_data = db_handle.get_data(login_user)
    user_data['money'] += money
    acc_info = f'北京时间:{now_time},用户:{login_user},存款:{money}元,当前余额:{user_data["money"]}'
    user_data['account'].append(acc_info)
    db_handle.save_data(user_data)
    return True,acc_info

def get_acc(login_user):
    user_data = db_handle.get_data(login_user)
    return user_data['account']