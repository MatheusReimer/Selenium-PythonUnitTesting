import unittest
from selenium import webdriver
import page

class PythonOrgSearch(unittest.TestCase):
    ###BEFORE EVERY TEST
    def setUp(self):
        self.driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
        self.driver.get("http://www.python.org")
    ###AFTER EVERY TEST
    def tearDown(self):
        self.driver.close()

   


    def test_search_python(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_matches()
        mainPage.search_text_element ="pycon"
        mainPage.click_go_button
        search_result_page = page.SearchResultPage(self.driver)
        assert search_result_page.is_result_found()


if __name__ == "__main__":
    unittest.main()