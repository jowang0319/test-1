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
        }
#         print(data_set)
        list.append(data_set)
print(list)

with open('test.csv', 'w') as csvfile:
    fieldnames = ["货币名称", "现汇买入价","现钞买入价","现汇卖出价","现钞卖出价","中行折算价","发布日期","发布时间"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for row in list:
        writer.writerow(row)
