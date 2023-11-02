class Employee:                         #员工类，作为基类
    def __init__(self,name):
        self.name = name                #定义属性name
    def get_salary(self):               #定义获取薪资的方法
        pass
class Manager(Employee):                #定义产品经理类，继承Employee类
    def __init__(self,name,salary=15000):
        super().__init__(name)          #继承父类属性
        self.salary = salary            #定义薪资salary
    def get_salary(self):               #重写父类方法
        return self.salary
    def __str__(self):                  #重写__str__()方法
        return f"{self.name}的薪资是{self.get_salary()}"
class Programmer(Employee):             #定义程序员类，继承Employee类
    def __init__(self, name, base_salary=100000, over_time=0):
        super().__init__(name)          #继承父类属性
        self.base_salary = base_salary  #定义基础工资base_salary
        self.__over_time = over_time    #定义加班时长
    def get_salary(self):               #重写父类方法
        if self.__over_time < 0:
            raise ValueError("工作时长的输入有误")
        elif self.__over_time > 20:
            self.__over_time = 20       #加班时长不能超过20小时，超出20小时不计入薪资
        return self.base_salary + 100 * self.__over_time
    def __str__(self):                  #重写__str__()方法
        return f"{self.name}的薪资是{self.get_salary()}"
class SoftTest(Employee):               #定义测试工程师类，继承Employee类
    def __init__(self,name,base_salary=200000,bug_num=0):
        super().__init__(name)          # 继承父类属性
        self.base_salary = base_salary  #定义基础工资base_salary
        self.bug_num = bug_num          #定义发现的错误个数bug_num
    def get_salary(self):               #重写父类方法
        return self.base_salary + 5 * self.bug_num
    def __str__(self):                  #重写__str__()方法
        return f"{self.name}的薪资是{self.get_salary()}"
def main():                             #定义计算所有员工工资的函数
    employee_list = [
        Manager("宋江"),Manager("吴用"),Manager("公孙胜",10000),
        Programmer("花荣"),Programmer("武松",10000,10),Programmer("林冲",13000,30),
        SoftTest("朱武"),SoftTest("蒋敬"),SoftTest("柴进",9000,100)
    ]
    for emp in employee_list:
        if isinstance(emp,Programmer):
            print("程序员：",emp)
        elif isinstance(emp,Manager):
            print("产品经理：",emp)
        else:
            print("测试工程师：",emp)
if __name__ == "__main__":
    main()
