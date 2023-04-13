import pandas as pd
import numpy as np
from statsmodels.stats.weightstats import ztest as z_test


chat_id = 143893840 # Ваш chat ID, не меняйте название переменной

def solution(*args) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    a, *b = args
    if not b:
        b = a
    
    p_value = 0.1
    result = z_test(a, b)
    
    
    
    return result[-1] < result
