from selenium.webdriver.common.by import By
import time
from PIL import Image
import pyautogui


def validate_elements(output_image_path, labels_path, driver):
    pil_image = Image.open(output_image_path)
    all_elements = []
    with open(labels_path) as file:
        elements = file.readlines()
        for element in elements:
            time.sleep(3)
            each_coordinate = element.split(" ")
            status_from_image = ["active", "inactive"][int(each_coordinate[0])]
            x_coordinate = float(each_coordinate[1])*int(pil_image.size[0])
            y_coordinate = float(each_coordinate[2])*int(pil_image.size[1])
            pyautogui.moveTo(x_coordinate, y_coordinate)
            pyautogui.click()
            time.sleep(4)
            area_name_xpath = "/html/body/div/div/div/div/div[2]/div/div/div/div[1]/div/div[1]/h3/span"
            area_name_element = driver.find_element(By.XPATH, area_name_xpath)
            area_name_from_description = area_name_element.text

            status_xpath = "/html/body/div/div/div/div/div[2]/div/div/div/div[1]/div/div[2]/div/div[3]/p"
            status_element = driver.find_element(By.XPATH, status_xpath)
            status_from_description = status_element.text
            backpage_xpath = "/html/body/div/div/header/div/button/span[1]"
            backpage_element = driver.find_element(By.XPATH, backpage_xpath)
            backpage_element.click()
            print(area_name_from_description, status_from_description.lower(), status_from_image.lower())
            all_elements.append((area_name_from_description, status_from_description.lower(), status_from_image.lower(), each_coordinate[5]))

    return all_elements