# -*- coding: utf-8 -*-

import scraperwiki
import lxml.html
import csv
import sys

reload(sys)
sys.setdefaultencoding('utf-8') 

html = scraperwiki.scrape("http://www.boc.cn/sourcedb/whpj/index.html")

# # Find something on the page using css selectors
root = lxml.html.fromstring(html)
root.cssselect("table")
print(root.cssselect("table"))

my_table = root.cssselect("table")[1]
page_url = "http://www.boc.cn/sourcedb/whpj/index.html"

list = []

for tr in my_table.cssselect("tr"):
    tds = tr.cssselect("td")
#     print(len(tds))
    if len(tds) == 8:
        data_set = {
            "货币名称":tds[0].text_content(),
            "现汇买入价":tds[1].text_content(),
            "现钞买入价":tds[2].text_content(),
            "现汇卖出价":tds[3].text_content(),
            "现钞卖出价":tds[4].text_content(),
            "中行折算价":tds[5].text_content(),
            "发布日期":tds[6].text_content(),
            "发布时间":tds[7].text_content(),
            "链接":page_url
        }
#         print(data_set)
        list.append(data_set)
print(list)

pre_url = "http://www.boc.cn/sourcedb/whpj/index_"
post_url = ".html"

for i in range (1,21):
    page_url = pre_url + str(i) + post_url
    html = scraperwiki.scrape(page_url)
    
    root = lxml.html.fromstring(html)
    root.cssselect("table")
       
    my_table = root.cssselect("table")[1]

    for tr in my_table.cssselect("tr"):
        tds = tr.cssselect("td")
    #     print(len(tds))
        if len(tds) == 8:
            data_set = {
                "货币名称":tds[0].text_content(),
                "现汇买入价":tds[1].text_content(),
                "现钞买入价":tds[2].text_content(),
                "现汇卖出价":tds[3].text_content(),
                "现钞卖出价":tds[4].text_content(),
                "中行折算价":tds[5].text_content(),
                "发布日期":tds[6].text_content(),
                "发布时间":tds[7].text_content(),
                "链接":page_url
            }
    #         print(data_set)
            list.append(data_set)
    
#     print(page_url)

table = scraperwiki.sqlite.save(unique_keys=['货币名称'], data=list)


