import random
import time

from playwright.sync_api import expect


def test_create_new_item(page):
    page.goto('/')

    username_loc = 'input[id="j_username"]'
    pass_loc = 'input[id="j_password"]'
    username = 'tony'
    password = 'tony1806'
    new_item_name = f'tony-{random.randint(0, 1000)}'
    new_item = 'a[href="/view/all/newJob"]'
    item_name = 'input[id="name"]'
    item_type_text = 'Pipeline'
    ok_btn = 'button[id="ok-button"]'
    logo = 'a.app-jenkins-logo'
    job_exists = lambda name: f'td > a[href="job/{name}/"]'

    page.locator(username_loc).fill(username)
    page.locator(pass_loc).fill(password)
    page.get_by_role(role='button', name='Sign in').click()

    page.locator(new_item).click()
    page.locator(item_name).fill(new_item_name)
    page.get_by_text(item_type_text, exact=True).click()
    page.locator(ok_btn).click()
    page.locator(logo).click()

    text = page.locator(job_exists(new_item_name)).text_content()

    print(text)