from parse import parse
import pytest

from pytest_bdd import scenarios, given, then , when, parsers
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from six import b

# Constants

DUCKDUCKGO_HOME = 'http://duckduckgo.com/'


# Scenarios 

scenarios('../features/web.feature')

# Fixtures

@pytest.fixture
def browser():
    # We are going to use Chrome
   b = webdriver.Chrome()
   b.implicitly_wait(15) 
   yield b
   b.quit()

# Given steps

@given('the DuckDuckGo home page is displayed')
def duckduckgo_home(browser):
    browser.get(DUCKDUCKGO_HOME)

# When Steps

@when(parsers.parse('the user searches for "{text}"'))
@when(parsers.parse('the user searches for the phrase:\n"""{text}"""'))
def search_phrase(browser, text):
    search_input = browser.find_element_by_name('q')
    search_input.send_keys(text + Keys.RETURN)

# Then steps
@then(parsers.parse('one of the results contains "{phrase}"'))
def result_have_one(browser, phrase):
    xpath = "//div[@id='links']//*[contains(text(), '%s')]" % phrase
    results = browser.find_elements_by_xpath(xpath)
    assert len(results) > 0

@then(parsers.parse('results are shown for "{phrase}"'))
def search_results(browser, phrase):
    # Check Search result list
    # A more comprehensive test would check results for matching phrases
    # Check the list before the search phrase for correct implicit waiting 
    links_div = browser.find_element_by_id('links')
    assert len(links_div.find_elements_by_xpath('//div')) > 0
    # Check search phrase
    search_input = browser.find_element_by_name('q')
    assert search_input.get_attribute('value') == phrase