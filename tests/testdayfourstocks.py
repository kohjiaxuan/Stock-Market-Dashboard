from os.path import dirname, abspath
import sys

# Get path of parent folder
parentpath = dirname(dirname(abspath(__file__)))
# print(parentpath)

# Add to directory defined by sys
sys.path.append(parentpath)

scriptpath = parentpath + "\\day_interval_fourstocks"
# print(scriptpath)

# Add main script to directory
sys.path.append(scriptpath)

# parentpath allows you to do absolute import below
from day_interval_fourstocks import dashboarddailyfour
# dashboarddaily does absolute import of retrievedaily, datasdaily and legend
# scriptpath allows you to do (implicit) absolute import from dashboarddaily.py

def newclass(stock1, stock2, stock3, stock4, date):
    return dashboarddailyfour.main(stock1, stock2, stock3, stock4)

# Simple test
if __name__ == "__main__":
    dashboarddailyfour.main('MCD','YUM','CMG','QSR')
