import re

html_content = """
<html>
<head>
<title>BeautifulSoup演示网页</title>
<style>
.big {font-size:150%; color:red}
#info {font-size:80%; text-align:right}
</style>
</head>
<body>
<h1>BeautifulSoup 的三板斧</h1>
<ul>
  <li class='big'>find_all('tag') 搜索当前所有的tag标签的集合</li>
  <li class='big'>find("tag") 返回一个标签（这个方法用的少）</li>
  <li>select("") 可以按标签查找，用的多是按标签逐层查找筛选元素</li>
</ul>
<p id='info'>制作：2023-11-15 07:09 于专家楼</p >
</body>
</html>
"""

# 查找<title>...</title>标题元素
title_pattern = re.compile(r'<title>(.*?)</title>', re.IGNORECASE)
title_match = title_pattern.search(html_content)
if title_match:
    print("标题元素为:", title_match.group(1))
else:
    print("未找到标题元素")

# 查找所有的 <...> 标记
tag_pattern = re.compile(r'<[^>]+>')
tags = tag_pattern.findall(html_content)
print("所有的标记为:", tags)

# 查找“yyyy-mm-dd hh:mm”格式的日期
date_pattern = re.compile(r'\d{4}-\d{1,2}-\d{1,2} \d{1,2}:\d{2}')
date_match = date_pattern.search(html_content)
if date_match:
    print("日期为:", date_match.group())
else:
    print("未找到日期")