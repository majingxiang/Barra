from functools import wraps
import time
from loguru import logger
from prettytable import PrettyTable


class MatrixError(Exception):
    pass


def format_for_print(df):
    """transform Data Frame to pretty table"""
    table = PrettyTable([''] + list(df.columns))
    for row in df.itertuples():
        table.add_row(row)
    return table


def timeit(f):
    """Compute time for functions"""

    @wraps(f)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = f(*args, **kwargs)
        end = time.time()
        logger.info("{} run in {} seconds".format(f.__name__, end - start))
        return result

    return wrapper


def is_psd():
    """Is positive semi-definite"""

    return


def is_singular(x):
    m, n = x.shape[0], x.shape[1]
    if m > n:
        pass
    else:
        raise MatrixError("More parameters than observations")

    return


def mp():
    """
    Multiprocessing decorator

    Sometimes, some functions like Newey West takes a long time which needs speeding up

    """

    def f():
        return

    return
