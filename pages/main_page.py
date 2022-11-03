import time

from selenium.webdriver.common.by import By
from pages.base_page import Page


class MainPage(Page):

    SEARCH_BOX = (By.XPATH, "//input[@id='twotabsearchtextbox']")
    FIND_BUTTON = (By.XPATH, "//input[@id='nav-search-submit-button']")
    VERIFY_PRODUCT = (By.XPATH, "//img[@alt='Books%20at%20Amazon']")


    def open_amazon_website(self):
        self.open_page(url="https://www.amazon.com/")

    def search_items(self, searchItem):
        box = self.driver.find_element(*self.SEARCH_BOX)
        box.send_keys(searchItem)

    def verify_items(self):
        self.driver.find_element(*self.VERIFY_PRODUCT)

    def clear_search(self):
        self.driver.find_element(*self.SEARCH_BOX).clear()
        # box.send_keys(searchItem)

    # def search_items(self, searchItem):
    #     box = self.driver.find_element(*self.SEARCH_BOX)
    #     box.send_keys(searchItem)

    def search_button(self):
        button = self.driver.find_element(*self.FIND_BUTTON)
        button.click()










