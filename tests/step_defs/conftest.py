import pytest

from pytest_bdd import given
from selenium import webdriver

DUCKDUCKGO_HOME = 'https://duckduckgo.com/'


def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
    print(f'Step failed: {step}')


@pytest.fixture
def browser():
    b = webdriver.Firefox()
    b.implicitly_wait(10)
    yield b
    b.quit()


@given('the DuckDuckGo home page is displayed', target_fixture="ddg_home")
def ddg_home(browser):
    browser.get(DUCKDUCKGO_HOME)

