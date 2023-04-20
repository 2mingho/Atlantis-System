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

class TestAgregarpacientes():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_agregarpacientes(self):
    self.driver.get("http://localhost/citas_medicas/login.php")
    self.driver.set_window_size(1621, 863)
    self.driver.find_element(By.NAME, "usuario").click()
    self.driver.find_element(By.NAME, "usuario").send_keys("dgam27")
    self.driver.find_element(By.NAME, "usuario").send_keys(Keys.ENTER)
    self.driver.find_element(By.NAME, "clave").send_keys("11111")
    self.driver.find_element(By.NAME, "clave").send_keys(Keys.ENTER)
    self.driver.find_element(By.CSS_SELECTOR, ".nav-item:nth-child(3) p").click()
    self.driver.find_element(By.LINK_TEXT, "Mostrar").click()
    self.driver.find_element(By.LINK_TEXT, "Nuevo").click()
    self.driver.find_element(By.NAME, "dnipa").click()
    self.driver.find_element(By.NAME, "dnipa").send_keys("23456789")
    self.driver.find_element(By.CSS_SELECTOR, ".pr-0 > .form-group").click()
    self.driver.find_element(By.NAME, "nombrep").click()
    self.driver.find_element(By.NAME, "nombrep").send_keys("Julian")
    self.driver.find_element(By.NAME, "apellidop").click()
    self.driver.find_element(By.NAME, "apellidop").send_keys("Alvarado")
    self.driver.find_element(By.NAME, "tele").click()
    self.driver.find_element(By.NAME, "tele").send_keys("809777777")
    self.driver.find_element(By.NAME, "seguro").click()
    self.driver.find_element(By.NAME, "sexo").click()
    self.driver.find_element(By.CSS_SELECTOR, ".row:nth-child(1) > .col-md-6:nth-child(7) > .form-group").click()
    self.driver.find_element(By.NAME, "usuario").click()
    self.driver.find_element(By.NAME, "usuario").send_keys("jalvarado")
    self.driver.find_element(By.NAME, "clave").click()
    self.driver.find_element(By.NAME, "clave").send_keys("11111")
    self.driver.find_element(By.NAME, "agregar").click()
    self.driver.find_element(By.CSS_SELECTOR, ".dropdown-toggle .avatar-img").click()
    self.driver.find_element(By.LINK_TEXT, "Logout").click()
  
