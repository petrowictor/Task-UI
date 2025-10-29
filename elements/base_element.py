import allure
import time
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException

from tools.logger import get_logger

logger = get_logger("BASE_ELEMENT")

class BaseElement:
    def __init__(self, driver: WebDriver, name: str, attribute: str, locator: str):
        self.driver = driver
        self.name = name
        self.attribute = attribute
        self.locator = locator
        self._wait = WebDriverWait(driver, 10)
        self.seconds_wait = 0

    @property
    def type_of(self)-> str:
        return "Base element"

    def wait(self, seconds=3):
        start_time = time.time()
        self._wait.until(lambda driver: (time.time() - start_time) >= seconds)
    
    def get_locator(self, **kwargs):
        locator = self.locator.format(**kwargs)
        step = f'Getting locator with "{self.attribute} = {locator}"'

        with allure.step(step):
            logger.info(step)
            element = self.driver.find_element(By.CSS_SELECTOR, f"[{self.attribute}='{locator}']")
            wait_element = self._wait.until(EC.visibility_of(element))
            self.wait(self.seconds_wait)
            return wait_element

    def click(self, **kwargs):
        step = f'Clicking on element {self.type_of} "{self.name}"'

        with allure.step(step):
            locator = self.get_locator(**kwargs)
            logger.info(step)
            self._wait.until(EC.element_to_be_clickable(locator))
            try:
                locator.click()
            except ElementClickInterceptedException:
                logger.info("Click submit failed")