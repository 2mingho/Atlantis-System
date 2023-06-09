# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestCambiarestadocitas():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_cambiarestadocitas(self):
    self.driver.get("http://localhost/citas_medicas/login.php")
    self.driver.set_window_size(1642, 727)
    self.driver.find_element(By.NAME, "usuario").click()
    self.driver.find_element(By.NAME, "usuario").send_keys("dgam27")
    self.driver.find_element(By.NAME, "usuario").send_keys(Keys.ENTER)
    self.driver.find_element(By.NAME, "clave").send_keys("11111")
    self.driver.find_element(By.NAME, "clave").send_keys(Keys.ENTER)
    self.driver.find_element(By.LINK_TEXT, "Citas").click()
    self.driver.find_element(By.LINK_TEXT, "Mostrar").click()
    self.driver.find_element(By.CSS_SELECTOR, ".btn-xs:nth-child(1)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".dropdown-toggle .avatar-img").click()
    self.driver.find_element(By.LINK_TEXT, "Logout").click()
  
