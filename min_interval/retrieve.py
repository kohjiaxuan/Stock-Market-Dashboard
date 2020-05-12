# Access and read API contents
# Have to read 3 APIs at a time due to limitations of Alpha Vantage API for free use (max 5 accesses per minute)
# Unable to read all 6 stock APIs (FAANGM) at once

import urllib.request, json
import time
# urllib is for opening URLs to get info
# json is for reading raw string from URL into json file
# time is for waiting 1 min before getting more API data
# Limit of 5 API calls per min, so need to run 3 by 3

def stocks(str1='AAPL', str2='MSFT', str3='AMZN', str4='GOOGL', str5='FB', str6='NFLX'):
	APIKEY_ALPHAVANTAGE = "PUTAPIKEYHERE"
	# save url inside variable as raw string
	urlAAPL = r"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=" + str1 + r"&interval=5min&apikey=" + APIKEY_ALPHAVANTAGE
	urlMSFT = r"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=" + str2 + r"&interval=5min&apikey=" + APIKEY_ALPHAVANTAGE
	urlAMZN = r"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=" + str3 + r"&interval=5min&apikey=" + APIKEY_ALPHAVANTAGE

	# use urllib.request.urlopen() to access API from URL links
	responseAAPL = urllib.request.urlopen(urlAAPL)
	responseMSFT = urllib.request.urlopen(urlMSFT)
	responseAMZN = urllib.request.urlopen(urlAMZN)

	# from var saved (HTTPresponse type), use .read() + .decode('utf-8')
	stringAAPL = responseAAPL.read().decode('utf-8')
	stringMSFT = responseMSFT.read().decode('utf-8')
	stringAMZN = responseAMZN.read().decode('utf-8')

	# Access and read API contents
	# Have to read 3 APIs at a time due to limitations of Alpha Vantage API for free use (max 5 accesses per minute)
	# Unable to read all 6 stock APIs (FAANGM) at once
	# Wait for 1 min
	time.sleep(60.1)

	# save url inside variable as raw string
	urlGOOGL = r"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=" + str4 + r"&interval=5min&apikey=" + APIKEY_ALPHAVANTAGE
	urlFB = r"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=" + str5 + r"&interval=5min&apikey=" + APIKEY_ALPHAVANTAGE
	urlNFLX = r"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=" + str6 + r"&interval=5min&apikey=" + APIKEY_ALPHAVANTAGE

	# use urllib.request.urlopen()
	responseGOOGL = urllib.request.urlopen(urlGOOGL)
	responseFB = urllib.request.urlopen(urlFB)
	responseNFLX = urllib.request.urlopen(urlNFLX)

	# from var saved (HTTPresponse type), use .read() + .decode('utf-8')
	stringGOOGL = responseGOOGL.read().decode('utf-8')
	stringFB = responseFB.read().decode('utf-8')
	stringNFLX = responseNFLX.read().decode('utf-8')

	print("Stock data has been retrieved successfully...")

	return [stringAAPL, stringMSFT, stringAMZN, stringGOOGL, stringFB, stringNFLX]