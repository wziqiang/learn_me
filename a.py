import requests
import time
from lxml import etree
headers= {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    'Cookie': 'Hm_lvt_05ab1246121becb4b2d6c584d39acf40=1691379833; Hm_lpvt_05ab1246121becb4b2d6c584d39acf40=1691393333',
}
def request_dandan(url):
    # 小说主页
    print(url)
    main_url = url
    # 使用get方法请求网页
    main_text = requests.get(main_url, headers=headers).content.decode('utf-8')
    main_html = etree.HTML(main_text)
    title= main_html.xpath('//*[@id="ss-reader-main"]/div[2]/h1/text()')[0]
    contents = main_html.xpath('//*[@id="article"]/p/text()')
    with open('./a/'+title.replace('/', '-')+ '.txt', 'w', encoding='utf-8') as f:
        for content in contents:
            f.write(content  + '\n')
        f.close()
    
if __name__ == "__main__":
    for i in range(1432322, 1433646):
        urlid=None
        if i%2==0:
            urlid=i
        else:
            urlid=str(i-1) + '_2'
        url='https://www.bqgwxz.cc/book/5183/{}.html'.format(urlid)
        # # url='https://www.bqgwxz.cc/book/5183/1432322.html'
        # time.sleep(2)
        request_dandan(url)

