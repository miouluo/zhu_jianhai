def zhishu(y):
    y = eval(input('请输入数据:'))
    if y <= 1:
        print('输入数据错误，请重新输入')
    elif y == 2:
        print('%d是质数' % y)
    else:
        for i in (3, y + 1):
            if y % i == 0:
                return '%d不是质数' % y
            else:
                return '%d是质数' % y

