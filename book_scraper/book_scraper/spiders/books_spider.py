import scrapy
import csv
import time

class BooksSpider(scrapy.Spider):
    name = 'books'
    start_urls = ['https://www.overdrive.com/subjects/biography-autobiography?page=' + str(i) for i in range(1, 101)]

    def parse(self, response):
        start_time = time.time()

        books = response.css('.title-result-row')
        for book in books:
            title = book.css('.title-result-row__title a::text').get()
            author = book.css('.title-result-row__creator::text').get()

            with open('books.csv', 'a', newline='', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([title, author])

        end_time = time.time()
        elapsed_time = end_time - start_time
        self.log(f"Scraping completed for {response.url} in {elapsed_time} seconds.")

        next_page = response.css('.pagination__link--next::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)
