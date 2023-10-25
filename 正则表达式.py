import re
str1 = '2018 Amazon Jeff Bezos 1120'
print('(1)去掉字符串中的2018字符串', re.findall(r'Amazon Jeff Bezos 1120$', str1))
print('(2)将字符串中的数字提取出来', ' '.join(re.findall(r'\d+', str1)))
print('(3)将字符串的数字部分用【】括起来，得到字符串：', re.sub(r'(\d+)', r'【\1】', str1))
print('(4)去除字符串中的所有空格，得到字符串:', re.sub(r'(\s+)', '', str1).strip())
#a = re.sub(r'(\s+)', '', str1).strip()
#b = str(int(a*2))
print('(5)将字符串中的数字乘以2倍，得到字符串：')
str2 = '美国企业请注意，要么创新，要么杰夫·贝佐斯替你创新'
c = list(str2)
c.insert(21,'(Jeff Bezos)')
print('(6)将字符串‘bezos’添加到字符串，得到字符串:', ''.join(c))
