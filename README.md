# Stock-Market-Dashboard
Creating a stock market dashboard from an external API that tracks daily performance of stocks and relative performance between stocks

## Building a dashboard for daily changing stock prices with API online
JSON file received has stock information for a particular stock
Receives JSON data file as string and convert it to dictionary format to easily access data
Data cleaning is done to format datetime, store them in correct order for plotting
Stock prices and datetime are stored in Python lists for convenience
Basic calculation done in numpy to find percentage change for display and relative stock performance graph
## Dashboard is split into two halves
The top half has 6 small graphs to show daily movement chart of each tech stock (FAANGM)
The bottom half has stock index movement normalized by opening stock price in order to track relative performance of each stock to others over the day
## Libraries used
Library used include urllib for accessing API, json to convert string into dictionary, datetime for formatting date time, numpy for calculations and matplotlib for graph plotting
