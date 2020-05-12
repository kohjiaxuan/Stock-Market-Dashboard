# Stock-Market-Dashboard
Creating a stock market dashboard from an external REST API (Alpha Vantage) that allows investors to track daily performance of stocks and relative performance between stocks.
## Motivations
While there are a lot of websites and apps that show great visualisation of stocks, there are many limitations like (1) being able to select and view different stock trends at once, (2) analyse relative performance (% change) between stocks over the day and (3) sending stock reports via images/pdf quickly instead of spending time to screenshot an app/saving a website many times. The current applications and terminals out there charge a hefty fee for such features. Hence, the motivation to create a dashboard from API of live data to allow investors to analyse stocks and send reports easily!
## Updates
Latest file is <b>FINAL. Using API to build Stock Market Dashboard.ipynb</b> modified on 9 Jun 2019
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
## Improvements in code (May 2020)
7. Tidied up repo into folders, old notebooks and images are now put in archive
8. Main script files to run are dashboarddaily.py in day_interval folder and dashboard.py in min_interval folder
9. This allows you to plot stock market dashboards for the past 6 months (daily changes) and for the past day (5 min intervals) respectively
10. Running the Python scripts directly will give a sample jpg/pdf in the same directory
11. testday.py and testmin.py in the tests folder are tests on dashboarddaily and dashboard respectively and show how to import the script and use its main function
12. New feature that allows user to choose a start date (e.g. 2020-01-02) for dashboarddaily.py or start time (09:35) for dashboard.py until the current/latest date/datetime to plot
## Libraries used
7. Library used include urllib for accessing API, time to delay the script running for a minute so that 3x2 API calls can be made to circumvent the 5 API call limit/min, json to convert string into dictionary, datetime for formatting date time, numpy for calculations and matplotlib for graph plotting
## Future Plans
8. Building a front end interface via a Python app or web browser (Javascript) to increase user friendliness (not run it through a notebook) and allow users to select their stocks
9. Using an email library that allows the images/PDF to be sent to the person's email on a hourly/daily/weekly basis
10. Productionizing code with cron or Windows scheduler
11. Deployment onto the cloud