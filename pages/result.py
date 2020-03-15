from selenium.webdriver.common.by import By


class ResultPage:
    LINK_DIVS = (By.CSS_SELECTOR, '#links > div')
    SEARCH_INPUT = (By.ID, 'search_form_input')

    @classmethod
    def __init__(cls, browser):
        cls.browser = browser

    def PHRASE_RESULTS(self, phrase):
        xpath = "//div[@id='links']//*[contains(text(), '{0}')]".format(phrase)
        print("xpath: " + xpath)
        return By.XPATH, xpath

    def link_div_count(self):
        link_divs = self.browser.find_elements(*self.LINK_DIVS)
        return len(link_divs)

    def phrase_result_count(self, phrase):
        phrase_results = self.browser.find_elements(*self.PHRASE_RESULTS(phrase))
        return len(phrase_results)

    def search_input_value(self):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        return search_input.get_attribute('value')
