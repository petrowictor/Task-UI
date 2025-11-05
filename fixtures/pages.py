import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from config import Settings
from pages.manager_page import ManagerPage


@pytest.fixture
def chromium_page(settings: Settings):
    chrome_options = Options()
    if settings.headless:
        chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--ignore-ssl-errors')
    chrome_options.page_load_strategy = 'normal'
    
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(str(settings.app_url))
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "[ng-class='btnClass2']"))
    )
    yield driver
    driver.quit()

@pytest.fixture
def manager_page(chromium_page):
    return ManagerPage(driver=chromium_page)