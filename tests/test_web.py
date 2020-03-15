from pages.search import SearchPage
from pages.result import ResultPage


def test_basic_search(browser):
    # Set up test case data
    PHRASE = 'panda'
    # Search for the phrase
    search_page = SearchPage(browser)
    search_page.load()
    search_page.search(PHRASE)
    # Verify that results appear
    result_page = ResultPage(browser)
    assert result_page.link_div_count() > 0
    assert result_page.phrase_result_count(PHRASE) > 0
    assert result_page.search_input_value() == PHRASE
