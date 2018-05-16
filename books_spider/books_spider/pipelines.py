# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class BooksSpiderPipeline(object):
    def open_spider(self, spider):
        self.conn = sqlite3.connect ("book.sqlite") 
        self.cur = self.conn.cursor() 
        self.cur.execute("create tab;e of not exists books title varchar(100), content text, time varchar(50)")

    def close_spider(self, spider):
        self.conn.commit()
        self.conn.close()

    def process_item(self, item, spider):
        sql='insert'
        self.cur.execute(sql)
        return item
