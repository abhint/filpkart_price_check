from flipkart_price_bot import flipkart_price_check

my_price = 25000
url = 'https://www.flipkart.com/redmi-k20-pro-flame-red-128-gb/p/itmfg7uysw6gs55a'
tele_token = '<your bot token>'
chat_id  = '<your chat id>'


flipkart_price_check(tele_token,chat_id,my_price,url)