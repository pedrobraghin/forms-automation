import random
import time
from selenium.webdriver.common.by import By

button_next_xpath='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]'

def answer_question(browser, id_one, id_two, id_three, id_four):
  checkbox_one_xpath = f'//*[@id="i{id_one}"]'
  checkbox_two_xpath = f'//*[@id="i{id_two}"]'
  checkbox_three_xpath = f'//*[@id="i{id_three}"]'
  checkbox_four_xpath = f'//*[@id="i{id_four}"]'
  
  index = random.randint(0, 10)
  checkbox_element = None

  if index >= 0 and index <= 3:
    checkbox_element = browser.find_element(By.XPATH, checkbox_one_xpath)
  elif index >=4 and index <= 7:
    checkbox_element = browser.find_element(By.XPATH, checkbox_two_xpath)
  elif index >=8 and index <= 9:
    checkbox_element = browser.find_element(By.XPATH, checkbox_three_xpath)
  else:
    checkbox_element = browser.find_element(By.XPATH, checkbox_four_xpath)
  
  checkbox_element.click()

def go_next_step(browser):
  button_next_element = browser.find_element(By.XPATH, button_next_xpath)
  button_next_element.click()

def fill_questions(browser):
  counter = 5

  for _ in range(0, 9):
    id_one = counter
    id_two = id_one + 3
    id_three = id_two + 3
    id_four = id_three + 3

    time.sleep(0.2) 

    answer_question(browser=browser, id_one=id_one, id_two=id_two, id_three=id_three, id_four=id_four)

    counter = id_four + 7

  go_next_step(browser)