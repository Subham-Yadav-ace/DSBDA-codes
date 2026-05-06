!pip install requests beautifulsoup4

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://webscraper.io/test-sites/e-commerce/static"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
products = soup.find_all("div", class_="thumbnail")

names = []
prices = []
reviews = []
lengths = []

for p in products:
    name = p.find("a", class_="title").text.strip()
    price = p.find("h4", class_="price").text.strip()
    desc = p.find("p", class_="description").text.strip()

    names.append(name)
    prices.append(price)
    reviews.append(desc)
    lengths.append(len(desc))

    print("Product:", name)
    print("Price:", price)
    print("Review:", desc)
    print("-"*50)

df = pd.DataFrame({
    "Customer": names,
    "Price": prices,
    "Review": reviews,
    "Length": lengths
})

df.head()

print("Total Reviews:", len(reviews))