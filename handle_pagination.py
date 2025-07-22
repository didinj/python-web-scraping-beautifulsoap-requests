import requests
from bs4 import BeautifulSoup

base_url = 'http://quotes.toscrape.com'
next_page = '/'

while next_page:
    # Fetch and parse the page
    response = requests.get(base_url + next_page)
    soup = BeautifulSoup(response.text, 'lxml')

    # Extract quotes
    quotes = soup.find_all('div', class_='quote')
    for quote in quotes:
        text = quote.find('span', class_='text').text
        author = quote.find('small', class_='author').text
        print(f'"{text}" — {author}')

    # Check for next page
    next_button = soup.find('li', class_='next')
    if next_button:
        next_page = next_button.find('a')['href']
    else:
        next_page = None
