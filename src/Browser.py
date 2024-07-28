from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class Browser:
    def __init__(self):
        # Initialize the driver attribute
        self.driver = None

    def firefox(self):
        # Set up the Firefox driver using GeckoDriverManager
        self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        # Open the target website
        self.driver.get('https://www.cambodiapostalcode.com')

    def brave(self):
        # Path to the Brave browser's chromedriver
        chromedriver = "D:/Ministry of Rural Development Intern/codes/MinistryOfRural-Development/Selenuim Scraping/ScrappingPeoject/SeleniumScrapping-RuralDevelopment/drivers/chromedriver.exe"
        
        # Set up Chrome options for Brave browser
        option = webdriver.ChromeOptions()
        option.binary_location = 'C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe'
        
        # Initialize the service with the specified chromedriver path
        service = ChromeService(chromedriver)
        
        # Initialize the WebDriver with the service and options
        self.driver = webdriver.Chrome(service=service, options=option)
        
        # Open the target website
        self.driver.get('https://www.cambodiapostalcode.com')