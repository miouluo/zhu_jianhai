'''print("__________________正则表达式___________________")
print("方法一：先将正则表达式模式编译成一个正则表达式对象，再匹配的正则表达式，返回匹配到的对象，只匹配一个")
import re
string = "123456789@email.com"
string1 = "d123456789@email.com"
pattern = r'\d+@email.com'
prog = re.compile(pattern)
result = prog.match(string)
result1 = prog.match(string1)
print(result)
print(result1)
print("方法二：先将正则表达式模式编译成一个正则表达式对象，再搜索查找与正则表达式匹配字符串，匹配到第一个位置")
import re
string = """
hello's email:123456789@qq.com
world's email:987654321@email.com
"""
pattern =r'\d+@\w+.com'
prog = re.compile(pattern)
result = prog.search(string)
print(result)
print("方法三：先将正则表达式模式编译成一个正则表达式对象，再用findall匹配到正则表达式的非重复子字符串，并返回列表")
import re
string = """
hello's email:123456789@email.com
world's email:987654321@email.com
"""
pattern = r'\d+@email.com'
prog = re.compile(pattern)
result = prog.findall(string)
print(result)
print("方法四：先将正则表达式模式编译成一个正则表达式对象，再用finditer匹配到正则表达式的非重复子字符串，并返回迭代器")
import re
string = """
hello's email:123456789@email.com
world's email:987654321@email.com
"""
pattern = r'\d+@email.com'
result = prog.finditer(string)
print(result)
print("方法五：正则表达式替换，re.sub(pattern, repl, string, count=0, flags=0)使用repl替换所有在string中与pattern相匹配的子字符串")
import re
string = """
hello's email:123456789@email.com
world's email:987654321@email.com
"""
pattern = r'\d+@email.com'
prog = re.compile(pattern)
string = re.sub(prog, "none", string)
print(string)

print("__________________利用正则表达式及re.split()动态分割___________________")
import re
string = """hello's email:123456789@email.com
world's email:987654321@email.com
apple's email:zhangfei@email.com
"""
pattern = r'\d+'
prog = re.compile(pattern)
string = re.split(prog, string)
print(string)

print("__________________利用正则表达式对输入的邮箱地址进行校验___________________")
import re
text = input("please input your email address：\n")
if re.match(r'^[0-9a-za-z_]{0,19}@[0-9a-za-z]{1,13}\.[com,cn,net]{1,3}$',text):
  print('email address is right!')
else:
  print('please reset your right email address!')
'''
'''import re
s="我叫小明，我的性别为女，籍贯为广东省广州市，哈哈你\
我的身份证号是429812199708046923，电话为13949636915，邮箱为1386606403@qq.com,我妈妈的身份证号是42981219710305392X，哈哈哈，身份证号是"
s_find1=re.findall(r"[女广东]",s)#匹配"女"或"广"或"东"
print("1:",s_find1)
s_find2=re.findall(r"[^女广东]",s)#匹配除了"女"或"广"或"东"之外的字符
print("2:",s_find2)
s_find3=re.findall(r"广[东州]",s)#匹配"广东"或"广州"
print("3:",s_find3)
s_find4=re.findall(r"身份证号是[0-9]*",s)#匹配"身份证号是"后跟0个或多个数字,"身份证号是\d*"也可
print("4:",s_find4)
s_find5=re.findall(r"1386{2}",s)
print("5:",s_find5)
s_find6=re.findall(r"1386{1,}",s)
print("6:",s_find6)
s_find7=re.findall(r"1386{3,4}",s)
print("7:",s_find7)
s_find8=re.findall(r"身份证号是(429812(\d{8})\d+)",s)#匹配身份证号及生日
print("8:",s_find8)
s_find9=re.findall(r"身份证号是(\d{17}[\da-zA-Z])",s)#匹配身份证号
print("9:",s_find9)
s_find10=re.findall(r"身份证号是(\d{17}(\d，|[a-zA-Z]，))",s)#匹配身份证号及最后一个字符
print("10:",s_find10)
s_find11=re.findall(r"身份证号是(\d{17}(?:\d，|[a-zA-Z]，)(?#用（?:）格式表示分组但不捕获))",s)#匹配身份证号及最后一个字符,但不输出最后一个字符,其中(?#...)为注释
print("11:",s_find11)
s_find12=re.findall("哈哈(?=哈)",s)#匹配哈哈后面是哈的哈哈
print("12:",s_find12)
s_find13=re.findall("哈(?!哈哈)",s)#匹配不在哈哈前面的哈
print("13:",s_find13)
s_find14=re.findall(r"身份证号是\d+?",s)#非贪婪匹配
print("14:",s_find14)
'''
import time

class Teacher:
    school = '广州软件学院'

    def __init__(self, number, age, department, phone, time, name):
        self.number = number
        self.age = age
        self.department = department
        self.phone = phone
        self.time = time
        self.name = name
        self.basic_salary = 0
        self.annual_merit_salary = 0

    def output(self):
        print('%s的个人信息如下：' % self.name)
        print('*' * 20)
        print('工号：%d' % self.number)
        print('年龄：%d' % self.age)
        print('部门：%s' % self.department)
        print('电话：%d' % self.phone)
        print('入职日期：%s' % self.time)
        print('*' * 20)

    def get_salary(self, year2):
        current_time = time.strftime("%Y.%m")
        current_year = int(current_time.split('.')[0])
        join_year = int(self.time.split('.')[0])
        if current_year - join_year <= 10:
            self.basic_salary += (current_year - join_year) * 100
        else:
            self.basic_salary += 1000
        self.annual_merit_salary = self.basic_salary * 0.1
        return self.basic_salary + self.annual_merit_salary

    def __del__(self):
        print('%s成员空间释放了' % self.name)


zhangsan = Teacher(1001, 26, '软件工程系', 13925438721, '2019.06', '张三')
lisi = Teacher(1201, 29, '网络技术系', 13926172345, '2017.10', '李四')
wangwu = Teacher(1154, 30, '数码媒体系', 13921783471, '2021.05', '王五')

zhangsan.output()
lisi.output()
wangwu.output()

print(zhangsan.get_salary('2023.05'))
print(lisi.get_salary('2023.05'))
print(wangwu.get_salary('2023.05'))

del zhangsan
del lisi
del wangwu
