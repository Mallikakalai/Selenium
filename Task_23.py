from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import os
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
# Navigate to the JQuery page
driver.get("https://jqueryui.com/droppable/")
driver.maximize_window()
time.sleep(3) #wait for the page to load

# switch to the iframe that contains the draggable and droppable elements
iframe = driver.find_element(By.CSS_SELECTOR, ".demo-frame")
driver.switch_to.frame(iframe)

# locate the draggable and droppable elements
draggable = driver.find_element(By.ID, "draggable")
droppable = driver.find_element(By.ID, "droppable")

# drag and drop operation
actions = ActionChains(driver)
actions.drag_and_drop(draggable, droppable).perform()

# wait to observe the result
time.sleep(3)

# print confirmation
print("Drag and drop operation performed successfully.")

# close the browser
driver.quit()

