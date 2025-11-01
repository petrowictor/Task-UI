import allure
from elements.base_element import BaseElement
from tools.logger import get_logger

logger = get_logger("Input")

class Input(BaseElement):
    @property
    def type_of(self) -> str:
        return "input"

    def fill(self, value, **kwargs):
        step = f'Fill {self.type_of} "{self.name}" to value "{value}"'

        with allure.step(step):
            locator = self.get_locator(**kwargs)
            logger.info(step)
            locator.send_keys(value)

    def get(self, **kwargs):
        step = f'Getting value {self.type_of} "{self.name}"'

        with allure.step(step):
            locator = self.get_locator(**kwargs)
            logger.info(step)
            value =locator.get_attribute("value")
            logger.info(f"Received value={value}")