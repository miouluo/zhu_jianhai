from api import user_i
from lib.common import is_login
from api import bank_i


# 1.注册
def register():
    while 1:
        user_name = input('请设置用户名>>>')
        password = input('请设置密码>>>')
        re_password = input('请再次确认密码>>>')
        if password == re_password:
            flag, msg = user_i.register_info(user_name, password)
            if flag:
                print(msg)

                break
            else:
                print(msg)
        else:
            print('密码不一致，请重新注册')


# 2.登录
login_user = None


def login():
    while 1:
        user_name = input('请输入用户名>>>')
        password = input('请输入密码>>>')
        flag, msg = user_i.login_info(user_name, password)
        if flag:
            print(msg)
            global login_user
            login_user = user_name
            break
        else:
            print(msg)


# 3.余额
@is_login
def check_money():
    money = bank_i.select_money(login_user)
    print(f'用户:{login_user}当前余额:{money}元')


# 4.存款
@is_login
def save_money():
    while 1:
        money = float(input('请输入存款金额'))
        flag, msg = bank_i.resave(login_user, money)
        if flag:
            print(msg)
            break
        else:
            print(msg)


# 5.取款
@is_login
def get_money():
    while 1:
        money = float(input('请输入取款金额'))
        flag, msg = bank_i.take_money(login_user,money)
        if flag:
            print(msg)
            break
        else:
            print(msg)
# 6.账单
@is_login
def account():
    acc = bank_i.get_acc(login_user)
    if acc:
        for i in acc:
            print(i)
    else:
        print('目前没有流水账单')



fun_select = {
    0: ['退出', exit],
    1: ['注册', register],
    2: ['登录', login],
    3: ['查询余额', check_money],
    4: ['存款', save_money],
    5: ['取款', get_money],
    6: ['流水账单', account]
}


def run():
    while 1:
        print('欢迎使用蟹老板牌ATM机')
        for i in fun_select:
            print(i, fun_select[i][0])
        select = int(input("请选择您要进行的操作>>>"))
        if select in fun_select:
            fun_select[select][1]()
        else:
            print("不存在该功能，请重新输入")
