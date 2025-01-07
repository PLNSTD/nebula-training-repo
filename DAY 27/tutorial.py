import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://example.com"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, "html.parser")
element = soup.select_one("#bodycontainer > div.mainContentContainer > div.mainContent > div.mainContentFloat > div.leftContainer > div.coverBigBox.clearFloats.bigBox > div.bigBoxBody > div")
print(element)

'''response = requests.get('http://books.toscrape.com')
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
print('Total book under 10:', tot_books_under_10)'''