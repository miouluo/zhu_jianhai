def zhishu(x):
    x = eval(input('请输入数据:'))
    if x <= 1:
        print('输入数据错误，请重新输入')
    elif x == 2:
        print('%d是质数' % x)
    else:
        for i in (3, x + 1):
            if x % i == 0:
                return '%d不是质数' % x
            else:
                return '%d是质数' % x
