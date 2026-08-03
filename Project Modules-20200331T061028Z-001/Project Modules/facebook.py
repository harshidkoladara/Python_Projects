from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import pyautogui
import time

#open facebook using ChromeDriver
option = Options()
option.add_argument("--disable-notifications")
driver = webdriver.Chrome(chrome_options = option)
driver.maximize_window()
driver.get("https://www.facebook.com")
email = "voiceassistant2479@gmail.com"#pyautogui.prompt("Please enter your email used to make Facebook account")
password = "ajax@2479"#pyautogui.password("Please enter the password for the Facebook account")
driver.find_element_by_id('email').send_keys(email)
driver.find_element_by_id('pass').send_keys(password + "\n")
choice = pyautogui.prompt('Text or Image?')
flag = 1
while flag == 1:
    if choice == "text":
        message = "Hey! How you doing?"
        driver.find_element_by_xpath("//*[@name='xhpc_message']").send_keys(message)
        time.sleep(2)
        buttons = driver.find_elements_by_tag_name('button')
        for button in buttons:
            if 'Post' in button.text:
                button.click()
                flag = 0
    elif choice == "image":
        choice = pyautogui.prompt("Enter the exact name of the image with extension you want to upload")
        driver.find_element_by_link_text('Photo/Video').click()
        time.sleep(1)
        search = pyautogui.locateOnScreen('search.png')
        pyautogui.click(search)
        time.sleep(1)
        pyautogui.typewrite(choice + "\n")
        time.sleep(2)
        pyautogui.hotkey('down')
        pyautogui.typewrite('\n')
        time.sleep(2)
        buttons = driver.find_elements_by_tag_name('button')
        for button in buttons:
            if 'Post' in button.text:
                button.click()
        flag = 0 
time.sleep(4)
driver.close()