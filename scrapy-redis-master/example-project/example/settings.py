# Scrapy settings for example project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#
SPIDER_MODULES = ['example.spiders']
NEWSPIDER_MODULE = 'example.spiders'
#
# USER_AGENT = 'scrapy-redis (+https://github.com/rolando/scrapy-redis)'

# 去重功能 断点续爬
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"

# 调度器
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
SCHEDULER_PERSIST = True
# SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderPriorityQueue"
# SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderQueue"
# SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderStack"

ITEM_PIPELINES = {
    # 'example.pipelines.ExamplePipeline': 300,
    'scrapy_redis.pipelines.RedisPipeline': 400,# 后面数据的保存默认是redis管道 默认开启
}

# 日志
LOG_LEVEL = 'DEBUG'

# Introduce an artifical delay to make use of parallelism. to speed up the
# crawl.
DOWNLOAD_DELAY = 1


"""需要自行配置数据库"""
# redis数据库配置
REDIS_HOST = '127.0.0.1'  # 本机地址 # 后续这个ip需要换成云服务器ip
REDIS_PORT = 6379  # 数据库端口, 传数字
