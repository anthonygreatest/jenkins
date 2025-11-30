import pytest
import requests
from playwright.sync_api import Playwright, ViewportSize

api_token = '11066bcbdf5ab1171ef303a6e38578c5fb'
user_name = 'tony'
url = 'http://localhost:9091'

def get_all_jobs():
    response = requests.get(
        url=f'{url}/api/json',
        auth=(user_name, api_token)
    )
    a = response.json()['jobs']
    print(a)
    return response.json()['jobs']

def delete_jobs():

    jobs_list = get_all_jobs()

    for job in jobs_list:
        name = job['name']
        requests.post(
            url=f'{url}/job/{name}/doDelete',
            auth=(user_name, api_token)
        )

@pytest.fixture(scope='session')
def get_cookies(playwright: Playwright):

    username_loc = 'input[id="j_username"]'
    pass_loc = 'input[id="j_password"]'
    username = 'tony'
    password = 'tony1806'

    browser = playwright.chromium.launch()
    context = browser.new_context(base_url='http://localhost:9091/login?from=%2F')
    page = context.new_page()

    page.goto('/')

    page.locator(username_loc).fill(username)
    page.locator(pass_loc).fill(password)
    page.get_by_role(role='button', name='Sign in').click()
    cookies = context.cookies()
    page.close()
    context.close()
    browser.close()

    return cookies

@pytest.fixture
def page(playwright: Playwright, get_cookies):
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context(viewport=ViewportSize(width=1440, height=980), base_url='http://localhost:9091')
    context.add_cookies(get_cookies)
    page = context.new_page()
    yield page
    page.close()
    context.close()
    browser.close()

@pytest.fixture(scope='session', autouse=True) #чтобы сама вызывалась всегда
def delete_jobs_after_tests():
    yield
    delete_jobs()