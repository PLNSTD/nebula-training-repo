# Introduction to Web Scraping with Beautiful Soup and Pandas 🌐🐍📊

Welcome to your journey into the fascinating world of web scraping with Python! This lecture will introduce you to the basics of extracting data from websites using Beautiful Soup and then manipulating and analyzing this data with Pandas. By the end, you'll embark on a hands-on project to scrape a website and analyze your findings with Pandas. Let's dive in!

## Section 1: Getting Started with Beautiful Soup 🍲

### What is Beautiful Soup?

Beautiful Soup is a Python library designed to scrape information from web pages. It sits atop an HTML or XML parser, providing Pythonic idioms for iterating, searching, and modifying the parse tree.

### Installation

Before we begin, make sure you have Python and pip installed on your system. Then, install Beautiful Soup and the requests library, which we'll use to fetch web pages:

```python
pip install beautifulsoup4 requests
```

### Try It Yourself

1. Install Beautiful Soup and requests if you haven't already.
2. Fetch the HTML of a simple webpage (e.g., http://example.com) using requests.
3. Print the fetched HTML content to ensure it worked.

## Section 2: Parsing HTML with Beautiful Soup 🔍

After fetching a webpage, the next step is to parse its HTML content. Beautiful Soup makes this process straightforward.

### Basic Parsing

```python
from bs4 import BeautifulSoup
import requests

# Fetch the webpage
response = requests.get('http://example.com')
html_content = response.text

# Parse the HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Print the prettified HTML
print(soup.prettify())
```

### Finding Elements

Beautiful Soup allows you to find elements by tags, attributes, or CSS classes.

```python
# Find the title tag
title_tag = soup.find('title')
print(title_tag.text)

# Find all paragraph tags
paragraphs = soup.find_all('p')
for paragraph in paragraphs:
    print(paragraph.text)

# Find elements by class name
highlighted_texts = soup.find_all('p', class_='highlight')
for text in highlighted_texts:
    print(text.text)
```

### Try It Yourself

1. Parse the HTML of a webpage of your choice.
2. Extract and print the text of the title tag.
3. Find and print all links (a tags) on the page.

## Section 3: Analyzing Scraped Data with Pandas 🐼🔍

After you've gotten your feet wet with Beautiful Soup by fetching and parsing HTML content, it's time to put those skills to work by scraping actual data from a webpage and analyzing it with Pandas. We'll scrape book titles and prices from a simple website and perform basic analysis to find the average price of the books.

### Scraping Data

Let's start by scraping book titles and prices from http://books.toscrape.com. We'll focus on just the first page for simplicity.

```python
from bs4 import BeautifulSoup
import requests
import pandas as pd

# Fetch the webpage
response = requests.get('http://books.toscrape.com')
html_content = response.text

# Parse the HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Initialize lists to store scraped data
titles = []
prices = []

# Loop through each book
for book in soup.find_all('article', class_='product_pod'):
    titles.append(book.find('h3').find('a')['title'])
    prices.append(book.find('p', class_='price_color').text[1:])  # Remove the pound sign

# Convert prices to floats
prices = [float(price) for price in prices]

# Display scraped data
print(titles)
print(prices)
```

### Preparing Your Data with Pandas

Now that we have our data in two lists, let's use Pandas to organize this data into a DataFrame for easy manipulation and analysis.

```python
# Create a DataFrame
data = {'Title': titles, 'Price (£)': prices}
df = pd.DataFrame(data)

print(df.head())  # Display the first few rows of the DataFrame
```

### Basic Analysis with Pandas

With our data in a DataFrame, we can easily perform some basic analysis to understand our dataset better. Let's calculate the average price of the books we've scraped.

#### Calculate Average Price

```python
average_price = df['Price (£)'].mean()
print(f"Average Price: £{average_price:.2f}")
```

### Try It Yourself

- **Scraping Part**: Adapt the scraping script to extract additional information from the website, such as availability.
- **Analysis Part**: Use Pandas to count how many books are under £10.

This example walks you through a complete cycle of scraping data from a web page and analyzing that data using Pandas. It's a foundational skill set for any data scientist or anyone interested in extracting insights from web-based data. Remember to respect websites' terms of service and robots.txt files when scraping.

##  Project: Scrape and Analyze Website Data 🚀

### Objective

Your objective is to scrape data from a website that's accessible with Beautiful Soup (ensure the website allows scraping by reviewing its robots.txt file) and to analyze this data using Pandas.

### Steps

1. Choose a website to scrape. For beginners, a simple website with a clear structure is recommended (e.g., http://books.toscrape.com).
2. Use Beautiful Soup to extract relevant data from the site, such as product names, prices, or any data of interest.
3. Store the extracted data in a Pandas DataFrame.
4. Perform basic data analysis—calculate averages, find the most expensive items, or visualize the data using Pandas' plotting capabilities.

### Try It Yourself

- **Scraping Part**: Write a script to scrape data from your chosen website. Focus on extracting at least two related pieces of information (e.g., book names and prices).
- **Analysis Part**: Load your scraped data into a Pandas DataFrame and perform at least two analyses or visualizations.

### Tips

- Respect the website's `robots.txt` policy to ensure ethical scraping.
- Check the website’s terms of service before scraping.
- Test your scraping code incrementally to avoid overwhelming the website's server.

Happy scraping, and enjoy the insights you'll uncover with your analysis!
