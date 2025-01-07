from bs4 import BeautifulSoup
import requests
import pandas as pd
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
response = requests.get('https://www.goodreads.com/list/show/2455.The_Most_Disturbing_Books_Ever_Written', headers=headers)
html_content = response.text

# Parse the HTML
soup = BeautifulSoup(html_content, 'html.parser')
# Titles, authors, ratings
items = soup.find_all('tr')

titles = []
authors = []
ratings = []

for idx, item in enumerate(items):
    title = item.find('a', class_='bookTitle').text.strip()
    author_name = item.find('a', class_='authorName').text
    ratingText = item.find('span', class_='minirating').text
    match = re.search(r'\d+\.\d+', ratingText)
    rating = match.group()
    titles.append(title)
    authors.append(author_name)
    ratings.append(float(rating))

dt = pd.DataFrame({'Title': titles, 'Author': authors, 'Rating': ratings})
dt.index = dt.index + 1
print(dt.head())

avg_rating = dt['Rating'].mean()
print(avg_rating)

author_books_count = dt['Author'].value_counts()
print('Author Books:', author_books_count)
