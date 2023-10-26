
#for循环
str='python'
for s in str:
    print(s)

#while循环
sum=0
m=10
while m>0:
    sum=sum+m
    m=m-1
print (sum)

#break语句
str='python'
for s in str:
    if s =='o':
        break
    print(s)

#continue语句
str='Python'
for s in str:
    if s =='o':
        continue
    print(s)

#pass语句
if true:
    pass