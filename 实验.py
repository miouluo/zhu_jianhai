class Dog:
    def __init__(self,a):
        self.name=a
    def game(self):
        print("普通狗在地上跑着玩耍")
class xiaotianquan(Dog):
    def __init__(self,a):
        self.name=a
    def game(self):
        print("神犬在天上飞着玩耍")
class person:
    def __init__(self,a):
        self.name=a
    def game_with_dog(self,dog):
        dog.game()
        print("%s和%s快乐的玩耍"%(self.name,dog.name))
wangcai=xiaotianquan("飞天旺财")
smalldog=Dog("普通小狗")
xiaoming=person("小明")
xiaoming.game_with_dog(wangcai)
xiaoming.game_with_dog(smalldog)
