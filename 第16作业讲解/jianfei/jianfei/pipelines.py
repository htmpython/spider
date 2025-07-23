# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import csv

class QdJianfeiPipeline:
    def open_spider(self, spider):
        self.f = open('jianfe.csv', mode='a', encoding='utf-8', newline='')
        self.csv_write = csv.DictWriter(self.f, fieldnames=['title','put_time','source','lead'])
        self.csv_write.writeheader() # 写入表头

    def process_item(self, item, spider):
        if item['title'] == None and item['put_time'] == None and item['source'] == None and item['lead'] == None:
            pass
        else:
            self.csv_write.writerow(item)
        return item

    def close_spider(self, spider):
        self.f.close()