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

class TestEditarpacientes():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_editarpacientes(self):
    self.driver.get("http://localhost/citas_medicas/login.php")
    self.driver.set_window_size(1810, 727)
    self.driver.find_element(By.NAME, "usuario").click()
    self.driver.find_element(By.NAME, "usuario").send_keys("dgam27")
    self.driver.find_element(By.NAME, "clave").click()
    self.driver.find_element(By.NAME, "clave").send_keys("11111")
    self.driver.find_element(By.NAME, "login").click()
    self.driver.find_element(By.LINK_TEXT, "Pacientes").click()
    self.driver.find_element(By.LINK_TEXT, "Mostrar").click()
    self.driver.find_element(By.CSS_SELECTOR, ".even:nth-child(4) .fa-edit").click()
    self.driver.find_element(By.CSS_SELECTOR, ".active > .form-control").click()
    self.driver.find_element(By.CSS_SELECTOR, ".active > .form-control").send_keys("12345678")
    self.driver.find_element(By.CSS_SELECTOR, ".active > .form-control").click()
    self.driver.find_element(By.CSS_SELECTOR, ".active > .form-control").click()
    self.driver.find_element(By.CSS_SELECTOR, ".active > .form-control").click()
    self.driver.find_element(By.CSS_SELECTOR, ".active > .form-control").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".active > .form-control")
    actions = ActionChains(self.driver)
    actions.double_click(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".active > .form-control").send_keys("Julio")
    self.driver.find_element(By.CSS_SELECTOR, ".active > .form-control").click()
    self.driver.find_element(By.CSS_SELECTOR, ".active > .form-control").click()
    self.driver.find_element(By.CSS_SELECTOR, ".active > .form-control").send_keys("809754777")
    self.driver.find_element(By.CSS_SELECTOR, "#editRowModal5 .btn-primary").click()
    self.driver.find_element(By.CSS_SELECTOR, ".dropdown-toggle .avatar-img").click()
    self.driver.find_element(By.LINK_TEXT, "Logout").click()
  
