import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import JianfeiItem

class Jianfei01Spider(CrawlSpider):
    name = "jianfei_01"
    # allowed_domains = ["baicim.com"]
    start_urls = ["https://jf.99.com.cn/jfqm/"]
    # 网址会自动补齐的
    rules = (Rule(LinkExtractor(allow=r"//jf.99.com.cn/jfqm/.*?.htm",
                                restrict_css=('div.DlistWfc>h2>a')),
                              callback="parse_item", follow=True),

             Rule(LinkExtractor(allow=r"230-\d+.htm",
                                restrict_css=('.list_page>span:last-of-type>a')),
                  callback="parse_next", follow=True)
             )

    def parse_item(self, response):
        # print(response.text)
        # 进行详情页的解析
        title = response.css('.wrap-title>h1::text').get() # 文章标题
        put_time = response.css('.wrap-title>p>span:nth-child(1)::text').get() # 发布时间
        source = response.css('.wrap-title>p>span:nth-child(2)::text').get() # 文章来源
        lead = response.css('.introduct>dl>dd::text').get() # 文章导语
        if lead:
            lead = lead.strip().replace('\n','').replace('\t','').replace('\r','')

        item = JianfeiItem(title=title,put_time=put_time,source=source,lead=lead)
        yield item

    def parse_next(self, response):
        # print(response.text)
        # 进行详情页的解析
        title = response.css('.wrap-title>h1::text').get() # 文章标题
        put_time = response.css('.wrap-title>p>span:nth-child(1)::text').get() # 发布时间
        source = response.css('.wrap-title>p>span:nth-child(2)::text').get() # 文章来源
        lead = response.css('.introduct>dl>dd::text').get() # 文章导语
        if lead:
            lead = lead.strip().replace('\n','').replace('\t','').replace('\r','')

        item = JianfeiItem(title=title,put_time=put_time,source=source,lead=lead)
        yield item




