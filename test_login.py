from selenium.webdriver.common.by import By


def test_login_valid(driver):
    username_field = driver.find_element(By.CSS_SELECTOR,"#user-name")
    password_field = driver.find_element(By.CSS_SELECTOR,"#password")
    login_button = driver.find_element(By.CSS_SELECTOR,"input#login-button")

    username_field.send_keys("standard_user")
    password_field.send_keys("secret_sauce")
    login_button.click()

    # Validate Login or not
    expected_url = "https://www.saucedemo.com/inventory.html"
    actual_url = driver.current_url
    assert expected_url == actual_url, f"Login failed !!"

    print("Assertion passed.Test Login Valid executed.")


def test_login_invalid(driver):
    username_field = driver.find_element(By.CSS_SELECTOR, "#user-name")
    password_field = driver.find_element(By.CSS_SELECTOR, "#password")
    login_button = driver.find_element(By.CSS_SELECTOR, "input#login-button")

    username_field.send_keys("standard_user")
    password_field.send_keys("1234")
    login_button.click()

    # Validate Login or not
    expected_error_message = "Epic sadface: Username and password do not match any user in this service"
    actual_error_message = driver.find_element(By.CSS_SELECTOR,"[data-test='error']").text
    assert expected_error_message == actual_error_message, f"Error Message Not Found or Mismatch!!"

    print("Assertion passed, Test Login InValid executed.")

