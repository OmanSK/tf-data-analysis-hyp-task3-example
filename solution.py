import pandas as pd
import numpy as np
from scipy.stats import ttest_ind


chat_id = 143893840 # Ваш chat ID, не меняйте название переменной

def solution(args) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    a, *b = args
    if not b:
        b = a
    
    p_value = 0.1
    result = ttest_ind(a, b, equal_var=False)
    
    
    
    return result.pvalue < result
