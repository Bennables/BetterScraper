from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://webscraper.io/test-sites/e-commerce/allinone")
title = driver.title


driver.implicitly_wait(1)

text_box = driver.find_elements(by=By.CLASS_NAME, value="title")

#get_attribute("value") is used to get the value of the input element,
#.text is the text inside the html element
value = text_box[0].text
print (value)







print("ddd\n\n")

driver.quit()
