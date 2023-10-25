student = {'name': '张三', 'age': '20', 'gender': '男', 'class': '网工1班', 'city': '广州'}
while True:
    try:
        a = str(input('请输入键值：'))
        if a == 'exit':
            print('退出成功')
            exit()
        else:
            print(student[a])
    except KeyError:
        print('发生了异常，请重新输入')
