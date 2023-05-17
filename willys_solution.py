import requests
from bs4 import BeautifulSoup

# Make a request to the webpage
response = requests.get("https://webscraper.io/test-sites/e-commerce/allinone/")
# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Find all <p> elements with the "data-rating" attribute inside the "ratings" class
rating_ps = soup.select("div.ratings p[data-rating]")

# Extract the values of the "data-rating" attributes
for rating_p in rating_ps:
    rating_value = rating_p["data-rating"]
    print("Rating:", rating_value)