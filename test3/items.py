# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Test3Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    imgurl=scrapy.Field()
    textdetail=scrapy.Field()
    title=scrapy.Field()
    srcurl=scrapy.Field()
    index=scrapy.Field()