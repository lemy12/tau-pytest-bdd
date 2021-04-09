import requests
from pytest_bdd import scenarios, given, then, parsers

DUCKDUCKGO_API = 'https://api.duckduckgo.com/'

scenarios('../features/service.feature', example_converters=dict(phrase=str))


@given('the DuckDuckGo API is queried with "<phrase>"', target_fixture='ddg_response')
def ddg_response(phrase):
    params = {'q': phrase, 'format': 'json'}
    response = requests.get(DUCKDUCKGO_API, params=params)
    return response


@then('the response contains results for "<phrase>"')
def ddg_response_contents(ddg_response, phrase):
    assert phrase.lower() == ddg_response.json()['Heading'].lower()


@then(parsers.parse('the response status code is "{code:d}"'))
def ddg_response_code(ddg_response, code):
    assert ddg_response.status_code == code