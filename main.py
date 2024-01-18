from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from hold_and_move import move
import time

driver = webdriver.Chrome()

driver.get("https://app.watchduty.org/search_results")
driver.maximize_window()

xpath = '/html/body/div/div/div/div/div/div[1]/div/div/input'
count = 0
while True:
    try:
        inputElement = driver.find_element(By.XPATH, xpath)
        break
    except:
        time.sleep(3)
        count += 1
    if count==10:
        break
count = 0 
inputElement.send_keys('Duck Creek Village') #helena west side #Duck Creek Village #Cottage groove #Boise #Del Norte County #Kuna #Spokane
inputElement.send_keys(Keys.ENTER)

dropdown_xpath = '/html/body/div/div/div/div/div/div[2]/div/ul/li[1]'
dropdown_element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, dropdown_xpath))
)

dropdown_element.click()
time.sleep(10)

xpath = "//button[@aria-label='Zoom Out']"
button_element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, xpath))
)

for i in range(3):
    button_element.click()
    time.sleep(1)

move(14, 150, 150, driver)
time.sleep(10)

driver.quit()
