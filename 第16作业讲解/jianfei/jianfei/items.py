# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JianfeiItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    put_time = scrapy.Field()
    source = scrapy.Field()
    lead = scrapy.Field()

