import requests
from lxml import etree


# 请求头
headers= {
    'User-Agent': '...',
    'Cookie': '...',
    'Host': 'www.365kk.cc',
    'Connection': 'keep-alive'
}

# 小说主页
main_url = "http://www.365kk.cc/255/255036/"

# 使用get方法请求网页
main_resp = requests.get(main_url, headers=headers)

# 将网页内容按utf-8规范解码为文本形式
main_text = main_resp.content.decode('utf-8')

# 将文本内容创建为可解析元素
main_html = etree.HTML(main_text)
href = main_html.xpath('//html/body/div[4]/div[2]/div/div[2]/ul/li[contains(@class,"book-item")]/a/text()')
# # /html/body/div[4]/div[2]/div/div[2]/ul/li[1]/a
# # result = html.xpath('//li')
bookTitle = main_html.xpath('/html/body/div[4]/div[1]/div/div/div[2]/div[1]/h1/text()')[0]
# author = main_html.xpath('/html/body/div[4]/div[1]/div/div/div[2]/div[1]/div/p[1]/text()')[0]
# update = main_html.xpath('/html/body/div[4]/div[1]/div/div/div[2]/div[1]/div/p[5]/text()')[0]
# introduction = main_html.xpath('/html/body/div[4]/div[1]/div/div/div[2]/div[2]/text()')[0]
# print(href)
# print(href[0].xpath('//li/a/text()'))
# for item in href[0]:
#     print(item.xpath('//li/a/text()'))
# 当前页面链接
url = 'http://www.365kk.cc/255/255036/4147599.html'

resp = requests.get(url, headers)
text = resp.content.decode('utf-8')
html = etree.HTML(text)

title = html.xpath('//*[@id="container"]/div/div/div[2]/h1/text()')[0]
contents = html.xpath('//*[@id="content"]/text()')
print(title)
print(contents)
with open(bookTitle + '.txt', 'w', encoding='utf-8') as f:
    f.write(title)
    for content in contents:
        f.write(content  + '\n')
    f.close()
