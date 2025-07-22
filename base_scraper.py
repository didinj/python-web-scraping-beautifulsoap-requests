import requests
from bs4 import BeautifulSoup

url = 'http://quotes.toscrape.com'
response = requests.get(url)

# Print the response status and raw HTML
print(response.status_code)
print(response.text)

soup = BeautifulSoup(response.text, 'lxml')  # or 'html.parser' if lxml is not installed

# Print the page title
print(soup.title.text)

quotes = soup.find_all('div', class_='quote')

for quote in quotes:
    text = quote.find('span', class_='text').text
    author = quote.find('small', class_='author').text
    print(f'"{text}" — {author}')

# Find the first quote div
quote = soup.find('div', class_='quote')

# Find all quote divs
quotes = soup.find_all('div', class_='quote')

# Search by multiple attributes
soup.find_all('span', {'class': 'text', 'itemprop': 'text'})

# Select all quote texts using CSS selector
quote_texts = soup.select('div.quote span.text')

for q in quote_texts:
    print(q.text)

# Select the first author's name
author = soup.select_one('div.quote small.author')
print(author.text)

link = soup.select_one('a')
print(link.get('href'))

for quote in quotes:
    link = quote.find('a')
    print(link['href'])  # Same as .get('href')

first_quote = quotes[0]
print(first_quote.find('span', class_='text').parent.name)  # Output: span's parent tag name