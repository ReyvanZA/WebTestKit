from enum import Enum
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

class ElementType(Enum):
    ID = 0
    Name = 1
    CSS = 2
    TEXT = 3
    CLASS = 4
    XPATH = 5

class SiteNavigator:
    def __init__ (self, driver):
        self.driver = driver

    def findElemnt(self,description, type):
        if type == ElementType.ID:
            return WebDriverWait(self.driver,400).until(ec.presence_of_element_located((By.ID,description)))
        if type == ElementType.TEXT:
            return WebDriverWait(self.driver,400).until(ec.presence_of_element_located((By.LINK_TEXT,description)))
        if type == ElementType.CLASS:
            return WebDriverWait(self.driver,400).until(ec.presence_of_element_located((By.CLASS_NAME,description)))
        if type == ElementType.XPATH:
            return WebDriverWait(self.driver,400).until(ec.presence_of_element_located((By.XPATH,description)))
            

            
   