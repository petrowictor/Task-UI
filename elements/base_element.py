import allure
import time
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException, NoAlertPresentException

from tools.helpers import get_logger

logger = get_logger("BASE_ELEMENT")

class BaseElement:
    def __init__(self, driver: WebDriver, name: str, locator: str):
        self.driver = driver
        self.name = name
        self.locator = locator
        self._wait = WebDriverWait(driver, 10)
        self.seconds_wait = 0

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
        step = f'Clicking "{self.name}"'

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
        step = f'Getting text {self.name}'
        with allure.step(step):
            locator = self.get_locator(nth,**kwargs)
            logger.info(step)
            return locator.text

    def fill(self, value, **kwargs):
        step = f'Fill "{self.name}" to value "{value}"'

        with allure.step(step):
            locator = self.get_locator(**kwargs)
            logger.info(step)
            locator.send_keys(value)

    def get(self, **kwargs):
        step = f'Getting value "{self.name}"'

        with allure.step(step):
            locator = self.get_locator(**kwargs)
            logger.info(step)
            value =locator.get_attribute("value")
            logger.info(f"Received value={value}")

    def accept(self):
        step = f"Check Alert is present"
        with allure.step(step):
            logger.info(step)
            try:
                alert = self.driver.switch_to.alert
                allure.attach(
                    f"Alert is present",
                    name="Alert detected",
                    attachment_type=allure.attachment_type.TEXT
                )
                alert.accept()
            except NoAlertPresentException:
                allure.attach(
                    f"Alert is not present",
                    name="Alert detected",
                    attachment_type=allure.attachment_type.TEXT
                )