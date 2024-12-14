import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By

driver_path = r"D:\Python_HW\chromedriver.exe"
os.environ["PATH"] += os.pathsep + os.path.dirname(driver_path)

chrome_options = (Options())
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.saucedemo.com/")
driver.maximize_window()

username= driver.find_element (By.ID,"user-name")
username.click()
time.sleep(2)
username.send_keys("standard_user")

passw=driver.find_element(By.ID,"password")
passw.click()
time.sleep(2)
passw.send_keys("secret_sauce")

logins=driver.find_element(By.ID,"login-button")
logins.click()

Webpage_Title=driver.title
Current_URL=driver.current_url

print(Webpage_Title)
print(Current_URL)

webpage=driver.find_element(By.XPATH,"/html/body").text
with open ("Webpage_task_11.txt","w") as textfile:
     textfile.write(webpage)
     textfile.close()


