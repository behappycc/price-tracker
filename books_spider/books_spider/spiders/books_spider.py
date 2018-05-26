from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from bs4 import BeautifulSoup

from books_spider.items import BookItem

class BooksSpider(CrawlSpider):
    name = 'books_spider'
    start_urls = ['http://search.books.com.tw/search/query/cat/all/key/python/sort/1/page/2/v/0/']
    rules = [       
        Rule(LinkExtractor(allow=('http://search.books.com.tw/search/query/cat/all/key/python/sort/1/page/[1-5]/v/0/',)), callback='parse_items'),       
    ]

    def parse_items(self, response):
        soup = BeautifulSoup(response.text, 'html.parser')
        books = soup.find_all('li', {'class': 'item'})

        for book in books:
            book_item = BookItem()
            title = book.a['title']
            author = []
            for e in book.find_all('a', {'rel': 'go_author'}):
                author.append(e.text)
            price = book.find('span', {'class': 'price'})('strong')[-1].b.text
            print(title, author, price)

            book_item['title'] = title
            book_item['author'] = author
            book_item['price'] = price
            print(book_item)
            yield book_item