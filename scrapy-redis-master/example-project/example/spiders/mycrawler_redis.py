from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

from scrapy_redis.spiders import RedisCrawlSpider


class MyCrawler(RedisCrawlSpider):
    """Spider that reads urls from redis queue (myspider:start_urls)."""
    name = 'mycrawler_redis'
    # scrapy的标志 后面的任务发布启动都需要通过这个redis_key进行运行代码
    redis_key = 'mycrawler:start_urls'
    # 匹配首页的网址规则
    rules = (
        # follow all links
        Rule(LinkExtractor( allow=r'/author/.*'), callback='parse_page', follow=True),
    )

    # def __init__(self, *args, **kwargs):
    #     # Dynamically define the allowed domains list.
    #     domain = kwargs.pop('domain', '')
    #     self.allowed_domains = filter(None, domain.split(','))
    #     super(MyCrawler, self).__init__(*args, **kwargs)

    def parse_page(self, response):
        # print(response.text)
        # 标题
        data = {
          'title' : response.css('.author-details>h3::text').get(),
          'time_data': response.css('.author-born-date::text').get()

        }
        return data


