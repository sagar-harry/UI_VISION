import pyautogui
import time
import math
import subprocess
import os
from verify import validate_elements
import pandas as pd
import shutil
import sys

def move(diagonal_inches, miles_right, miles_below, driver):
    time.sleep(3)
    exp_count = 1
    screen_width, screen_height = pyautogui.size()
    diagonal_pixels = math.hypot(screen_width, screen_height)
    ppi = diagonal_pixels/diagonal_inches

    horizontal_distance_cm = 10
    distance_inch  = horizontal_distance_cm/2.54
    distance_pixels = int(distance_inch * ppi)
    start_x, start_y = screen_width//2, screen_height//2

    number_of_horizontal_slides = miles_right//(3*horizontal_distance_cm)
    
    vertical_distance_cm = 5
    number_of_vertical_slides = miles_below//(3*vertical_distance_cm)
    vertical_distance_inch  = vertical_distance_cm/2.54
    vertical_distance_pixels = int(vertical_distance_inch * ppi)

    pyautogui.click()
    sign = 0
    df = pd.DataFrame(columns=["Place name", "Status from description", "Status from UI", "Accuracy"])
    work_dir = os.getcwd().replace("\\", "/")
    input_dir = os.path.join(os.getcwd(), "Data/input").replace("\\", "/")
    output_dir = os.path.join(os.getcwd(), "Data/output").replace("\\", "/")
    env_dir = sys.prefix.replace("\\", "/")

    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    os.mkdir(output_dir)
    if os.path.exists(input_dir):
        shutil.rmtree(input_dir)
    os.mkdir(input_dir)

    for j in range(2):
        if sign!=0:
            vend_x, vend_y = start_x, start_y-vertical_distance_pixels
            pyautogui.moveTo(start_x, start_y, duration=0)
            pyautogui.mouseDown()
            pyautogui.moveTo(vend_x, vend_y, duration=1)
            pyautogui.mouseUp()
            pyautogui.moveTo(start_x, start_y, duration=0)

        for i in range(2):
            time.sleep(8)
            pyautogui.screenshot(os.path.join(input_dir, f"temp_{str(j)}_{str(i)}.png"))
            command = f"cd {env_dir}/Scripts && activate && python {work_dir}/model_42/content/yolov5/detect.py --weights {work_dir}/model_42/content/yolov5/runs/train/exp5/weights/best.pt --img 640 --conf 0.3 --project {work_dir}/Data/output --save-txt --save-conf --source {work_dir}/Data/input/temp_{str(j)}_{str(i)}.png"
            subprocess.call(command, shell=True)
            if exp_count==1:
                if os.path.exists(os.path.join(f"{work_dir}/Data/output/exp/labels", f"temp_{str(j)}_{str(i)}.txt")):
                    all_elements = validate_elements(os.path.join(f"{work_dir}/Data/output/exp", f"temp_{str(j)}_{str(i)}.png"), os.path.join(f"{work_dir}/Data/output/exp/labels", f"temp_{str(j)}_{str(i)}.txt"), driver)
                else: all_elements=[]
            else:
                if os.path.exists(os.path.join(f"{work_dir}/Data/output/exp{str(exp_count)}/labels", f"temp_{str(j)}_{str(i)}.txt")):
                    all_elements = validate_elements(os.path.join(f"{work_dir}/Data/output/exp{str(exp_count)}", f"temp_{str(j)}_{str(i)}.png"), os.path.join(f"{work_dir}/Data/output/exp{str(exp_count)}/labels", f"temp_{str(j)}_{str(i)}.txt"), driver)
                else: all_elements=[]
            exp_count += 1
            if len(all_elements)>0:
                
                df_temp = pd.DataFrame(all_elements, columns=["Place name", "Status from description", "Status from UI", "Accuracy"])
                df = pd.concat([df, df_temp])
            if sign%2==0:
                end_x, end_y = start_x-distance_pixels, start_y
            else:
                end_x, end_y = start_x+distance_pixels, start_y
            time.sleep(3)
            pyautogui.moveTo(start_x, start_y, duration=0)
            pyautogui.mouseDown()
            pyautogui.moveTo(end_x, end_y, duration=1)
            pyautogui.mouseUp()
            pyautogui.moveTo(start_x, start_y, duration=0)
        sign+=1
    # df.to_csv("output.csv", index=False)
    driver.close()
