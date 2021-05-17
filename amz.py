import csv 
import bs4 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class GetArticles():
    def __init__ (self, title, price):
        self.title = title
        self.price = price

class Bot:
    def article(self, name):
        count = 1 
        page = 1
        pageIncrement = 10
        maxRetrieves = 100

        url ='https://wwww.amazon.ca/s?k=' name+ "&page=" str(page)

        options = Options()
        options.headless = False
        options.add_experimental_option('detach', True)

        browser = webdriver.Chrome(ChromeDriverManager().install(), options = options)

        browser.maximize_window()
        browser.get(url)
        browser.set_page_load_timeout(10)

        while True: 
            try:
                if pageIncrement *page > maxRetrieves:
                    break

                if count > pageIncrement:
                    count = 1
                    page += 1
                    
            catch: 


//*[@id="search"]/div[1]/div/div[1]/div/span[3]/div[2]/div[3]/div/span/div/div/div[2]/div[2]/div/div[1]/h2/a/span