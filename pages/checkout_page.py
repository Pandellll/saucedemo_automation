from selenium.webdriver.common.by import By

class CheckoutPage:
    CHECKOUT_BUTTON = (By.ID, "checkout")
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "complete-header")

    def __init__(self, driver):
        self.driver = driver
    
    def checkout(self, first_name, last_name, postal_code):
        self.driver.find_element(*self.CHECKOUT_BUTTON).click()
        self.driver.find_element(*self.FIRST_NAME).send_keys(first_name)
        self.driver.find_element(*self.LAST_NAME).send_keys(last_name)
        self.driver.find_element(*self.POSTAL_CODE).send_keys(postal_code)
        self.driver.find_element(*self.CONTINUE_BUTTON).click()
        self.driver.find_element(*self.FINISH_BUTTON).click()
    
    def get_success_message(self):
        return self.driver.find_element(*self.SUCCESS_MESSAGE).text