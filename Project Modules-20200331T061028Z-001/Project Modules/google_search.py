from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import pyautogui

option = Options()
option.add_argument("--disable-notifications")
driver = webdriver.Chrome(chrome_options = option)
driver.maximize_window()
driver.get("https://www.google.com")
search = pyautogui.prompt('Enter what you want to search')
driver.find_element_by_name('q').send_keys(search + '\n')
time.sleep(4)
driver.close()