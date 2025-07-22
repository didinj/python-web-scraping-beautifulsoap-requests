import requests
from bs4 import BeautifulSoup
import time
import random

base_url = 'http://quotes.toscrape.com'
next_page = '/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
}

while next_page:
    try:
        # Fetch page with headers
        response = requests.get(base_url + next_page, headers=headers, timeout=5)
        response.raise_for_status()

        # Parse the page content
        soup = BeautifulSoup(response.text, 'lxml')
        quotes = soup.find_all('div', class_='quote')

        for quote in quotes:
            text = quote.find('span', class_='text').text
            author = quote.find('small', class_='author').text
            print(f'"{text}" — {author}')

        # Find the next page link
        next_button = soup.find('li', class_='next')
        next_page = next_button.find('a')['href'] if next_button else None

        # Be respectful
        time.sleep(random.uniform(1, 3))

    except requests.exceptions.RequestException as e:
        print(f"Error fetching page: {e}")
        break
