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

rets = price.pivot_table(columns=["ticker"], index="date").pct_change()
rets = rets.droplevel(axis=1, level=0)
rets = rets.dropna(how="all")

# refine the equity universe: remove equity with

# get industry dummy variable

# zscore

# validate




if __name__ == "__main__":
    pass
