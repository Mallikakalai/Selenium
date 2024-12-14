import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver_path = r"D:\Python_HW\chromedriver.exe"
os.environ["PATH"] += os.pathsep + os.path.dirname(driver_path)
chrome_options = (Options())
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

#Navigate to the Intagram page
driver.get("https://www.instagram.com/guviofficial/")
driver.maximize_window()

followers_element = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/section/main/div/header/section/div[3]/ul/li[2]/div/button/span")))
following_element = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/section/main/div/header/section/div[3]/ul/li[3]/div/button/span/span")))

#Fetching the followers and following details
followers_count_exact = followers_element.get_attribute("title") ##tried using attribute method
followers_count= followers_element.text
following_count = following_element.text

print(f"Followers Exact Count: {followers_count_exact}")
print(f"Followers: {followers_count}")
print(f"Following: {following_count}")

# Close the browser
driver.quit()