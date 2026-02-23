import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

class TestBookScraping(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        self.browser = webdriver.Chrome(options=chrome_options)
        self.browser.get("https://books.toscrape.com/catalogue/category/books_1/index.html")
        self.browser.implicitly_wait(5)

    def tearDown(self):
        self.browser.quit()

    def test_books_present(self):
        products = self.browser.find_elements(By.CSS_SELECTOR, 'article.product_pod')
        self.assertGreater(len(products), 0, "Aucun livre trouvé sur la page.")

    def test_book_fields(self):
        products = self.browser.find_elements(By.CSS_SELECTOR, 'article.product_pod')
        for product in products:
            title = product.find_element(By.CSS_SELECTOR, 'h3 a').get_attribute('title')
            url = product.find_element(By.CSS_SELECTOR, 'h3 a').get_attribute('href')
            price = product.find_element(By.CSS_SELECTOR, 'p.price_color').text
            description = product.find_element(By.CSS_SELECTOR, 'p.instock.availability').text.strip()
            self.assertTrue(title)
            self.assertTrue(url)
            self.assertTrue(price)
            self.assertTrue(description)

if __name__ == '__main__':
    unittest.main()
