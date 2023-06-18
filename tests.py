import pytest
import selenium
from main import get_song, check_result
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from main import app


correct_answer = 'Stairway to Heaven'
lives = 3
score = 0

@pytest.fixture()
def client():
    return app.test_client()


def test_request_example(client):
    response = client.get("/")
    assert response.status_code == 200


def test_not_empty():
    assert get_song() != ""



# @pytest.fixture()
# def browser():
#     driver = Chrome()
#     driver.implicitly_wait(10)
#     yield driver
#     driver.quit()
#
#
# def test_basic(browser):
#     URL = 'http://127.0.0.1:5000'
#     browser.get(URL)
#     body_text = driver.find_element_by_css_selector('body').text
#     assert body_text == 'Hi'
#     driver.quit()
#
#




