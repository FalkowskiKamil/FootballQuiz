# Generated by Selenium IDE
import random
import string
import time
from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestFunctional(TestCase):
  def setUp(self):
    self.driver = webdriver.Firefox()
    self.vars = {}
    self.data = self.random_register_data()
  
  def tearDown(self):
    self.driver.quit()
  
  def random_register_data(self):
    return (''.join(random.choices(string.ascii_uppercase + string.digits, k=8)))

  def test_functional(self):
    self.driver.get("http://localhost:8000/")
    self.driver.set_window_size(686, 819)
    self.driver.find_element(By.LINK_TEXT, "Login").click()
    self.driver.find_element(By.ID, "username").send_keys(self.data)
    self.driver.find_element(By.ID, "psw").send_keys(self.data)
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    self.driver.find_element(By.LINK_TEXT, "Register").click()
    self.driver.find_element(By.NAME, "username").send_keys(self.data)
    self.driver.find_element(By.NAME, "firstname").send_keys(self.data)
    self.driver.find_element(By.NAME, "lastname").send_keys(self.data)
    self.driver.find_element(By.NAME, "psw").click()
    self.driver.find_element(By.NAME, "psw").click()
    element = self.driver.find_element(By.NAME, "psw")
    actions = ActionChains(self.driver)
    actions.double_click(element).perform()
    self.driver.find_element(By.NAME, "psw").send_keys(self.data)
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    self.driver.find_element(By.LINK_TEXT, "Logout").click()
    self.driver.close()
  
