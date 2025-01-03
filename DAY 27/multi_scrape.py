from bs4 import BeautifulSoup
import requests
import pandas as pd

# Initialize lists to store scraped data
quotes = []
authors = []
tags = []

for i in range(1,10):
    # Fetch the webpage
    response = requests.get(f'http://quotes.toscrape.com/page/{i}/')
    html_content = response.text

    # Parse the HTML
    soup = BeautifulSoup(html_content, 'html.parser')
    # Find quote Container
    quotesContainer = soup.find_all('div', class_='quote')
    for quoteBlock in quotesContainer:
        # Find the quote
        quote = quoteBlock.find('span', class_='text').text
        quotes.append(quote)

        # Find the author
        author = quoteBlock.find('small', class_='author').text
        authors.append(author)

        # Find the tags for the quote
        tagsA = quoteBlock.find_all('a', class_='tag')
        block_tags = []
        for tag in tagsA:
            block_tags.append(tag.text)  
        tags.append(block_tags)

# Create a DataFrame
pd = pd.DataFrame({'Quote': quotes, 'Author': authors, 'Tags': tags})
# print(pd.head())

# Calculate which author has the most quotes
author_count = pd['Author'].value_counts()
common_words_in_quotes = pd['Quote'].str.split(expand=True).stack().value_counts()

print('Common words in quotes:\n', common_words_in_quotes.head())
print('Authors with the most quotes:\n', author_count.head())

