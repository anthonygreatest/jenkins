import random
import time

from playwright.sync_api import expect

from conftest import delete_jobs


def test_create_new_item(page):
    page.goto('/')

    new_item_name = f'tony-{random.randint(0, 1000)}'
    new_item = 'a[href="/view/all/newJob"]'
    item_name = 'input[id="name"]'
    item_type_text = 'Pipeline'
    ok_btn = 'button[id="ok-button"]'
    logo = 'a.app-jenkins-logo'
    job_exists = lambda name: f'td > a[href="job/{name}/"]'


    page.locator(new_item).click()
    page.locator(item_name).fill(new_item_name)
    page.get_by_text(item_type_text, exact=True).click()
    page.locator(ok_btn).click()
    page.locator(logo).click()

    expect(page.locator(job_exists(new_item_name))).to_have_text(new_item_name)
    print(new_item_name)

