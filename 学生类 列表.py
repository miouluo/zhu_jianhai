'''
class Student(object):
    def __init__(self, number, name):
        self.number = number
        self.name = name

     #    self.score = score

    def __getitem__(self, item):
        print(item)
        return self.name[item]

    def __setitem__(self, key, value):
        self.name[key] = value


    def __delitem__(self, key):
        del self.name[key]

#   score = [chinese, math, english, physics,chemistry, history, geography, biology]


zhangsan = (100001, '张三')
lisi = (100002, '李四')
score1 = Student('张三', [91, 87, 81.5, 69, 97, 88, 69, 78.5])
score2 = Student('李四', [95, 91, 88, 87, 97.5, 69.5, 92, 78.5])

print(zhangsan, score1.name)
print(lisi, score2.name)
'''


class Student:
    def __init__(self, stu_id, name, scores):
        self.stu_id = stu_id
        self.name = name
        self.scores = scores

    def __getitem__(self, key):
        return self.scores[key]

    def __setitem__(self, key, value):
        self.scores[key] = value

    def __delitem__(self, key):
        del self.scores[key]

    def __str__(self):
        return f"{self.stu_id} {self.name} {self.scores}"
#   使用 f-string 的语法，将学生的学号、姓名和成绩列表转换为一个字符串

zhangsan = Student(100001, "张三", [91, 87, 81.5, 69, 97, 88, 69, 78.5])
lisi = Student(100002, "李四", [95, 91, 88, 87, 97.5, 69.5, 92, 78.5])
zhangsan[0] = 102
del lisi[5:]
print(zhangsan)
print(lisi)
