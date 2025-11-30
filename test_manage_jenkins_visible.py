import time
from http import HTTPStatus


def test_create_new_item(page):
    page.goto('/')

    expected_url = 'http://localhost:9091/manage/'

    manage_btn = 'a[id="root-action-ManageJenkinsAction"]'

    with page.expect_response(lambda response: response.status) as response_info:
        page.locator(manage_btn).click()

    response = response_info.value
    status_code = response.status

    actual_url = page.url

    assert actual_url == expected_url and status_code == HTTPStatus.FOUND

def test(page):
    page.goto('/')
    time.sleep(10)