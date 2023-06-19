import pytest
import selenium
import time
from main import get_song, check_result
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from main import app


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')

driver = webdriver.Chrome(options=chrome_options)

@pytest.fixture()
def client():
    return app.test_client()


def test_request_example(client):
    response = client.get("/")
    assert response.status_code == 200


def test_not_empty():
    assert get_song() != ""



@pytest.fixture()
def browser():
    global driver
    driver.implicitly_wait(10)
    yield driver


def test_image_gen(browser):
    global driver
    URL = 'http://127.0.0.1:5000'
    browser.get(URL)
    start_btn = driver.find_element(By.ID, "getGen")
    start_btn.click()
    time.sleep(15)
    img = driver.find_element(By.NAME, "check")
    img_src = img.get_attribute('src')
    assert img_src != ''


def test_ptn_decr(browser):
    global driver
    URL = 'http://127.0.0.1:5000'
    browser.get(URL)
    post_btn = driver.find_element(By.ID, "postAns")
    for i in range(2):
        post_btn.click()
        time.sleep(10)
        print("i=", i)
        a = 2 - i
        print("a=", a)
        pnt = driver.find_element(By.ID, "qwe").text
        assert pnt == f"{a}"
    driver.quit()

