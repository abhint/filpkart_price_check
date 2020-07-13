import requests
from bs4 import BeautifulSoup
import time

your_price = 40000
URL = 'https://www.flipkart.com/asus-rog-phone-ii-black-128-gb/p/itm99be8e028a908'
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
page = requests.get(URL, headers)
soup = BeautifulSoup(page.content, 'html.parser')
titile = soup.find(attrs= '_35KyD6').get_text()
price  = soup.find(attrs = '_1vC4OE _3qQ9m1').get_text()
convert_first_price = price[1:3]
convert_sencond_price = price[4:7]
final_price = float(convert_first_price + convert_sencond_price)
your_price  = float(your_price)
print(titile)
print(price)
tele_token = '1306098991:AAEetTcs5EqM7JH-9hlfNXpVGFQaa-hc7_U'
tele_id = '1070202696'
tele_url = 'https://api.telegram.org/bot{}'.format(tele_token)+'/sendMessage?chat_id={}'.format(tele_id)+'&text='
tele_url_cmd = tele_url + '<b>' + titile + '\n' + price + '</b> \n <pre>' + URL + '</pre>'+'&parse_mode=html' 
print(tele_url_cmd)

if(final_price < your_price):
    requests.get(tele_url_cmd)
else: 
    print("")
