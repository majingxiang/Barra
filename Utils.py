from functools import wraps
import time
from loguru import logger


class MatrixError(Exception):
    pass


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


def fill_na():
    return


def is_psd():
    """is positive semi-definite"""

    return


def is_singular(x):
    m, n = x.shape[0], x.shape[1]
    if m > n:
        pass
    else:
        raise MatrixError("More parameters than observations")

    return


def validate():
    return


def mp():
    """
    Multiprocessing decorator

    Sometimes, some functions like Newey West takes a long time which needs speeding up

    """

    def f():
        return

    return
