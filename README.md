# Stock-Market-Dashboard
Creating a stock market dashboard from an external API that tracks daily performance of stocks and relative performance between stocks
<br>Latest file is <b>FINAL. Using API to build Stock Market Dashboard.ipynb</b> modified on 9 Jun 2019
<br>Earliest design of dashboard is <b>Draft_Dashboard_Structure.png</b> in Mar 2019
<br>Older versions of Juypter Notebook are named in alphabetical order (BE, BF, BF2, BF3, BF4, BF5)
<br>Older designs of dashboard are also present in the repository

## Building a dashboard for daily changing stock prices with API online
JSON file received from REST API has stock information for a particular stock<br>
1. Receives JSON data file as string and convert it to dictionary format to easily access data<br>
2. Data cleaning is done to format datetime, store them in correct order for plotting<br>
3. Stock prices and datetime are stored in Python lists for convenience of plotting<br>
4. Basic calculation done in numpy to find percentage change for display and relative stock performance graph
## Dashboard Design - Divided into two halves
![Stock Prices for June 6, 2019](https://github.com/kohjiaxuan/Stock-Market-Dashboard/blob/master/Dashboard_2019-06-06.jpg)
<br>
5. The top half has 6 small graphs to show daily movement chart of each tech stock (FAANGM)<br>
6. The bottom half has stock index movement normalized by opening stock price in order to track relative performance of each stock to others over the day
## Libraries used
7. Library used include urllib for accessing API, json to convert string into dictionary, datetime for formatting date time, numpy for calculations and matplotlib for graph plotting
## Future Plans
8. Moving all the code into a class object and allowing user to choose the stocks to plot<br>
9. Building a front end interface via a Python app or web browser (Javascript) to increase user friendliness (not run it through a notebook) and allow users to select their stocks
