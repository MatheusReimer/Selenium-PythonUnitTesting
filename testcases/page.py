from locator import SearchResultPageLocators,MainPageLocators
from element import BasePageElement


from locator import *


class SearchTextElement(BasePageElement):
    locator = "q"
    

class BasePage(object):
    def __init__(self,driver):
        self.driver = driver

###Argument  === inhereting from basepage
class MainPage(BasePage):

    search_text_element = SearchTextElement()

    def is_title_matches(self):
        return "Python" in self.driver.title

    def click_go_button(self):
        element = self.driver.find_element(*MainPageLocators.GO_BUTTON)
        element.click()
    
class SearchResultPage(BasePage):

    def is_result_found(self):
        return "No results found " not in self.driver.page_source