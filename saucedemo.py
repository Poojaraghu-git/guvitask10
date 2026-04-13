from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
#to get title of the webpage
print("The title of the webpage is:: ", driver.title)
time.sleep(2)
#to get current url of the webpage
print("The current url is:: ", driver.current_url)
time.sleep(2)
#to extract and save the content of the webpage
pagesource = driver.page_source
with open("Webpage_task_11.txt", "w") as file:
    file.write(pagesource)



