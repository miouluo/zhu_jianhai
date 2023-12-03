import  re
f=open('广东外语外贸大学副校长刘建达教授应邀来校做专题讲座（图文）.txt','r',encoding='utf-8')
s=f.read()
f.close()
p=r'\'\n{7,}w+'
m=re.findall(p,s,re.UNICODE)
s2=re.sub(p,'',s,flags=re.U)
print(s2)
s3=re.sub(r'\n+',r'\n',s2,flags=re.U)
print(s3)

s='13712345678 13700000000 13677779985 137843'
p=r'\b137\d{8}\b'
m=re.findall(p,s)
print(m)

p=r'\b[a-zA-Z][0-9a-zA-Z]{0,4}\b'
s='a ab 3ab 4aa a3b4f aaaaa8 ab_x'
m=re.findall(p,s,re.I|re.U)
print(m)

p=r'<title>.*<title>'
s='<title>hdubhdbnd<title>'
m=re.findall(p,s,re.I|re.U)
print(m)


s='尝一尝、拍一拍、试一试'
p=r'((\w)一\2)'
m=re.findall(p,s,re.U)
print(m)