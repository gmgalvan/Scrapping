from selenium import webdriver
from selenium.webdriver.firefox.options import Options

class Agent:
    path_s = './geckodriver-v0.23.0-linux64/geckodriver' # Needs to be downloaded
    def __init__(self,visible=True,focus_page="https://www.google.com.mx"): 
        if visible:
            self.driver = webdriver.Firefox(executable_path = self.path_s)
        else:
            options = Options()
            options.add_argument('--headless')
            self.driver = webdriver.Firefox(executable_path = self.path_s,options=options)
        self.page = self.driver.get(focus_page)
    def source(self):
        return self.driver.page_source
    def screenshot(self,name_s):
        self.driver.implicitly_wait(10)
        self.driver.save_screenshot(name_s)
    def read_by_css_selector_txt(self,selector):
        return self.driver.find_element_by_css_selector(selector).text
    def wait(self,time_wait):
        self.driver.implicitly_wait(time_wait)
    def focus(self,page):
        self.page = self.driver.get(page)
    def end(self):
        self.driver.quit()