import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from matplotlib.ticker import LinearLocator
import os
# %matplotlib inline
import retrievedaily
import datasdaily
import legend

def main(stock1, stock2, stock3, stock4, stock5, stock6, startdate=''):
    print('Retrieving stock takes 1 min due to max 5 API call per min, remove time.sleep(60.1) if using premium API account')
    stockdata = retrievedaily.stocks(stock1, stock2, stock3, stock4, stock5, stock6)
    print('Stock data has been successfully retrieved.')
    transformed_data = datasdaily.transformdata(stockdata[0], stockdata[1], stockdata[2], stockdata[3], stockdata[4], stockdata[5], startdate)

    # Create dashboard of stocks
    # There will be 6 small graphs at the top for the daily stock movement for the 6 US tech stocks (FAANGM)
    # A big graph at the bottom comparing the relative performance (in %) of each stock over the day
    # Instead of using the candlestick plot, I used a continuous line plot with dotted lines signifying the higher/lower bound

    # Plan of subplot layering (1x1 one for title, 2x1 for overlaid graphs, 6x3 one for small graphs but only occupy top 9 spaces)

    # Create big figure
    stocks = plt.figure(1,figsize=(24,30))
    plt.style.use('ggplot')

    #Create big subplot for title and remove frame (frameon=False), remove tick parameters
    stocks_title = stocks.add_subplot(111, frameon=False) #remove frame but need remove ticks/axes
    stocks_title.tick_params(labelcolor='none', top=False, bottom=False, left=False, right=False)
    stocks_title.set_title('Daily Stock Prices (USD)', fontsize=24)

    # Determine where to put legend board in relative stock performance graph
    legendjson = legend.legendcalculation(transformed_data["daily"][0], transformed_data["daily"][1], transformed_data["daily"][2], transformed_data["daily"][3], transformed_data["daily"][4], transformed_data["daily"][5])

    #Create big subplot for mega chart using 2x1 plot using normal .add_subplot
    #Change x-axis to be integer (year) and y-axis to be integer (price_index)
    stocks_big = stocks.add_subplot(212)
    #If apple stock is higher than the start (legendjson['stockloc'][0] == 4), add + sign in the stock price
    #If apple stock is lower than the start, number has - sign so + sign is omitted
    #Repeat for all other stocks
    if legendjson['stockloc'][0] == 4:
        AAPL_n = stocks_big.plot(transformed_data["time"][0], transformed_data["daily"][0], '-o', label=stock1+' +'+str(transformed_data["change"][0])+'%', linewidth = 4, markersize=8)
    else:
        AAPL_n = stocks_big.plot(transformed_data["time"][0], transformed_data["daily"][0], '-o', label=stock1+' '+str(transformed_data["change"][0])+'%', linewidth = 4, markersize=8)

    if legendjson['stockloc'][1] == 4:
        AMZN_n = stocks_big.plot(transformed_data["time"][1], transformed_data["daily"][1], '-o', label=stock2+' +'+str(transformed_data["change"][1])+'%', linewidth = 4, markersize=8)
    else:
        AMZN_n = stocks_big.plot(transformed_data["time"][1], transformed_data["daily"][1], '-o', label=stock2+' '+str(transformed_data["change"][1])+'%', linewidth = 4, markersize=8)

    if legendjson['stockloc'][2] == 4:
        GOOGL_n = stocks_big.plot(transformed_data["time"][2], transformed_data["daily"][2], '-o', label=stock3+' +'+str(transformed_data["change"][2])+'%', linewidth = 4, markersize=8)
    else:
        GOOGL_n = stocks_big.plot(transformed_data["time"][2], transformed_data["daily"][2], '-o', label=stock3+' '+str(transformed_data["change"][2])+'%', linewidth = 4, markersize=8)

    if legendjson['stockloc'][3] == 4:
        FB_n = stocks_big.plot(transformed_data["time"][3], transformed_data["daily"][3], '-o', label=stock4+' +'+str(transformed_data["change"][3])+'%', linewidth = 4, markersize=8)
    else:
        FB_n = stocks_big.plot(transformed_data["time"][3], transformed_data["daily"][3], '-o', label=stock4+' '+str(transformed_data["change"][3])+'%', linewidth = 4, markersize=8)

    if legendjson['stockloc'][4] == 4:
        MSFT_n = stocks_big.plot(transformed_data["time"][4], transformed_data["daily"][4], '-o', label=stock5+' +'+str(transformed_data["change"][4])+'%', linewidth = 4, markersize=8)
    else:
        MSFT_n = stocks_big.plot(transformed_data["time"][4], transformed_data["daily"][4], '-o', label=stock5+' '+str(transformed_data["change"][4])+'%', linewidth = 4, markersize=8)

    if legendjson['stockloc'][5] == 4:
        NFLX_n = stocks_big.plot(transformed_data["time"][5], transformed_data["daily"][5], '-o', label=stock6+' +'+str(transformed_data["change"][5])+'%', linewidth = 4, markersize=8)
    else:
        NFLX_n = stocks_big.plot(transformed_data["time"][5], transformed_data["daily"][5], '-o', label=stock6+' '+str(transformed_data["change"][5])+'%', linewidth = 4, markersize=8)
        
    #Get all handle/variable storing the legend in a tuple from 0-8 and also all label of the legend var in a tuple from 0-8
    #Each element n of the tuple has a pair of handle/label associated
    handlesN, labelsN = plt.gca().get_legend_handles_labels()
    order = [0,1,2,3,4,5]
    stocks_big.legend([handlesN[idx] for idx in order],[labelsN[idx] for idx in order], loc=legendjson['legendloc'], fontsize=24)
    #Possible improvement is to detect initial and final position of graphs and relocate legend loc=1,2,3,4 accordingly every day
    stocks_big.tick_params(axis='y', which='major', labelsize=22)
    stocks_big.tick_params(axis='x', which='major', labelsize=12)
    stocks_big.set_title('Relative Graph of Stock Price Index', fontsize=26)
    #Get datetime and add it to x label
    stocks_big.set_xlabel('Index starting from date: ' + transformed_data["time"][0][0],fontsize=24)
    stocks_big.set_ylabel('Stock Price Index',fontsize=24)
    stocks_big.xaxis.set_major_locator(MaxNLocator(integer=True))
    stocks_big.yaxis.set_major_locator(MaxNLocator(integer=True))

    #Horizontal line denoting the starting stock index at beginning of time
    stocks_big.axhline(y=1, color='black', linestyle='--')


    #Create matplotlib figure with subplot size 6x3 plot using fig, axes_small (axes_small is np.array)
    #Found out that it is easier to use big figure and overlay many different size of subplot (1x1 title), (2x1 big chart),
    #(6x3 small charts) into a single matplotlib figure
    #instead of using fig, axes to define fig and axes (matrix size) tgt since there is varying sizes


    #Plot the individual stock graphs for each stock from position 1 to 6 in 6x2 matrix
    #Note that positions 7-12 taken up by big graph. It is equivalent to add_subplot(212) - position 2 in 2x1 matrix

    AAPLplot = stocks.add_subplot(621)
    #AAPLplot.set_xlabel('Date & Time',fontsize=14)
    AAPLplot.set_ylabel('Stock Price (USD)',fontsize=14)
    if legendjson['stockloc'][0] == 4:
        AAPLplot.set_title(stock1+'  Stock Price +'+str(transformed_data["change"][0])+'%',fontsize=20,color='g')
    else:
        AAPLplot.set_title(stock1+'  Stock Price '+str(transformed_data["change"][0])+'%',fontsize=20,color='r')
    AAPLplot.tick_params(axis='y', which='major', labelsize=14)
    AAPLplot.tick_params(axis='x', which='major', labelsize=9)
    AAPLdailyopen = AAPLplot.plot(transformed_data["time"][0],transformed_data["open"][0],color='blue', label='Open')
    AAPLdailyhigh = AAPLplot.plot(transformed_data["time"][0],transformed_data["high"][0],'--',color='green', label='High')
    AAPLdailylow = AAPLplot.plot(transformed_data["time"][0],transformed_data["low"][0],'--',color='red', label='Low')
    AAPLdailyclose = AAPLplot.plot(transformed_data["time"][0],transformed_data["close"][0],'.', color='black', label='Close')
    AAPLplot.legend(loc=legendjson['stockloc'][0], fontsize=12)
    #Major locator helps in choosing the right numbers for x and y axis to be more presentable
    AAPLplot.xaxis.set_major_locator(MaxNLocator(integer=True))
    AAPLplot.yaxis.set_major_locator(LinearLocator(9))

    AMZNplot = stocks.add_subplot(622)
    #AMZNplot.set_xlabel('Date & Time',fontsize=14)
    AMZNplot.set_ylabel('Stock Price (USD)',fontsize=14)
    if legendjson['stockloc'][1] == 4:
        AMZNplot.set_title(stock2+'  Stock Price +'+str(transformed_data["change"][1])+'%',fontsize=20,color='g')
    else:
        AMZNplot.set_title(stock2+'  Stock Price '+str(transformed_data["change"][1])+'%',fontsize=20,color='r')    
    AMZNplot.tick_params(axis='y', which='major', labelsize=14)
    AMZNplot.tick_params(axis='x', which='major', labelsize=9)
    AMZNdailyopen = AMZNplot.plot(transformed_data["time"][1],transformed_data["open"][1],color='blue', label='Open')
    AMZNdailyhigh = AMZNplot.plot(transformed_data["time"][1],transformed_data["high"][1],'--',color='green', label='High')
    AMZNdailylow = AMZNplot.plot(transformed_data["time"][1],transformed_data["low"][1],'--',color='red', label='Low')
    AMZNdailyclose = AMZNplot.plot(transformed_data["time"][1],transformed_data["close"][1],'.', color='black', label='Close')
    AMZNplot.legend(loc=legendjson['stockloc'][1], fontsize=12)
    AMZNplot.xaxis.set_major_locator(MaxNLocator(integer=True))
    AMZNplot.yaxis.set_major_locator(LinearLocator(9))

    GOOGLplot = stocks.add_subplot(623)
    #GOOGLplot.set_xlabel('Date & Time',fontsize=14)
    GOOGLplot.set_ylabel('Stock Price (USD)',fontsize=14)
    if legendjson['stockloc'][2] == 4:
        GOOGLplot.set_title(stock3+'  Stock Price +'+str(transformed_data["change"][2])+'%',fontsize=20,color='g')
    else:
        GOOGLplot.set_title(stock3+'  Stock Price '+str(transformed_data["change"][2])+'%',fontsize=20,color='r')
    GOOGLplot.tick_params(axis='y', which='major', labelsize=14)
    GOOGLplot.tick_params(axis='x', which='major', labelsize=9)
    GOOGLdailyopen = GOOGLplot.plot(transformed_data["time"][2],transformed_data["open"][2],color='blue', label='Open')
    GOOGLdailyhigh = GOOGLplot.plot(transformed_data["time"][2],transformed_data["high"][2],'--',color='green', label='High')
    GOOGLdailylow = GOOGLplot.plot(transformed_data["time"][2],transformed_data["low"][2],'--',color='red', label='Low')
    GOOGLdailyclose = GOOGLplot.plot(transformed_data["time"][2],transformed_data["close"][2],'.', color='black', label='Close')
    GOOGLplot.legend(loc=legendjson['stockloc'][2], fontsize=12)
    GOOGLplot.xaxis.set_major_locator(MaxNLocator(integer=True))
    GOOGLplot.yaxis.set_major_locator(LinearLocator(9))

    FBplot = stocks.add_subplot(624)
    #FBplot.set_xlabel('Date & Time',fontsize=14)
    FBplot.set_ylabel('Stock Price (USD)',fontsize=14)
    if legendjson['stockloc'][3] == 4:
        FBplot.set_title(stock4+'  Stock Price +'+str(transformed_data["change"][3])+'%',fontsize=20,color='g')
    else:
        FBplot.set_title(stock4+'  Stock Price '+str(transformed_data["change"][3])+'%',fontsize=20,color='r')
    FBplot.tick_params(axis='y', which='major', labelsize=14)
    FBplot.tick_params(axis='x', which='major', labelsize=9)
    FBdailyopen = FBplot.plot(transformed_data["time"][3],transformed_data["open"][3],color='blue', label='Open')
    FBdailyhigh = FBplot.plot(transformed_data["time"][3],transformed_data["high"][3],'--',color='green', label='High')
    FBdailylow = FBplot.plot(transformed_data["time"][3],transformed_data["low"][3],'--',color='red', label='Low')
    FBdailyclose = FBplot.plot(transformed_data["time"][3],transformed_data["close"][3],'.', color='black', label='Close')
    FBplot.legend(loc=legendjson['stockloc'][3], fontsize=12)
    FBplot.xaxis.set_major_locator(MaxNLocator(integer=True))
    FBplot.yaxis.set_major_locator(LinearLocator(9))

    MSFTplot = stocks.add_subplot(625)
    #MSFTplot.set_xlabel('Date & Time',fontsize=14)
    MSFTplot.set_ylabel('Stock Price (USD)',fontsize=14)
    if legendjson['stockloc'][4] == 4:
        MSFTplot.set_title(stock5+'  Stock Price +'+str(transformed_data["change"][4])+'%',fontsize=20,color='g')
    else:
        MSFTplot.set_title(stock5+'  Stock Price '+str(transformed_data["change"][4])+'%',fontsize=20,color='r')
    MSFTplot.tick_params(axis='y', which='major', labelsize=14)
    MSFTplot.tick_params(axis='x', which='major', labelsize=9)
    MSFTdailyopen = MSFTplot.plot(transformed_data["time"][4],transformed_data["open"][4],color='blue', label='Open')
    MSFTdailyhigh = MSFTplot.plot(transformed_data["time"][4],transformed_data["high"][4],'--',color='green', label='High')
    MSFTdailylow = MSFTplot.plot(transformed_data["time"][4],transformed_data["low"][4],'--',color='red', label='Low')
    MSFTdailyclose = MSFTplot.plot(transformed_data["time"][4],transformed_data["close"][4],'.', color='black', label='Close')
    MSFTplot.legend(loc=legendjson['stockloc'][4], fontsize=12)
    MSFTplot.xaxis.set_major_locator(MaxNLocator(integer=True))
    MSFTplot.yaxis.set_major_locator(LinearLocator(9))

    NFLXplot = stocks.add_subplot(626)
    #NFLXplot.set_xlabel('Date & Time',fontsize=14)
    NFLXplot.set_ylabel('Stock Price (USD)',fontsize=14)
    if legendjson['stockloc'][5] == 4:
        NFLXplot.set_title(stock6+'  Stock Price +'+str(transformed_data["change"][5])+'%',fontsize=20,color='g')
    else:
        NFLXplot.set_title(stock6+'  Stock Price '+str(transformed_data["change"][5])+'%',fontsize=20,color='r')
    NFLXplot.tick_params(axis='y', which='major', labelsize=14)
    NFLXplot.tick_params(axis='x', which='major', labelsize=9)
    NFLXdailyopen = NFLXplot.plot(transformed_data["time"][5],transformed_data["open"][5],color='blue', label='Open')
    NFLXdailyhigh = NFLXplot.plot(transformed_data["time"][5],transformed_data["high"][5],'--',color='green', label='High')
    NFLXdailylow = NFLXplot.plot(transformed_data["time"][5],transformed_data["low"][5],'--',color='red', label='Low')
    NFLXdailyclose = NFLXplot.plot(transformed_data["time"][5],transformed_data["close"][5],'.', color='black', label='Close')
    NFLXplot.legend(loc=legendjson['stockloc'][5], fontsize=12)
    NFLXplot.xaxis.set_major_locator(MaxNLocator(integer=True))
    NFLXplot.yaxis.set_major_locator(LinearLocator(9))

    #Save as jpg, pdf with today's date
    stocknames = '_'+stock1+'-'+stock2+'-'+stock3+'-'+stock4+'-'+stock5+'-'+stock6
    jpg_name = 'DashboardDaily_'+str(transformed_data["time"][0][0][0:10])+stocknames+'.jpg'
    pdf_name = 'DashboardDaily_'+str(transformed_data["time"][0][0][0:10])+stocknames+'.pdf'
    stocks.savefig(jpg_name)
    stocks.savefig(pdf_name)

    #Show all plots
    plt.show()

    #Notification if there are no errors to inform on file names
    print('Dashboard saved as: '+jpg_name+' in local directory')
    print('Dashboard saved as: '+pdf_name+' in local directory')

    # Open PDF file
    os.startfile(pdf_name)


if __name__ == "__main__":
    main('AAPL', 'AMZN', 'GOOGL', 'FB', 'MSFT', 'NFLX', '2020-01-02')