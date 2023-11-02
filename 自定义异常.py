# 自定义异常
class AgeError(Exception):
    def __int__(self,error_info):
        self.error_info =error_info
        def __str__(self):
            return self.error_info
age = int(input('请输入你的年龄：'))
if age<18 or age>200:
    raise AgeError('年龄不在成年人范围内。')
else:
        print('年龄是：',age)
