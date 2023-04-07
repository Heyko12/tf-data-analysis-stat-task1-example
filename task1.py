import pandas as pd
import numpy as np


chat_id = 2090817777

def solution(x: np.array) -> float:
    n = len(x)
    time = 10
    errors = np.random.exponential(scale=1, size=n) - 23
    v_real = x - errors
    a = np.mean(v_real) / time
    return a
