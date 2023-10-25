import time

time = time.strftime("%Y.%m")


class Teacher:

    school = '广州软件学院'

    def __init__(self, a, b, c, d, e, f, g):
        self.number = a
        self.age = b
        self.department = c
        self.phone = d
        self.time = e
        self.name = f
        self.basic_salary = g

    def output(self):
        print('%s的个人信息如下：' % self.name)
        print('*' * 20)
        print('工号：%d' % self.number)
        print('年龄：%d' % self.age)
        print('部门：%s' % self.department)
        print('电话：%d' % self.phone)
        print('入职日期：%s' % self.time)
        print('*' * 20)

    def get_salary(self, g, time2):

        current_time = time.strftime("%Y.%m")
        current_year = int(current_time.split('.')[0])
        join_year = int(self.time.split('.')[0])

        if current_year - join_year <= 10:
            salary = g + (current_year - join_year) * 100
        else:
            salary = g + 1000
        return salary

    def __del__(self):
        print('%s成员空间释放了' % self.name)


zhangsan = Teacher(1001, 26, '软件工程系', 13925438721, '2019.06', '张三', 1000)
zhangsan.output()
print(zhangsan.get_salary(1000, '2023.05'))

'''zhangsan = Teacher(1001, 26, '软件工程系', 13925438721, '2019.06', '张三')
lisi = Teacher(1201, 29, '网络技术系', 13926172345, '2017.10', '李四')
wangwu = Teacher(1154, 30, '数码媒体系', 13921783471, '2021.05', '王五')

zhangsan.output()
lisi.output()
wangwu.output()

del zhangsan
del lisi
del wangwu
'''