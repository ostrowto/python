# app_2.py scrapper by Dev Ed https://www.youtube.com/watch?v=Bg9r_yLk7VY

import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.de/Lenovo-ST50-XEON-2124G-3-4GHZ/dp/B07MQC15NH/ref=sr_1_2?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=xeon&qid=1573416066&sr=8-2'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0'}


def check_price():
    

    page = requests.get(URL, headers = headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    #print(soup.prettify()) 

    title = soup.find(id='productTitle').get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = int(price[0:3])

    if (converted_price < 600):
        send_mail()

    print(title.strip())
    print(converted_price)


    if(converted_price < 600):
        send_mail()




def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()


    server.login('EMAIL@gmail.com', 'PASSWORDTOGOOGLE')
    subject = 'Price fell down!'
    body = 'Check the Amazon link: https://www.amazon.de/Lenovo-ST50-XEON-2124G-3-4GHZ/dp/B07MQC15NH/ref=sr_1_2?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=xeon&qid=1573416066&sr=8-2'

    msg = f'Subject: {subject}\n\n{body}'

    server.sendmail('EMAIL_SENDER@gmail.com', 'EMAIL_RECIVER@outlook.com', msg)

    print('Hey Email has been sent!')

    server.quit()

#check_price()

while(True):
    check_price()
    time.sleep(60)
