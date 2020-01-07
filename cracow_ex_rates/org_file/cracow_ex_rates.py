# scrap_soup_1.py

import sys
import requests
from bs4 import BeautifulSoup
from datetime import datetime

import_data = requests.get('http://www.kantorgrosz.pl/index.php/kursywalut')
import_data_2 = requests.get('https://www.baksy.pl/kurs-walut')

web_site_to_analize_grosz = BeautifulSoup(import_data.text, 'html.parser')
web_site_to_analize_baksy = BeautifulSoup(import_data_2.text, 'html.parser')

list_of_values_grosz = []
list_of_values_baksy = []

for tr in web_site_to_analize_grosz.find_all('tr'):
    for td in tr.find_all('td'):
        #print(td.text)
        #xxx_2 = str(td.text)
        list_of_values_grosz.append(td.text)
        

for tr in web_site_to_analize_baksy.find_all('tr'):
    for td in tr.find_all('td'):
        #print(td.text)
        #xxx_2 = str(td.text)
        list_of_values_baksy.append(td.text)

filename_datetime = datetime.now().strftime("\n\n\tDate: %Y-%m-%d Time: %H:%M:%S")

sys.stdout = open('Your_exchange_rates.txt', 'w')
print('Date and time of creation: ', filename_datetime)
print(' ')
print(50*'-')
print('http://www.kantorgrosz.pl/index.php/kursywalut')
print(50*'-')
print(' ')
for i in list_of_values_grosz:
    print(i)
    print(' ')
print(' ')
print('Data as string list: ', list_of_values_grosz)
print(' ')

print(50*'*')
print(50*'*')
print(50*'*')


print(' ')
print(40*'-')
print('https://www.baksy.pl/kurs-walut')
print(40*'-')
print(' ')
for i in list_of_values_baksy:
    print(i)
    print(' ')
print(' ')
print('Data as string list: ', list_of_values_baksy)
print(' ')

sys.stdout.close()
