from selenium.webdriver.common.by import By

class HomePage:
    INVENTORY_ITEM = (By.CLASS_NAME, "inventory_item")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "button.btn_primary")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver
    def add_first_item_to_cart(self):
        items = self.driver.find_elements(*self.ADD_TO_CART_BUTTON)
        if items:
            items[0].click()
    def go_to_cart(self):
        self.driver.find_element(*self.CART_LINK).click()