# Access and read API contents

import urllib.request, json
# urllib is for opening URLs to get info
# json is for reading raw string from URL into json file

def stocks(str1='AAPL', str2='MSFT', str3='AMZN', str4='GOOGL'):
	APIKEY_ALPHAVANTAGE = "PUTAPIKEYHERE"
	# save url inside variable as raw string
	urlAAPL = r"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=" + str1 + r"&interval=5min&apikey=" + APIKEY_ALPHAVANTAGE
	urlMSFT = r"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=" + str2 + r"&interval=5min&apikey=" + APIKEY_ALPHAVANTAGE
	urlAMZN = r"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=" + str3 + r"&interval=5min&apikey=" + APIKEY_ALPHAVANTAGE
	urlGOOGL = r"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=" + str4 + r"&interval=5min&apikey=" + APIKEY_ALPHAVANTAGE
	# use urllib.request.urlopen() to access API from URL links
	responseAAPL = urllib.request.urlopen(urlAAPL)
	responseMSFT = urllib.request.urlopen(urlMSFT)
	responseAMZN = urllib.request.urlopen(urlAMZN)
	responseGOOGL = urllib.request.urlopen(urlGOOGL)

	# from var saved (HTTPresponse type), use .read() + .decode('utf-8')
	stringAAPL = responseAAPL.read().decode('utf-8')
	stringMSFT = responseMSFT.read().decode('utf-8')
	stringAMZN = responseAMZN.read().decode('utf-8')
	stringGOOGL = responseGOOGL.read().decode('utf-8')

	print("Stock data has been retrieved successfully...")

	return [stringAAPL, stringMSFT, stringAMZN, stringGOOGL]