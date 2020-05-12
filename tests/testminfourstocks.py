from os.path import dirname, abspath
import sys

# Get path of parent folder
parentpath = dirname(dirname(abspath(__file__)))
# print(parentpath)

# Add to directory defined by sys
sys.path.append(parentpath)

scriptpath = parentpath + "\\min_interval_fourstocks"
# print(scriptpath)

# Add main script to directory
sys.path.append(scriptpath)

# parentpath allows you to do absolute import below
from min_interval_fourstocks import dashboardfour
# dashboard does absolute import of retrieve, datas and legend
# scriptpath allows you to do (implicit) absolute import from dashboard.py

def newclass(stock1, stock2, stock3, stock4, time):
    return dashboardfour.main(stock1, stock2, stock3, stock4, time)

# Simple test
if __name__ == "__main__":
    dashboardfour.main('XOM', 'CVX', 'BP', 'PSX')
