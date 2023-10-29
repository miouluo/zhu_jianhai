from DB import db_handle


def register_info(user_name, password):
    user_info = {
        'user_name': user_name,
        'password': password,
        'money': 100,
        'account': []
    }
    user_data = db_handle.get_data(user_name)
    if user_data :
        return False,'注册失败，该用户已经存在'
    db_handle.save_data(user_info)
    return True, f'{user_name}注册成功'


def login_info(user_name, password):
    user_data = db_handle.get_data(user_name)
    if user_data:
        if password == user_data['password']:
            print('登录成功')
            return True, f'{user_name}登录成功,请开始使用'
        else:
            print('登录失败')
            return False, '密码错误，请重新输入'
    else:

        return False, '该用户不存在，请重新输入'


