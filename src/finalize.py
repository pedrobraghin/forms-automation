from selenium.webdriver.common.by import By

button_send_xpath='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]'
checkbox_no_suggestion_xpath='//*[@id="i8"]'

def send_form(browser):
  button_next_element = browser.find_element(By.XPATH, button_send_xpath)
  button_next_element.click()

def fill_finalize(browser):
  checkbox_no_suggestion_element = browser.find_element(By.XPATH, checkbox_no_suggestion_xpath)
  checkbox_no_suggestion_element.click()
  send_form(browser)