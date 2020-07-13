import requests
from bs4 import BeautifulSoup
import time

def flipkart_price_check(tele_token,chat_id,my_price,url):
    your_price = my_price
    URL = url
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
    tele_id = chat_id
    tele_url = 'https://api.telegram.org/bot{}'.format(tele_token)+'/sendMessage?chat_id={}'.format(tele_id)+'&text='
    tele_url_cmd = tele_url + '<b> PRICE IS DOWN GOO AND PURCHAES ! \n' + titile + '\n' + price + '</b> \n <pre>' + URL + '</pre>'+'&parse_mode=html' 
    tele_url_cmd_else = tele_url + '<b> THIS IS TODAYS PRICE \n' + titile + '\n' + price + '</b>' + '&parse_mode=html'
    if(final_price < your_price):
        requests.get(tele_url_cmd)
    else: 
        requests.get(tele_url_cmd_else)
        

