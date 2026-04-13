from selenium.webdriver.common.by import By
import time
#To check Title - Positive scenario
def test_sauce(driver):
    driver.get("https://www.saucedemo.com")
    print("Title of web page", driver.title)
    assert driver.title == "Swag Labs"

#To check Title - Negative scenario
def test_sauce1(driver):
    driver.get("https://www.saucedemo.com")
    print("Title of web page", driver.title)
    assert driver.title == "Sauce demo"

#To check Home page Current url - Positive scenario
def test_sauce2(driver):
    driver.get("https://www.saucedemo.com")
    print("Url of Home page is :: ", driver.current_url)
    assert driver.current_url == "https://www.saucedemo.com/"

#To check Home page Current url - Negative scenario
def test_sauce3(driver):
    driver.get("https://www.saucedemo.com")
    print("Url of Home page is :: ", driver.current_url)
    assert driver.current_url == "https://www.saucedemo.com"

#To check after Login page Current url - Positive scenario
def test_sauce4(driver):
    driver.get("https://www.saucedemo.com")
    driver.find_element(By.XPATH,".//input[@type='text']").send_keys("standard_user")
    time.sleep(1)
    driver.find_element(By.XPATH,".//input[@type='password']").send_keys("secret_sauce")
    time.sleep(1)
    driver.find_element(By.XPATH, ".//input[@type='submit']").click()
    time.sleep(1)
    print("URL of the dashboard after login with credentials: ", driver.current_url)
    assert driver.current_url == "https://www.saucedemo.com/inventory.html"

#To check after Login page Current url - Negative scenario
def test_sauce5(driver):
    driver.get("https://www.saucedemo.com")
    driver.find_element(By.XPATH,".//input[@type='text']").send_keys("standard_user")
    time.sleep(1)
    driver.find_element(By.XPATH,".//input[@type='password']").send_keys("secret_sauce")
    time.sleep(1)
    driver.find_element(By.XPATH, ".//input[@type='submit']").click()
    time.sleep(1)
    print("URL of the dashboard after login with credentials: ", driver.current_url)
    assert driver.current_url == "https://www.saucedemo.com/inventor.html"
