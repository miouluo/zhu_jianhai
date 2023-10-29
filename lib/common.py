from core import src


def is_login(f):
    def check(*args,**kwargs):
        if src.login_user:
            print('您已登录，欢迎使用')
            f(*args,**kwargs)
        else:
            print('您还未登录，请登录后再使用该功能')
            src.login()
    return check
