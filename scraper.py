import requests
from bs4 import BeautifulSoup
import smtplib
import time


URL = 'https://www.amazon.com/Sony-Alpha-a6400-Mirrorless-Camera/dp/B07MV3P7M8/ref=sr_1_3?keywords=sony+a6400&qid=1574330660&sr=8-3'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'} 

def check_price():
    page = requests.get(URL, headers=headers)
    soup1 = BeautifulSoup(page.content, "html.parser")
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    title = soup2.find(id="productTitle").get_text()
    price = soup2.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[1:4])

    if(converted_price < 800):
        send_mail()

    print(converted_price)
    print(title.strip())

    if(converted_price < 800):
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('amankumar1998official@gmail.com', 'wgfjlcitvvykjhre')

    subject = 'Price fell down!'
    body = 'Cheek out the link https://www.amazon.com/Sony-Alpha-a6400-Mirrorless-Camera/dp/B07MV3P7M8/ref=sr_1_3?keywords=sony+a6400&qid=1574330660&sr=8-3'

    msg = f"Subject: {subject} \n\n {body}"

    server.sendmail(
        'amankumar1998official@gmail.com',
        'amankumar@mail.sfsu.edu',
        msg
    )
    print('Hey email has been sent')

    server.quit()

while(True):
    check_price()
    time.sleep(60 * 60 * 24)