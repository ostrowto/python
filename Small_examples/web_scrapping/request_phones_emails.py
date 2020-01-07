# request_phones_emails.py

import requests
import re

data_import = requests.get('https://WEBSITE WRITE HERE')

# phones like 12 123 45 57
phones_to_search = re.findall(r'(\(?[0-9]{2}\)?(?:\-|\s|\.)?[0-9]{3}(?:\-|\.)[0-9]{2})?[0-9]{3}(?:\-|\.)[0-9]{2}', data_import.text)
emails_to_search = re.findall(r'([\d\w\.]+@[\d\w\.\-]+\.\w+)', data_import.text)

print(phones_to_search, emails_to_search)