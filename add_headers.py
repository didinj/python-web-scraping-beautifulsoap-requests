import requests
import time
import random

base_url = 'http://quotes.toscrape.com'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
}

response = requests.get('http://quotes.toscrape.com', headers=headers)

try:
    response = requests.get(base_url, headers=headers, timeout=5)
    response.raise_for_status()  # Raise error if not 2xx
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")

time.sleep(1) # 1 second delay between requests
time.sleep(random.uniform(1, 3))  # Delay between 1 and 3 seconds