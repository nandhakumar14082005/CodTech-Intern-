from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 10)

try:
    driver.get("https://the-internet.herokuapp.com/login")
    print("Opened login page")

    username = wait.until(
        EC.presence_of_element_located((By.ID, "username"))
    )
    password = driver.find_element(By.ID, "password")

    username.send_keys("tomsmith")
    password.send_keys("SuperSecretPassword!")
    print("Entered login credentials")

    login_button = driver.find_element(By.CSS_SELECTOR, "button.radius")
    login_button.click()
    print("Clicked login button")

    success_message = wait.until(
        EC.presence_of_element_located((By.ID, "flash"))
    )
    assert "You logged into a secure area!" in success_message.text
    print("Login successful")

    current_url = driver.current_url
    assert "secure" in current_url
    print("Navigation to secure area verified")

    logout_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a.button"))
    )
    logout_button.click()
    print("Clicked logout button")

    logout_message = wait.until(
        EC.presence_of_element_located((By.ID, "flash"))
    )
    assert "You logged out of the secure area!" in logout_message.text
    print("Logout successful")

except TimeoutException:
    print("Element not found within timeout period")

except AssertionError:
    print("Assertion failed")

finally:
    time.sleep(3)
    driver.quit()
    print("Browser closed")