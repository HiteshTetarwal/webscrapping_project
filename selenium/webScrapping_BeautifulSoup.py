from selenium import webdriver
import time
from bs4 import BeautifulSoup
import csv

options = webdriver.ChromeOptions()

options.add_argument('--disable-features=Permissions-Policy')
driver = webdriver.Chrome(options=options)

base_url = 'https://www.overdrive.com/subjects/biography-autobiography?page='
page_count = 5


books_data = []
for page in range(1, page_count + 1):
    url = base_url + str(page)
    driver.get(url)
    time.sleep(3) 

    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')

    titles = soup.select('.title-result-row__title a')
    authors = soup.select('.title-result-row__creator')
    for title, author in zip(titles, authors):
        book_title = title.text.strip()
        book_author = author.text.strip()
        books_data.append([book_title, book_author])

driver.quit()
