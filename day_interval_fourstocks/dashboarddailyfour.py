import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from matplotlib.ticker import LinearLocator
import os
# %matplotlib inline
import retrievedailyfour
import datasdailyfour
import legendfour

def main(stock1, stock2, stock3, stock4, startdate=''):
    stockdata = retrievedailyfour.stocks(stock1, stock2, stock3, stock4)
    transformed_data = datasdailyfour.transformdata(stockdata[0], stockdata[1], stockdata[2], stockdata[3], startdate)

    # Create dashboard of stocks
    # A big graph at the bottom comparing the relative performance (in %) of each stock over the day
    # Instead of using the candlestick plot, I used a continuous line plot with dotted lines signifying the higher/lower bound

    # Plan of subplot layering (1x1 one for title, 2x1 for overlaid graphs, 4x2 one for small graphs but only occupy top 4 spaces)

    # Create big figure
    stocks = plt.figure(1,figsize=(24,30))
    plt.style.use('ggplot')

    #Create big subplot for title and remove frame (frameon=False), remove tick parameters
    stocks_title = stocks.add_subplot(111, frameon=False) #remove frame but need remove ticks/axes
    stocks_title.tick_params(labelcolor='none', top=False, bottom=False, left=False, right=False)
    stocks_title.set_title('Daily Stock Prices (USD)', fontsize=28)

    # Determine where to put legend board in relative stock performance graph
    legendjson = legendfour.legendcalculation(transformed_data["daily"][0], transformed_data["daily"][1], transformed_data["daily"][2], transformed_data["daily"][3])

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

    #Get all handle/variable storing the legend in a tuple from 0-8 and also all label of the legend var in a tuple from 0-8
    #Each element n of the tuple has a pair of handle/label associated
    handlesN, labelsN = plt.gca().get_legend_handles_labels()
    order = [0,1,2,3]
    stocks_big.legend([handlesN[idx] for idx in order],[labelsN[idx] for idx in order], loc=legendjson['legendloc'], fontsize=24)
    #Possible improvement is to detect initial and final position of graphs and relocate legend loc=1,2,3,4 accordingly every day
    stocks_big.tick_params(axis='y', which='major', labelsize=22)
    stocks_big.tick_params(axis='x', which='major', labelsize=20)
    stocks_big.set_title('Relative Graph of Stock Price Index', fontsize=30)
    #Get datetime and add it to x label
    stocks_big.set_xlabel('Index starting from date: ' + transformed_data["time"][0][0],fontsize=28)
    stocks_big.set_ylabel('Stock Price Index',fontsize=28)
    stocks_big.xaxis.set_major_locator(MaxNLocator(integer=True))
    stocks_big.yaxis.set_major_locator(MaxNLocator(integer=True))

    #Horizontal line denoting the starting stock index at beginning of time
    stocks_big.axhline(y=1, color='black', linestyle='--')


    #Create matplotlib figure with subplot size 4x2 plot using fig, axes_small (axes_small is np.array)
    #Found out that it is easier to use big figure and overlay many different size of subplot (1x1 title), (2x1 big chart),
    #(4x2 small charts) into a single matplotlib figure
    #instead of using fig, axes to define fig and axes (matrix size) tgt since there is varying sizes


    #Plot the individual stock graphs for each stock from position 1 to 4 in 4x2 matrix
    #Note that positions 5-8 taken up by big graph. It is equivalent to add_subplot(212) - position 2 in 2x1 matrix

    AAPLplot = stocks.add_subplot(421)
    #AAPLplot.set_xlabel('Date & Time',fontsize=14)
    AAPLplot.set_ylabel('Stock Price (USD)',fontsize=18)
    if legendjson['stockloc'][0] == 4:
        AAPLplot.set_title(stock1+'  Stock Price +'+str(transformed_data["change"][0])+'%',fontsize=24,color='g')
    else:
        AAPLplot.set_title(stock1+'  Stock Price '+str(transformed_data["change"][0])+'%',fontsize=24,color='r')
    AAPLplot.tick_params(axis='y', which='major', labelsize=16)
    AAPLplot.tick_params(axis='x', which='major', labelsize=12)
    AAPLdailyopen = AAPLplot.plot(transformed_data["time"][0],transformed_data["open"][0],color='blue', label='Open')
    AAPLdailyhigh = AAPLplot.plot(transformed_data["time"][0],transformed_data["high"][0],'--',color='green', label='High')
    AAPLdailylow = AAPLplot.plot(transformed_data["time"][0],transformed_data["low"][0],'--',color='red', label='Low')
    AAPLdailyclose = AAPLplot.plot(transformed_data["time"][0],transformed_data["close"][0],'.', color='black', label='Close')
    AAPLplot.legend(loc=legendjson['stockloc'][0], fontsize=16)
    #Major locator helps in choosing the right numbers for x and y axis to be more presentable
    AAPLplot.xaxis.set_major_locator(MaxNLocator(integer=True))
    AAPLplot.yaxis.set_major_locator(LinearLocator(9))

    AMZNplot = stocks.add_subplot(422)
    #AMZNplot.set_xlabel('Date & Time',fontsize=14)
    AMZNplot.set_ylabel('Stock Price (USD)',fontsize=18)
    if legendjson['stockloc'][1] == 4:
        AMZNplot.set_title(stock2+'  Stock Price +'+str(transformed_data["change"][1])+'%',fontsize=24,color='g')
    else:
        AMZNplot.set_title(stock2+'  Stock Price '+str(transformed_data["change"][1])+'%',fontsize=24,color='r')    
    AMZNplot.tick_params(axis='y', which='major', labelsize=16)
    AMZNplot.tick_params(axis='x', which='major', labelsize=12)
    AMZNdailyopen = AMZNplot.plot(transformed_data["time"][1],transformed_data["open"][1],color='blue', label='Open')
    AMZNdailyhigh = AMZNplot.plot(transformed_data["time"][1],transformed_data["high"][1],'--',color='green', label='High')
    AMZNdailylow = AMZNplot.plot(transformed_data["time"][1],transformed_data["low"][1],'--',color='red', label='Low')
    AMZNdailyclose = AMZNplot.plot(transformed_data["time"][1],transformed_data["close"][1],'.', color='black', label='Close')
    AMZNplot.legend(loc=legendjson['stockloc'][1], fontsize=16)
    AMZNplot.xaxis.set_major_locator(MaxNLocator(integer=True))
    AMZNplot.yaxis.set_major_locator(LinearLocator(9))

    GOOGLplot = stocks.add_subplot(423)
    #GOOGLplot.set_xlabel('Date & Time',fontsize=14)
    GOOGLplot.set_ylabel('Stock Price (USD)',fontsize=18)
    if legendjson['stockloc'][2] == 4:
        GOOGLplot.set_title(stock3+'  Stock Price +'+str(transformed_data["change"][2])+'%',fontsize=24,color='g')
    else:
        GOOGLplot.set_title(stock3+'  Stock Price '+str(transformed_data["change"][2])+'%',fontsize=24,color='r')
    GOOGLplot.tick_params(axis='y', which='major', labelsize=16)
    GOOGLplot.tick_params(axis='x', which='major', labelsize=12)
    GOOGLdailyopen = GOOGLplot.plot(transformed_data["time"][2],transformed_data["open"][2],color='blue', label='Open')
    GOOGLdailyhigh = GOOGLplot.plot(transformed_data["time"][2],transformed_data["high"][2],'--',color='green', label='High')
    GOOGLdailylow = GOOGLplot.plot(transformed_data["time"][2],transformed_data["low"][2],'--',color='red', label='Low')
    GOOGLdailyclose = GOOGLplot.plot(transformed_data["time"][2],transformed_data["close"][2],'.', color='black', label='Close')
    GOOGLplot.legend(loc=legendjson['stockloc'][2], fontsize=16)
    GOOGLplot.xaxis.set_major_locator(MaxNLocator(integer=True))
    GOOGLplot.yaxis.set_major_locator(LinearLocator(9))

    FBplot = stocks.add_subplot(424)
    #FBplot.set_xlabel('Date & Time',fontsize=14)
    FBplot.set_ylabel('Stock Price (USD)',fontsize=18)
    if legendjson['stockloc'][3] == 4:
        FBplot.set_title(stock4+'  Stock Price +'+str(transformed_data["change"][3])+'%',fontsize=24,color='g')
    else:
        FBplot.set_title(stock4+'  Stock Price '+str(transformed_data["change"][3])+'%',fontsize=24,color='r')
    FBplot.tick_params(axis='y', which='major', labelsize=16)
    FBplot.tick_params(axis='x', which='major', labelsize=12)
    FBdailyopen = FBplot.plot(transformed_data["time"][3],transformed_data["open"][3],color='blue', label='Open')
    FBdailyhigh = FBplot.plot(transformed_data["time"][3],transformed_data["high"][3],'--',color='green', label='High')
    FBdailylow = FBplot.plot(transformed_data["time"][3],transformed_data["low"][3],'--',color='red', label='Low')
    FBdailyclose = FBplot.plot(transformed_data["time"][3],transformed_data["close"][3],'.', color='black', label='Close')
    FBplot.legend(loc=legendjson['stockloc'][3], fontsize=16)
    FBplot.xaxis.set_major_locator(MaxNLocator(integer=True))
    FBplot.yaxis.set_major_locator(LinearLocator(9))

    #Save as jpg, pdf with today's date
    stocknames = '_'+stock1+'-'+stock2+'-'+stock3+'-'+stock4
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
    main('XOM', 'CVX', 'BP', 'SNP', '2019-12-18')