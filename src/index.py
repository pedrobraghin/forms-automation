import time

from selenium import webdriver

from files import load_users
from personalInfo import fill_person_info
from questions import fill_questions
from finalize import fill_finalize

forms_urls=''


def fill_form(user, browser):
  browser.get(forms_urls)

  fill_person_info(browser, user)
  fill_questions(browser)
  fill_finalize(browser)

  browser.refresh()
  time.sleep(1)


if __name__ == '__main__':
  option = webdriver.ChromeOptions()

  option.add_argument("-incognito")
  option.add_argument("--headless")

  browser = webdriver.Chrome(options=option)
  users = load_users()
  
  for i in range(0, len(users) - 1):
    fill_form(users[i], browser)