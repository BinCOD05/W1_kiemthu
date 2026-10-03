from selenium import webdriver
from selenium.webdriver.common.by import By

def test_home_page():
    driver = webdriver.Chrome()

    driver.get("https://the-internet.herokuapp.com/")

    heading = driver.find_element(By.TAG_NAME, "h1")

    assert heading.text == "Welcome to the-internet"

    driver.quit()