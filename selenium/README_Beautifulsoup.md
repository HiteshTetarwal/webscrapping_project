

# Web Scraping with Selenium and BeautifulSoup

This project demonstrates web scraping using Selenium and BeautifulSoup to extract book titles and authors from a website. The extracted data is then saved to a CSV file. The project utilizes Python programming language and requires the Chrome WebDriver for Selenium.

## Installation

1. Clone the project repository:

```shell
git clone https://github.com/HiteshTetarwal/webscrapping_project
```

2. Install the required dependencies:

```shell
pip install selenium beautifulsoup4
```

3. Download the Chrome WebDriver suitable for your Chrome browser version and operating system. Place the WebDriver executable in the project directory.

4. (Optional) If you prefer to run Chrome in headless mode (without opening the browser window), uncomment the line `# options.add_argument('--headless')` in the code.

## Usage

1. Update the `base_url` and `page_count` variables in the code to match the desired URL and number of pages to scrape.

2. Run the script:

```shell
python web_scraping.py
```

3. Monitor the console output for progress updates. Once the scraping is complete, a CSV file named `books_data.csv` will be generated in the project directory. This file contains the scraped book titles and authors.

## Approach

1. The Chrome WebDriver is configured using the `webdriver.Chrome()` method. Additional options can be set, such as running Chrome in headless mode or disabling certain features.

2. The base URL and page count are defined to determine the range of pages to scrape.

3. A loop is used to iterate through each page, and the WebDriver navigates to each page using the constructed URL.

4. A waiting period is added to allow the page to load before extracting the data.

5. The page source is retrieved using `driver.page_source`, and BeautifulSoup is used to parse the HTML content.

6. CSS selectors are used to locate the book titles and authors on the page. The appropriate selectors are `.title-result-row__title a` for the book titles and `.title-result-row__creator` for the authors.

7. The extracted book titles and authors are stored in a list.

8. Once all pages are processed, the WebDriver is closed.

9. The book titles and authors are saved to a CSV file using the `csv` library.

10. The elapsed time for the scraping process is calculated and printed to the console.
