
import numpy as np
from scipy import stats

#------------------Вариант с p_value--------------------------------

data = np.random.uniform(low=0,high=0.9999, size=500)

# считаем частоты. Берем например 40 интервалов, чтобы в каждом интервале было точно больше чем 5 значений
r=40
observed, _ = np.histogram(data, bins=r, range=(0, 1))

# считаем ожидаемые частоты
expected = len(data)/r

#критерий
chi2, p_value = stats.chisquare(observed)

print(f'Критерий хи квадрат: {chi2:.2f}')
print(f'p_value: {p_value:.2f}')

if p_value >= 0.05:
    print("Не отвергаем H0: генератор хороший")
else:
    print("Отвергаем H0: генератор плохой")

#---------------------Вариант с критическим значением----------------------

# Считаем частоты. Берём 40 интервалов
r = 40
observed, _ = np.histogram(data, bins=r, range=(0, 1))

# Считаем ожидаемые частоты
expected = len(data) / r

# Критерий хи-квадрат
chi2, p_value = stats.chisquare(observed)

# Критическое значение для df = r-1 = 39, alpha = 0.05
df = r - 1
alpha = 0.05
critical = stats.chi2.ppf(1 - alpha, df)

print(f"Критерий хи-квадрат: {chi2:.4f}")
print(f"Критическое значение (alpha=0.05, df={df}): {critical:.4f}")
print(f"p-value: {p_value:.4f}")

# Решение через критическое значение
if chi2 < critical:
    print("Не отвергаем H0: генератор хороший")
else:
    print("Отвергаем H0: генератор плохой")
