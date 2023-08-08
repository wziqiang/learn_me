from bs4 import BeautifulSoup
from urllib import request

# 要请求的网络地址
url = 'https://www.hao123.com/'

# 请求网络地址得到html网页代码
html = request.urlopen(url)

# 整理代码
soup = BeautifulSoup(html, 'html.parser')

# 找出所有的 a 标签， 因为所有的链接都在 a 标签内
data = soup.find_all('a')

# 打开文件对象做持久化操作
file = open('D:/link.txt', mode='w', encoding='utf-8')

# 遍历所有的 a 标签， 获取它们的 href 属性的值和它们的 text
for item in data:
    if item.string is not None and item['href'] != 'javascript:;' and item['href'] != '#':
        print(item.string, item.get('href'))
        file.write(str.__add__(item.string, ' '))
        file.write(str.__add__(item['href'], '\n'))

file.close()