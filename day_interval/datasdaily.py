# Build lists to store information for stock prices at (open, close, high, low) at 5 minute intervals
# This step can be built into a Python Class in the future to allow users to select their own stock names

# https://www.powercms.in/blog/how-get-json-data-remote-url-python-script

import json
# from class datetime import subclass datetime
from datetime import datetime
import numpy as np

def transformdata(string1,string2,string3,string4,string5,string6,startdate):
    # load string saved into json data
    jsondataAAPL = json.loads(string1)
    jsondataAMZN = json.loads(string2)
    jsondataGOOGL = json.loads(string3)
    jsondataFB = json.loads(string4)
    jsondataMSFT = json.loads(string5)
    jsondataNFLX = json.loads(string6)


    # Get all keys of time series (datetime) as string type and save it onto a list
    timeAAPL = list(reversed(list(jsondataAAPL['Time Series (Daily)'].keys())))
    timeAMZN = list(reversed(list(jsondataAMZN['Time Series (Daily)'].keys())))
    timeGOOGL = list(reversed(list(jsondataGOOGL['Time Series (Daily)'].keys())))
    timeFB = list(reversed(list(jsondataFB['Time Series (Daily)'].keys())))
    timeMSFT = list(reversed(list(jsondataMSFT['Time Series (Daily)'].keys())))
    timeNFLX = list(reversed(list(jsondataNFLX['Time Series (Daily)'].keys())))

    # Get element index/position for start date
    try:
        startposition = timeAAPL.index(startdate)
    except:
        startposition = 0

        
    AAPLopen = []
    AAPLhigh = []
    AAPLlow = []
    AAPLclose = []
    AMZNopen = []
    AMZNhigh = []
    AMZNlow = []
    AMZNclose = []
    GOOGLopen = []
    GOOGLhigh = []
    GOOGLlow = []
    GOOGLclose = []
    FBopen = []
    FBhigh = []
    FBlow = []
    FBclose = []
    MSFTopen = []
    MSFThigh = []
    MSFTlow = []
    MSFTclose = []
    NFLXopen = []
    NFLXhigh = []
    NFLXlow = []
    NFLXclose = []
    timeAAPL_s = []
    timeAMZN_s = []
    timeGOOGL_s = []
    timeFB_s = []
    timeMSFT_s = []
    timeNFLX_s = []

    # Get all the stock information using the datetime key used in the JSON packet
    trackposition = -1
    for string in timeAAPL:
        trackposition += 1
        if trackposition < startposition:
            continue
        timeAAPL_s.append(string[:])
        AAPLopen.append(float(jsondataAAPL['Time Series (Daily)'][string]['1. open']))
        AAPLhigh.append(float(jsondataAAPL['Time Series (Daily)'][string]['2. high']))
        AAPLlow.append(float(jsondataAAPL['Time Series (Daily)'][string]['3. low']))
        AAPLclose.append(float(jsondataAAPL['Time Series (Daily)'][string]['4. close']))

    trackposition = -1
    for string in timeAMZN:
        trackposition += 1
        if trackposition < startposition:
            continue
        timeAMZN_s.append(string[:])
        AMZNopen.append(float(jsondataAMZN['Time Series (Daily)'][string]['1. open']))
        AMZNhigh.append(float(jsondataAMZN['Time Series (Daily)'][string]['2. high']))
        AMZNlow.append(float(jsondataAMZN['Time Series (Daily)'][string]['3. low']))
        AMZNclose.append(float(jsondataAMZN['Time Series (Daily)'][string]['4. close']))

    trackposition = -1
    for string in timeGOOGL:
        trackposition += 1
        if trackposition < startposition:
            continue
        timeGOOGL_s.append(string[:])
        GOOGLopen.append(float(jsondataGOOGL['Time Series (Daily)'][string]['1. open']))
        GOOGLhigh.append(float(jsondataGOOGL['Time Series (Daily)'][string]['2. high']))
        GOOGLlow.append(float(jsondataGOOGL['Time Series (Daily)'][string]['3. low']))
        GOOGLclose.append(float(jsondataGOOGL['Time Series (Daily)'][string]['4. close']))
        
    trackposition = -1
    for string in timeFB:
        trackposition += 1
        if trackposition < startposition:
            continue
        timeFB_s.append(string[:])
        FBopen.append(float(jsondataFB['Time Series (Daily)'][string]['1. open']))
        FBhigh.append(float(jsondataFB['Time Series (Daily)'][string]['2. high']))
        FBlow.append(float(jsondataFB['Time Series (Daily)'][string]['3. low']))
        FBclose.append(float(jsondataFB['Time Series (Daily)'][string]['4. close']))

    trackposition = -1
    for string in timeMSFT:
        trackposition += 1
        if trackposition < startposition:
            continue
        timeMSFT_s.append(string[:])
        MSFTopen.append(float(jsondataMSFT['Time Series (Daily)'][string]['1. open']))
        MSFThigh.append(float(jsondataMSFT['Time Series (Daily)'][string]['2. high']))
        MSFTlow.append(float(jsondataMSFT['Time Series (Daily)'][string]['3. low']))
        MSFTclose.append(float(jsondataMSFT['Time Series (Daily)'][string]['4. close']))
        
    trackposition = -1
    for string in timeNFLX:
        trackposition += 1
        if trackposition < startposition:
            continue
        timeNFLX_s.append(string[:])
        NFLXopen.append(float(jsondataNFLX['Time Series (Daily)'][string]['1. open']))
        NFLXhigh.append(float(jsondataNFLX['Time Series (Daily)'][string]['2. high']))
        NFLXlow.append(float(jsondataNFLX['Time Series (Daily)'][string]['3. low']))
        NFLXclose.append(float(jsondataNFLX['Time Series (Daily)'][string]['4. close']))
        
      
    # Create normalized list of 9 companies stock prices by the price at opening
    # This is used for plotting the relative stock performance chart (% movement in a day) for all 6 stocks
    AAPLdailyopen_n = np.array(AAPLopen)/AAPLopen[0]
    AMZNdailyopen_n = np.array(AMZNopen)/AMZNopen[0]
    GOOGLdailyopen_n = np.array(GOOGLopen)/GOOGLopen[0]
    FBdailyopen_n = np.array(FBopen)/FBopen[0]
    MSFTdailyopen_n = np.array(MSFTopen)/MSFTopen[0]
    NFLXdailyopen_n = np.array(NFLXopen)/NFLXopen[0]

    # Get percentage change of each stock to show in the title of graphs
    AAPL_change = round((AAPLopen[-1] - AAPLopen[0])/AAPLopen[0] * 100,2)
    AMZN_change = round((AMZNopen[-1] - AMZNopen[0])/AMZNopen[0] * 100,2)
    GOOGL_change = round((GOOGLopen[-1] - GOOGLopen[0])/GOOGLopen[0] * 100,2)
    FB_change = round((FBopen[-1] - FBopen[0])/FBopen[0] * 100,2)
    MSFT_change = round((MSFTopen[-1] - MSFTopen[0])/MSFTopen[0] * 100,2)
    NFLX_change = round((NFLXopen[-1] - NFLXopen[0])/NFLXopen[0] * 100,2)

    return {"daily": [AAPLdailyopen_n, AMZNdailyopen_n, GOOGLdailyopen_n, FBdailyopen_n, MSFTdailyopen_n, NFLXdailyopen_n],
            "change": [AAPL_change, AMZN_change, GOOGL_change, FB_change, MSFT_change, NFLX_change],
            "time": [timeAAPL_s, timeAMZN_s, timeGOOGL_s, timeFB_s, timeMSFT_s, timeNFLX_s],
            "open": [AAPLopen, AMZNopen, GOOGLopen, FBopen, MSFTopen, NFLXopen],
            "high": [AAPLhigh, AMZNhigh, GOOGLhigh, FBhigh, MSFThigh, NFLXhigh],
            "low": [AAPLlow, AMZNlow, GOOGLlow, FBlow, MSFTlow, NFLXlow],
            "close": [AAPLclose, AMZNclose, GOOGLclose, FBclose, MSFTclose, NFLXclose]
            }