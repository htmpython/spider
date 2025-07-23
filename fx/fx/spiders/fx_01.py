import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule
from scrapy_redis.spiders import RedisCrawlSpider,RedisSpider

from ..items import FxItem
class Fx01Spider(RedisSpider):  # 继承自普通爬虫的分布式功能
    name = "fx_01"
    # allowed_domains = ["bai.com"]
    # start_urls = ["fang:url12 https://www.fang.com/SoufunFamily.htm"]

    redis_key = 'fang:url12'  # 设置一个key, 后续是要监听数据库中的这个key任务

    def parse(self, response):
        # 省份信息
        trs = response.css('#c02 tr')  # 57个

        province = None
        for tr in trs:
            pro = tr.css('td[valign="top"]>strong::text').get()
            if pro:
                # 判断有没有获取到省份, 防止获取到空字符串
                if pro.strip():  # 二次判断空格符
                    province = pro

            # 海外获取
            if province == '其他':
                continue  # 跳过这一次循环

            # 获取城市信息
            city_a = tr.css('td a')  # 获取所有的城市标签
            for city in city_a:
                city_name = city.css('a::text').get()  # 城市名字
                city_url = city.css('a::attr(href)').get()  # 城市的url地址
                yield scrapy.Request(
                    url=city_url,
                    callback=self.get_city,
                    meta={
                        'province': province,  # 省份
                        'city_name': city_name,  # 城市名字
                    }
                )

    def get_city(self, response):
        """由省份列表页到新房详情页的过渡"""
        new_house_url = response.css('div[track-id="newhouse"] .s4Box>a::attr(href)').get()  # 新房详情页链接
        print('news', new_house_url)
        if new_house_url:
            yield scrapy.Request(
                url=new_house_url,
                meta={
                    'get': response.meta},
                callback=self.parse_newHouse,
                # 此函数没用到meta, 需要传到下一级
            )

    def parse_newHouse(self, response):
        """解析三级页面的函数"""
        province = response.meta.get('get').get('province')  # 通过meta获取省份名数据
        city_name = response.meta.get('get').get('city_name')  # 通过meta获取城市名数据

        lis = response.css('.nl_con>ul>li')
        for li in lis:
            name = li.css('.nlcd_name>a::text').get()  # 楼盘名字
            if name:
                name = name.strip()

            price = li.xpath(
                './/*[@id="lp_3416136428"]/div[1]/div[2]/div[5]/div/span/text()|.//*[@id="lp_3416136428"]/div[1]/div[2]/div[5]/div/em/text()')
            if price:
                price = ''.join(price)  # 价格

            room = li.css('.house_type>a::text').getall()  # 几居室
            if room:
                room = '-'.join(room)

            else:
                room = '无数据'

            area = li.css('.house_type::text').re('[\d~平米]+')  # 面积 数据有 正则匹配下 返回的列表
            if area:
                area = area[0]
            else:
                area = '无数据'

            sale = li.css('.inSale::text')  # 是否在售
            if sale:
                sale = sale.get()
            else:
                sale = '无数据'

            origin_url = li.css('.nlcd_name>a::attr(href)').get()  # 详情页的地址
            item = FxItem(province=province,city_name=city_name,name=name,price=price,room=room,
                          area=area,sale=sale,
                          origin_url=origin_url)


            print('itemssssssssssss',item)
            yield item












