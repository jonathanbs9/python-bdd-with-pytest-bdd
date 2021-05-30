"""
This module contains step definitions for service.feature
It uses the request page:
http://docs.python-requests.org/
"""
from _pytest.mark import param
import requests

from pytest_bdd import scenarios, given, then, parsers

# Shared variables
DUCKDUCKGO_API  = 'http://api.duckduckgo.com/'

# Scenarios
scenarios('../features/service.feature', example_converters=dict(phrase=str))

# Given steps

@given('the DuckDuckGo API is queried with "<phrase>"', target_fixture='duckduckgo_response')
def duckduckgo_response(phrase):
    params = {'q': phrase, 'format': 'json'}
    response = requests.get(DUCKDUCKGO_API, params=params)
    return response

# Then steps
@then('the response contains results for "<phrase>"')
def duckduckgo_response_contents(duckduckgo_response, phrase):
    assert phrase.lower() == duckduckgo_response.json()['Heading'].lower()

@then(parsers.parse('the response status code is "{code:d}"'))
def duckduckgo_response_code(duckduckgo_response, code):
    assert duckduckgo_response.status_code == code
