from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time

def dismiss_password_popup(driver):
    """
    Dismiss Google Password Manager popup if it appears
    """
    try:
        time.sleep(1)

        ok_button = driver.find_element(By.XPATH, "//button[normalize-space()='OK']")
        ok_button.click()
        print("password popup ditemukan dan ditutup")
    except NoSuchElementException:
        print("tidak ada popup password, lanjut tes")