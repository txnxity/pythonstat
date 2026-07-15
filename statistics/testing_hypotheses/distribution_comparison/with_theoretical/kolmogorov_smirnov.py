
import pandas as pd
from scipy import stats
import numpy as np

#-------------------Вариант с p_value-------------------

data = np.random.uniform(low=0,high=1,size=300)

statistics, p_value = stats.kstest(data, 'uniform')

print(f'Статистика теста: {statistics:.2f}')
print(f'p значение {p_value:.2f}')

if p_value < 0.05:
    print('Отвергаем гипотезу о равномерности')
else:
    print('Нет оснований отвергать гипотезу о равномерности')

# -----------------Вариант с критичесским значением--------------

numbers = np.random.uniform(0, 1, 1000)
n = len(numbers)

statistic, _ = stats.kstest(numbers, 'uniform')

alpha = 0.05
critical_value = 1.36 / np.sqrt(n)

print(f"Статистика D = {statistic:.4f}")
print(f"Критическое значение D_крит = {critical_value:.4f}")

if statistic > critical_value:
    print("Отвергаем H0: распределение НЕ равномерное")
else:
    print("Не отвергаем H0: распределение равномерное")
