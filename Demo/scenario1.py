import pandas as pd
import numpy as np
from pathlib import Path
import sys, os
from pathlib import Path

from Factor import *
from Utils import *

PATH = "C:\\Users\\tjmaj\\Desktop\\Barra\\Data"  # Change the path here

price = pd.read_csv(PATH + "\\price1.csv")
fundamental = pd.read_csv(PATH + "\\fundamental1.csv")

# get returns
rets = price_to_rets(price[["date", "ticker", "close"]])
# get industry dummy variable
industry_dummy = dummy(price[["industry", "ticker"]])

# Fill missing value
fill = NA(rets)
fill.drop(0.4)
rets = fill.data

# winsorize
lb, ub = 0.01, 0.99
fundamental_winsorize = winsorize(fundamental, lb=lb, ub=ub)
rets = winsorize(rets, lb=lb, ub=ub)

# zscore

# validate


if __name__ == "__main__":
    pass
