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
    def __init__(self, driver: WebDriver, name: str, locator: str):
        self.driver = driver
        self.name = name
        self.locator = locator
        self._wait = WebDriverWait(driver, 10)
        self.seconds_wait = 0

    @property
    def type_of(self)-> str:
        return "Base element"

    def wait(self, seconds=3):
        start_time = time.time()
        self._wait.until(lambda driver: (time.time() - start_time) >= seconds)

    def wait_for_all_elements(self, **kwargs):
        locator = self.locator.format(**kwargs)
        WebDriverWait(self.driver, 15).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, locator))
            )

    def get_locator(self, nth: int = 0, **kwargs):
        locator = self.locator.format(**kwargs)
        step = f'Getting locator with {locator} at index "{nth}"'

        with allure.step(step):
            self.wait_for_all_elements(locator=locator)
            element = self.driver.find_elements(By.CSS_SELECTOR, locator)[nth]
            self.wait(self.seconds_wait)
            return element

    def click(self, nth: int = 0, **kwargs):
        step = f'Clicking {self.type_of} "{self.name}"'

        with allure.step(step):
            locator = self.get_locator(nth,**kwargs)
            logger.info(step)
            self._wait.until(EC.element_to_be_clickable(locator))
            try:
                locator.click()
            except ElementClickInterceptedException:
                logger.info("Click submit failed")
            self.wait(self.seconds_wait)

    def get_text(self, nth: int = 0, **kwargs):
        step = f'Gettig text {self.name}'
        with allure.step(step):
            locator = self.get_locator(nth,**kwargs)
            logger.info(step)
            return locator.text