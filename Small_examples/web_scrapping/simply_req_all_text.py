# simply_req_all_text.py

import requests
from bs4 import BeautifulSoup
url = 'PUT YOUR WWW HERE'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'lxml')
print("This is text from Your`s web:")
print(soup.get_text())