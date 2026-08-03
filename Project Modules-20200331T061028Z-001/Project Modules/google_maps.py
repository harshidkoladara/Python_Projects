from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import pyautogui

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://maps.google.com")
wait = WebDriverWait(driver,20)
wait.until(EC.visibility_of_element_located((By.ID, 'widget-mylocation')))
driver.find_element_by_id('widget-mylocation').click()
place = pyautogui.prompt('Enter the name of place you want to search')
driver.find_element_by_id('searchboxinput').send_keys(place + '\n')
wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'iRxY3GoUYUY__icon')))
choice = pyautogui.prompt('Would you like to switch to Satellite view?')
if choice.lower() == 'yes':
    driver.find_element_by_xpath('//*[@id="minimap"]/div/div[2]/button').click()
choice = pyautogui.prompt('Would you like to switch to Map View?')
if choice.lower() == 'yes':
    driver.find_element_by_xpath('//*[@id="minimap"]/div/div[2]/button').click()
choice = pyautogui.prompt('Would you like to see all photos of this place?')
if choice.lower() == 'yes':
    driver.find_element_by_id('card-label-All').click()
    time.sleep(4)
    buttons = driver.find_elements_by_tag_name('button')
    for button in buttons:
        if button.get_attribute('aria-label') == 'Back':
            button.click()
wait.until(EC.visibility_of_element_located((By.ID, 'widget-mylocation')))
choice = pyautogui.prompt('Would you like to see the reviews of this place?')
time.sleep(4)
driver.close()