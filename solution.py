import pandas as pd
import numpy as np


chat_id = 1474426447 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    import scipy.stats as sts
    stat, p = sts.ttest_ind(x, y)
    alpha = 0.03
    answer = p < alpha
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    return answer # Ваш ответ, True или False
