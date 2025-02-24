from selenium.webdriver.common.by import By

from test_login import test_login_valid


def test_order(driver):

    test_login_valid(driver)

    backpack_add_to_cart_button = driver.find_element(By.CSS_SELECTOR, "button#add-to-cart-sauce-labs-backpack")
    backpack_add_to_cart_button.click()

    shopping_cart= driver.find_element(By.CSS_SELECTOR, "[data-test='shopping-cart-link']")
    shopping_cart.click()

    expected_product_name = "Sauce Labs Backpack"
    actual_product_name = driver.find_element(By.CSS_SELECTOR, "[data-test='inventory-item-name']").text
    assert expected_product_name == actual_product_name, f"Product Not Found or Mismatch!!"

    print("Assertion passed, Product added shopping cart.")

    checkout_button = driver.find_element(By. CSS_SELECTOR, "[name='checkout']")
    checkout_button.click()

    checkout_first_name = driver.find_element(By.CSS_SELECTOR,"#first-name")
    checkout_last_name =  driver.find_element(By.CSS_SELECTOR,"#last-name")
    checkout_zip_code = driver.find_element(By.CSS_SELECTOR, "#postal-code")
    continue_button = driver.find_element(By.CSS_SELECTOR, "[name='continue']")

    checkout_first_name.send_keys("Test first name")
    checkout_last_name.send_keys('Test last name')
    checkout_zip_code.send_keys("123454")
    continue_button.click()

    expected_url = "https://www.saucedemo.com/checkout-step-two.html"
    actual_url = driver.current_url
    assert expected_url == actual_url, f"Checkout Step 2 Failed !!"

    print("Assertion passed, Checkout Step 2 success.")

    finish_button = driver.find_element(By.CSS_SELECTOR, "button#finish")
    finish_button.click()

    expected_confirm_message = "Thank you for your order!"
    actual_confirm_message = driver.find_element(By.CSS_SELECTOR, "[data-test='complete-header']").text
    assert expected_confirm_message == actual_confirm_message, f"Confirmation Message Not Fount or Match!!"

    print("Assertion passed, Checkout Complete success.")