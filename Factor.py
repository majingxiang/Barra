"""
Factor preprocessing

"""

import numpy as np
import pandas as pd
from functools import wraps


def dummy(x: pd.DataFrame):
    """
    :param x:
    :return:
    """
    assert "industry" in x.columns and "ticker" in x.columns

    x_unique = x[["ticker", "industry"]].drop_duplicates().set_index("ticker")
    df_dummy = pd.get_dummies(x_unique)
    result = x.merge(df_dummy, on="ticker", how="left")

    return result


def price_to_rets(df, column="ticker", index="date"):
    """

    :param df: Price DataFrame
    :param column: params for pivot table
    :param index:
    :return:m
    """

    assert len(df.columns) == 3 or len(df.columns) == 2
    rets = df.pivot_table(columns=column, index=index).pct_change()
    rets = rets.droplevel(axis=1, level=0)
    rets = rets.dropna(how="all")
    mask = abs(rets).max() < 0.11
    rets = rets[[index for index, value in mask.iteritems() if value is True]]

    return rets


def winsorize(df: pd.DataFrame, lb=0.05, ub=0.95):
    """ winsorize function"""
    upper, lower = df.quantile(ub, axis=1), df.quantile(lb, axis=1)

    return df.clip(lower, upper, axis=0)


def zscore():
    return


def factor_combine():
    return


def preprocessing():
    return
