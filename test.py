import requests
from bs4 import BeautifulSoup

# BOOKS_URL = 'http://search.books.com.tw/search/query/key/<keyword>/cat/BKA'
BOOKS_URL = 'http://search.books.com.tw/search/query/cat/all/key/<keyword>/sort/1/page/2/v/0/'
# 將 url 中的 <keyword> 置換成我們要查詢的書名
url = BOOKS_URL.replace('<keyword>', 'python')

# 使用 requests 跟博客來的伺服器要資料
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')
books = soup.find_all('li', {'class': 'item'})

for book in books:
    # 取得書名
    title = book.a['title']
    author = []
    for e in book.find_all('a', {'rel': 'go_author'}):
        author.append(e.text)
    price = book.find('span', {'class': 'price'})('strong')[-1].b.text
    # 對書名做處理，濾掉多餘的字元
    print(title, author, price)