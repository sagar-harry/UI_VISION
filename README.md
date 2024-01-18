# UI VISION
Computer vision based UI testing framework

<details>
  <summary>Why is this project needed? (click here)</summary>
Current approach: </br>
1. UI testing automation tools currently in market generally use element analysis, css of the page or other attributes that are involved the frontend for testing </br>
2. Usually the automation engineer analysis the website and prepares his script with keys for every element that requires some actions to be performed on </br>

Issues with current approach: </br>
1. UI testing should solely depend on the UI not based on script of the UI, in the current frameworks that script is utilized </br>
2. Changes in code would lead to changes in automation script

Limitations: </br>
1. If a website is not interactable then automating it using the current tools would no tbe possible
2. Any third party add-ons present in web app cannot be tested using current tools if they are not interactable

Proposed approach:
A comprehensive UI testing framework using AI </br>
1.Replicate human like capabilities in automated UI testing </br>
2.Use compute vision to identify elements </br>
3.Use Selenium and other python libraries for performing actions </br>

Computer vision replicates humans in terms of vision, any UI testing framework built using computer vision would be the ideal approach to test UI </br>
</details>

## Project description
The website [https://app.watchduty.org/] that has been used in this project is a US based wild fire watch duty website. This website shows the areas where wild fires have occured in Nevada. </br>
There is a map on website on which icons are present, the map is not inspectable and hence tools like selenium cannot be used to perform any actions on them. </br>
</br>
</br>
Snapshot of website: </br> 
</br> 
<img width="960" alt="image" src="https://github.com/sagar-harry/UI_VISION/assets/68346310/6c97820a-eddd-4df6-ab25-5efc7bac459e">

#### Training process:
1. Several snapshots of the website have been taken and bounding boxes have been drawn around icons
2. The annotated dataset has been used to train an object detection model

#### Program flow:
1. Use selenium to open website and enter the address
2. Take a snapshot of the site and feed to object detection model
3. Annotations from model have to be fed to pyautogui library which controls the clickable actions
4. Then scrape the elements whose information is necessary(if needed)
5. Navigate back to map again, move the map based on user's need (top, left, right, bottom)

## How to run:
1. Clone the repository and go to root directory.
2. Create a virtual environment for python: </br>
```python -m venv ui_vision_venv1``` 
3. Activate the environment: </br>
```cd ui_vision_venv1\Scripts``` </br>
```activate```
4. Navigate back to root directory: </br>
   ```cd ..``` </br>
   ```cd ..```
5. Install the requirements: </br>
   ```pip install -r requirements.txt```
6. Run the script: </br>
   ```python main.py```
