import requests
from bs4 import BeautifulSoup
import pandas as pd

response = requests.get('http://books.toscrape.com')
html_content = response.text

# Parse the HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Initialize lists to store scraped data
titles = []
prices = []
availabilities = []
tot_books_under_10 = 0

# Find all the book info
for book in soup.find_all('article', class_='product_pod'):
    title = book.find('h3').find('a')['title']
    titles.append(title)

    price = float(book.find('p', class_='price_color').get_text()[2:])
    prices.append(price)
    if price < 10: # No books under 10
        tot_books_under_10 += 1
    
    availability = book.find('p', class_='instock availability').get_text().strip()
    availabilities.append(availability)

pd = pd.DataFrame({'Title': titles, 'Price': prices, 'Availability': availabilities})

print(pd.head())
print('Total book under 10:', tot_books_under_10)