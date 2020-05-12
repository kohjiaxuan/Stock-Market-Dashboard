# Stock-Market-Dashboard
Creating a stock market dashboard from an external REST API (Alpha Vantage) - only for NYSE stocks - that allows investors to track daily performance of stocks and relative performance between stocks.
## Motivations
While there are a lot of websites and apps that show great visualisation of stocks, there are many limitations like:
<br>1. Being able to select and view different stock trends at once
<br>2. Analyse relative performance (% change) between stocks over the day
<br>3. Sending stock reports via images/pdf quickly instead of spending time to screenshot an app/saving a website many times. The current applications and terminals out there charge a hefty fee for such features.
<br>Hence, the motivation to create a dashboard from API of live data to allow investors to analyse stocks and send reports easily!
## Updates
<b>12 May 2020</b> - Code has been refactored significantly to make it more production ready (instead of being in notebooks only)
<br>Python code to run/import now has four variants:

| Folder | Main Python File | Number of stocks | Stock Price Time Interval | Stock Time Range | Delay |
| :---: | :---: | :---: | :---: | :---: | :---: |
| min_interval | dashboard.py | 6 | 5 minutes | 1.5 days | 1 min++ |
| min_interval_fourstocks | dashboardfour.py | 4 | 5 minutes | 1.5 days | Minimal delay |
| day_interval | dashboarddaily.py | 6 | 1 day | 6 months | 1 min++ |
| day_interval_fourstocks | dashboarddailyfour.py | 4 | 5 minutes | 6 months | Minimal delay |

## Building a dashboard for daily changing stock prices with API online
JSON file received from REST API has stock information for a particular stock<br>
1. Receives JSON data file as string and convert it to dictionary format to easily access data<br>
2. Data cleaning is done to format datetime, store them in correct order for plotting<br>
3. Stock prices and datetime are stored in Python lists for convenience of plotting<br>
4. Basic calculation done in numpy to find percentage change for display and relative stock performance graph
## Dashboard Design - Divided into two halves
![Stock Prices for June 6, 2019](https://github.com/kohjiaxuan/Stock-Market-Dashboard/blob/master/archive/Dashboard_2019-06-06.jpg)
<br>
5. The top half has 6 small graphs to show daily movement chart of each tech stock (FAANGM) or stock listing name of your choice<br>
6. The bottom half has stock index movement normalized by a specific starting stock price in order to track relative performance of each stock to others over the day/months. As per point 12, the starting date/time can be selected.
## Improvements in code (May 2020)
7. Tidied up repo into folders, old notebooks and images are now put in archive
8. Each folder has a main py file called dashboard.py or dashboard<b>(variantname)</b>.py to be used directly or imported by another script file (refer to Updates section for more info)
9. This allows you to plot stock market dashboards for the past 6 months (daily changes) and for the past day (5 min intervals) respectively
10. Running the Python scripts directly will give a sample jpg/pdf in the same directory
11. test scripts such as testday.py and testmin.py are in the tests folder (import test on dashboarddaily and dashboard respectively) and show how to import the script and use its "main" function
12. New feature that allows user to choose a start date (e.g. 2020-01-02) for dashboarddaily.py or start time (e.g. 09:35) for dashboard.py to do percentage change comparison. The graph will be plotted until the current/latest date/datetime
## Useful information
* To use the code, just run the main Python files (listed in Updates section) directly or import them
* Note that the dashboard py files already have some sample stock market listings inside that will execute by default, this can be changed (look for the line <b>if __name__ == "__main__":</b>)
* Importing the dashboard py files will not activate the generation of stock market dashboard, user can use the main function to generate any comparison/sets of NYSE stock listings
* Delay in the py code is due to the restriction of 5 API calls/min for the basic Alpha Vantage API, user can remove the time delay in the retrieve.py if they are using premium/paid API (remove time.sleep(60.1) in the code)
* User must put the API key in the retrieve.py of each respective folder of dashboard.py before using, under APIKEY_ALPHAVANTAGE = "PUTAPIKEYHERE"
* dashboard.py will use retrieve.py, datas.py and legend.py
* test folder with test py scripts showcase how to call the dashboard.py scripts and export the JPG/PDF in the parent folder of the script importing dashboard.py
* By default, PDF file and matplotlib plot is shown. To stop this, comment out os.startfile(pdf_name) and plt.show() respectively.
* matplotlib plot might show skewed axes/titles/plots due to problems of scaling on the open window, however Juypter Notebook and the exported jpg/pdf will not have this issue
* <b>9 June 2019</b> - Latest notebook is <b>FINAL. Using API to build Stock Market Dashboard.ipynb</b> modified on 9 Jun 2019
* Earliest design of dashboard is <b>Draft_Dashboard_Structure.png</b> in Mar 2019
* Older versions of Juypter Notebook are named in alphabetical order (BE, BF, BF2, BF3, BF4, BF5), now stored in notebooks folder
* Older designs of dashboard are also present in the repository in archive folder
## Libraries used
* Library used include urllib for accessing API, time to delay the script running for a minute so that 3x2 API calls can be made to circumvent the 5 API call limit/min, os to add the parent directory storing the dashboard scripts for absolute imports and opening PDF file, json to convert string into dictionary, datetime for formatting date time, numpy for calculations and matplotlib for graph plotting
* Refer to pip_install.txt and requirements.txt for what to pip install and all the library dependencies respectively
## Future Plans
* Building a front end interface via a Python app or web browser (Javascript) to increase user friendliness (not run it through a notebook) and allow users to select their stocks
* Using an email library that allows the images/PDF to be sent to the person's email on a hourly/daily/weekly basis
* Productionizing code with cron or Windows scheduler
* Deployment onto the cloud using Flask
