from bs4 import BeautifulSoup

f = open('demo.html', 'r', encoding='utf-8')
html = f.read()
f.close()
soup = BeautifulSoup(html,features='html.parser')

print(soup.prettify())
print(soup.title)
print(soup.title.name)
print(soup.title.string)
print(soup.title.parent.name)
print(soup.li)
print(soup.li['class'])
print(soup.find(id='my'))
print(soup.find_all('li'))
print(soup.find_all('li', class_='big'))
