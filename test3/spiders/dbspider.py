import scrapy

from test3.items import Test3Item


class dbspider(scrapy.Spider):
    name = "dbspider"
    allowed_domains=["douban.com"]
    start_urls=[
    "https://movie.douban.com/top250"
    ]
    url="https://movie.douban.com/top250"
    def parse(self, response):
            item=Test3Item()
            selector=scrapy.Selector(response)
            Movies=selector.xpath('//div[@class="info"]')
            for eachMovie in Movies:
                title=eachMovie.xpath('div[@class="hd"]/a/span/text()').extract()
                fulltltle=''
                for each in title:
                    fulltltle+=each
                star=eachMovie.xpath('div[@class="bd"]/div[@class="star"]/span[@class="rating_num"]/text()').extract()
                item['title']=fulltltle
                item['star']=star
                yield item
            nextLink=selector.xpath('//span[@class="next"]/link/@href').extract()
            if nextLink:
                nextLink=nextLink[0]
                print nextLink
                yield scrapy.Request(self.url+nextLink,callback=self.parse)