# web_scraper.py

import requests
from bs4 import BeautifulSoup
url = 'URL URL URL'
r = requests.get(url, headers={'user-agent': 'INSERT USER AGENT'})
soup = BeautifulSoup(r.text, "lxml")
body = soup.body  
div = body.find('div', {'class': 'CLASS NAME'}) 
print(type(div.find('WHAT TO FIND?')))
links = div('a', {'rel': 'nofollow'})
for link in links[:10]:
    print(link.text)
rel = links[0].get('rel')
href = links[0].get('href')
	
from urllib.parse import urljoin
for relative_link in links[:10]:
    absolute_link = urljoin(url, relative_link)
    print(absolute_link)

from urllib.parse import urlparse
protocol = urlparse(url).scheme
netloc = urlparse(url).netloc
	
relative = urlparse(url).path
query = urlparse('LINK LINK LINK').query

def get_absolute_link(relative_link: str) -> str:
    protocol = urlparse(url).scheme  
    netloc = urlparse(url).netloc
    absolute_link: str = protocol + "://" + netloc + relative_link
    return absolute_link
	
for link in links:
    href: str = link.get('href')
    if href.startswith("/r"):
        print(urljoin(url, href))