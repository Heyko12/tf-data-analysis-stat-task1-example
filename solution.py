import pandas as pd
import numpy as np


chat_id = 1012233839

def solution(x: np.array) -> float:
    n = len(x)
    time = 10
    errors = np.random.exponential(scale=1, size=n) - 39
    v_real = x - errors
    a = np.mean(v_real) / time
    return a
