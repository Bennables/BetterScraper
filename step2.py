from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import numpy as np


driver = webdriver.Chrome()
driver.get("https://webscraper.io/test-sites/e-commerce/allinone/")

page_source = driver.page_source
soup = BeautifulSoup(page_source, 'html.parser')



driver.implicitly_wait(1)

"""by
class name
id
css
link text
name
partial link text
tagname
xpath
"""

item_names = driver.find_elements(by=By.CLASS_NAME, value="title")
ratings=  soup.find_all('p')
arr = []

for x in ratings:
    if x.has_attr('data-rating'):
        arr.append(x['data-rating'])





#get_attribute("value") is used to get the value of the input element,
#.text is the text inside the html element
# value = item_names[0].text
# print (value)

for i, element in enumerate(item_names):
    print(element.text +"    " +  arr[i])



driver.quit()
