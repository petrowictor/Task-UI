from elements.base_element import BaseElement
from tools.logger import get_logger

logger = get_logger("BUTTON")
class Button(BaseElement):
    @property
    def type_of(self) -> str:
        return "Button"