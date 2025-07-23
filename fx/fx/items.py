# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FxItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    province = scrapy.Field()  # 通过meta获取省份名数据
    city_name = scrapy.Field()  # 通过meta获取城市名数据
    name = scrapy.Field()  # 楼盘名字
    price = scrapy.Field()  # 楼盘价格
    room = scrapy.Field()  # 几居室
    area = scrapy.Field()  # 面积
    sale = scrapy.Field()  # 是否在售
    origin_url = scrapy.Field()  # 详情页地址
