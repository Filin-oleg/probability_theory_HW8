# Задача 3. Известно, что рост футболистов в сборной распределен нормально с дисперсией
# генеральной совокупности, равной 25 кв.см. Объем выборки равен 27, среднее
# выборочное составляет 174.2. Найдите доверительный интервал для математического
# ожидания с надежностью 0.95.


import numpy


M = 174.2
n = 27
std = numpy.sqrt(25)
Z = 1.96

L = numpy.round(M - Z * std / numpy.sqrt(n), 2)
U = numpy.round(M + Z * std / numpy.sqrt(n), 2)

print(f'Доверительный интервал [ {L} ; {U} ]')
