import math

# Исходные данные
mu = 178  # Среднее значение роста
sigma_squared = 25  # Дисперсия роста

# Рост человека
x = 190

# Стандартное отклонение (квадратный корень из дисперсии)
sigma = math.sqrt(sigma_squared)

# Количество сигм, на которое отклоняется значение роста от среднего
num_sigma = (x - mu) / sigma

print("Количество сигм, на которое отклоняется рост в 190 см от среднего:", num_sigma)
