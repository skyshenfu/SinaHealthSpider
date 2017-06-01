import scrapy

from test3.items import Test3Item
import sys
sys.path.append("..")
import data as  Data
from Sina import getUrls
index=0
class sinaspider(scrapy.Spider):
    name = "sinaspider"
    allowed_domains = ["sina.com.cn"]
    getUrls(100)
    start_urls = Data.get_urlSourceValue()
    srcls = Data.get_urlSourceValue()
    titlels=Data.get_nameSourceValue()
    def parse(self, response):
        global index
        item = Test3Item()
        selector = scrapy.Selector(response)
        News = selector.xpath('//div[@class="content"]')
        for newsitem in News:
            allimg = ''
            alltext = ''
            imgs = newsitem.xpath('div[@class="img_wrapper"]/img/@src').extract()
            texts = newsitem.xpath('p/text()').extract()
            for img in imgs:
                allimg += str(img) + "\n"
            for text in texts:
                alltext += text + "\n"
            item['imgurl']=allimg
            item['textdetail']=alltext
            item['index']=str(index+1)
            item['title']=self.titlels[index]
            item['srcurl']=self.srcls[index]
            index+=1
            yield item
