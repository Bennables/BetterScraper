from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path= 'C:/chromedriver.exe')
driver.get("https://www.selenium.dev/selenium/web/web-form.html")
title = driver.title
assert title == "Web form"

driver.implicitly_wait(1)

text_box = driver.find_element(by=By.NAME, value="my-text")
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

text_box.send_keys("Selenium")
print(text_box.get_attribute("value"))
submit_button.click()



message = driver.find_element(by=By.ID, value="message")
value = message.text
print(value)


assert value == "Received!"

print("ddd\n\n")

driver.quit()

