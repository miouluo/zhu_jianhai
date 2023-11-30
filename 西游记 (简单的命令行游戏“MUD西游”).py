#!/usr/bin/env python
# coding: utf-8

# ### MUD version 3

# In[ ]:


class NPC:
	''' 游戏NPC '''
	def __init__(self, name):
		self.name = name
	
	def __str__(self):
		''' 为地图类where调用生成对象信息 '''
		return '['+self.name+']'
	
	def say(self):
		return self.name  +'在此！'
class MyMap:
	''' 地图类 '''
	def __init__(self):
		# 初始化一维地图元素
		self.line = [NPC("孙悟空"), NPC("猪八戒"), NPC("沙和尚"), NPC("白龙马"), NPC("妖怪婆")]
		self.index = 0	# 玩家位置
		
	def dialog(self):
		face=self.line[self.index-1]
		print(face.say())
		
	def foreward(self):
		self.index -= 1
		if self.index<=0: 
			self.index=0
	
	def backward(self):
		self.index += 1
		if self.index>=len(self.line): 
			self.index=len(self.line)
	
	def where(self):
		before = "我在最前面" if self.index<=0 else "我前面是"+str(self.line[self.index-1])
		after = "我在最后面" if self.index>=len(self.line) else "我后面是"+str(self.line[self.index])
		print(before + "，" + after + '：')
class Mud:
	''' 游戏交互辅助类 '''
	def __init__(self):
		self.mymap = MyMap()
		
	def run(self):
		msg = "[w] 前进\n[s] 后退\n[q] 退出\n [ ]空格对话\n";
		while True:
			self.mymap.where()
			action = input(msg)
			if action=='w': self.mymap.foreward()
			elif action=='s': self.mymap.backward()
			elif action==' ': self.mymap.dialog()
			elif action=='q': break
	
if __name__ == '__main__':
	mud = Mud()
	mud.run()


# ### MUD version 2

# In[ ]:





# In[ ]:




