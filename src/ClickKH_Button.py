from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
class KhmerInterface:
    def __init__(self, driver):
        # Initialize with an existing WebDriver instance
        self.driver = driver

    def click_khmer(self):
        # Wait until the dialog backdrop is invisible
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located((By.CLASS_NAME, 'q-dialog__backdrop'))
        )
        
        # Wait until the Khmer language button is clickable
        khmer_language_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/header/div[1]/div/a[2]/div[2]/div'))
        )
        
        # Click the Khmer language button
        khmer_language_button.click()