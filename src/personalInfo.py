import random

from selenium.webdriver.common.by import By

male_xpath='//*[@id="i9"]'
female_xpath='//*[@id="i12"]'
prefer_not_say='//*[@id="i15"]'
name_input_xpath='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'
age_input_xpath='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input'
button_next_xpath='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div'

def fill_gender(browser, gender):
  gender_input = None

  if gender == 'masculino':
    gender_input = browser.find_element(By.XPATH, male_xpath)
  elif gender == 'feminino':
    gender_input = browser.find_element(By.XPATH, female_xpath)
  else:
    gender_input = browser.find_element(By.XPATH, prefer_not_say)

  gender_input.click()

def fill_name(browser, name):
  name_input_element = browser.find_element(By.XPATH, name_input_xpath)
  name_input_element.send_keys(name)

def fill_age(browser):
  random_age = random.randint(19, 28)

  age_input_element = browser.find_element(By.XPATH, age_input_xpath)
  age_input_element.send_keys(random_age)

def go_next_step_1(browser):
  button_next_element = browser.find_element(By.XPATH, button_next_xpath)
  button_next_element.click()

def fill_person_info(browser, user):
  name, gender=user
  
  fill_gender(browser, gender)
  fill_name(browser, name)
  fill_age(browser)
  go_next_step_1(browser)