import requests_html, json, time
errFlag=False
def reqAllCoins():
	try:
		return json.loads(requests_html.HTMLSession().get('https://api.mexc.com/api/v3/ticker/price').text)
	except:
		errFlag=True
		f = open('../../var/www/wana/log.txt', 'a')
		f.write(time.asctime()+' ошибка получения списка монеток / error getting list of coins')
		f.close()
def reqSplitSymbol(symbol):
	try:
		splitSymbol = json.loads(requests_html.HTMLSession().get('https://api.mexc.com/api/v3/exchangeInfo?symbol='+symbol).text)
		return splitSymbol['symbols'][0]['baseAsset']+'_'+splitSymbol['symbols'][0]['quoteAsset']
	except:
		errFlag=True
		f = open('../../var/www/wana/log.txt', 'a')
		f.write(time.asctime()+' ошибка преобразования символа / symbol conversion error')
		f.close()
for n in reqAllCoins():
	if n['price'] == '0':
		sym_bol = reqSplitSymbol(n['symbol'])
