# --------
# Потанин Богдан Станиславович
# Математическая Статистика в Python
# Урок 6. Статистические оценки
# --------

import sys
import math
import pandas as pd
import numpy as np
import scipy
import matplotlib.pyplot as plt
import seaborn
from scipy.stats import t, chi2, f, norm, poisson, binom, uniform, multivariate_normal

np.set_printoptions(suppress = True)                    # уберем scientific notation

# --------
# Часть №1. Подготовительный этап
# --------

# Рассмотрим случайную величину Y со
# следующей квантильной функцией
def q_Y(p,                                              # уровень квантили
        theta = 1):                                     # параметр распределения
        return (np.sqrt(p) * theta)

# Осуществим расчет в точках
theta = 2                                               # возьмем конкретное значение параметра для распределения
q_Y(0.5, theta)                                         # найдем медиану

# Для наглядности запрограммируем, хоть далее и
# не будем использовать, и функцию плотности Y
def f_Y(t,                                              # аргумент функции плотности
        theta = 1):                                     # параметр распределения
    val = 2 * t / (theta ** 2)
    val[(t < 0) | (t >= theta)] = 0
    return (val)

# Посчитаем значения функции плотности
# с.в. Y в точках 0.3 и 0.5
f_Y(np.array([0.3, 0.5]), theta)

# Также, запрограммируем используемую далее
# функцию распределения Y
def F_Y(t,                                              # аргумент функции распределения
        theta = 1):                                     # параметр распределения
    val = (t / theta) ** 2
    val[(t < 0)] = 0
    val[(t > theta)] = 1
    return (val)

# Посчитаем значения функции распределения
# с.в. Y в точках 0.3 и 0.5
F_Y(np.array([0.3, 0.5]), theta)

# --------
# Часть №2. Оценивание параметров распределения
# --------

# Сформируем выборку из стандартного равномерного
# распределения, то есть из U~(0, 1)
np.random.seed(123)                                     # для воспроизводимости результатов, полученных с использованием
                                                        # выборок, необходима установка случайного зерна
n = 1000
u = np.random.uniform(size = n,                         # объем выборки
                      low = 0,                          # наименьшее значение
                      high = 1)                         # наибольшее значение


# Сгенерируем выборку из того же
# распределения, что и у с.в. Y
x = q_Y(u, theta)

# Рассмотрим три оценки параметра theta
theta_1 = 1.5 * np.mean(x)                              # первая оценка
theta_2 = max(x)                                        # вторая оценка
theta_3 = 5 * np.log(np.median(x))                      # третья оценка

# Рассчитаем реализации оценок при
# различных объемах выборки: от 1 до n
theta_1_vec = np.empty(n)                               # первая оценка при различных объмах выборки
theta_2_vec = np.empty(n)                               # вторая оценка при различных объмах выборки
theta_3_vec = np.empty(n)                               # третья оценка при различных объмах выборки
for i in range(0, n):                                   # считаем оценки при различных объемах выборки
    u_new = np.random.uniform(size = i + 1)
    x_new = q_Y(u_new, theta)                           # генерируем новую выборку объема (i + 1) и считаем
    theta_1_vec[i] = theta_1 = 1.5 * np.mean(x_new)     # по ней реализации оценок
    theta_2_vec[i] = max(x_new)
    theta_3_vec[i] = 5 * np.log(np.median(x_new))

# Визуализируем результат для того, чтобы
# понять, как отличаются между собой оценки,
# обладающие различными свойствами
plt.xlabel('Sample Size')
plt.ylabel('Estimate of Theta')
plt.plot(theta_1_vec, 'ro', markersize = 2,             # несмещенная и состоятельная, но менее
         color = "limegreen", label = "theta_1")        # эффективная (начиная с некоторого объема выборки), чем theta_2
plt.plot(theta_2_vec, 'ro', markersize = 2,             # смещенная и состоятельная, а также более
         color = "goldenrod", label = "theta_2")        # эффективная (начиная с некоторого объема выборки), чем theta_1
plt.plot(theta_3_vec, 'ro', markersize = 2,             # не состоятельная
         color = "darkcyan", label = "theta_3")
plt.axhline(y = theta , linestyle='-',                  # истинное значение оцениваемого
            color='cyan', label = "theta")              # параметра theta
plt.ylim(ymin = 1, ymax = 2.5)                          # обрежем часть значений, чтобы график
                                                        # смотрелся нагляднее
plt.legend()
# Обратите внимание, что:
# 1. Реализации оценки theta_1 колеблются вокруг
# истинного значения оцениваемого параметр theta,
# примерно с равной вероятностью и в равной степени
# превышая или оказываясь меньше theta, поскольку
# оценка theta_1 несмещенная.
# 2. При достаточно больших объемах выборки реализации
# оценок theta_1 и theta_2 оказываются очень близки
# к истинному значению и практически не колеблятся
# рядом с ним. Это происходит потому, что theta_1
# и theta_2 состоятельные.
# 3. Колебания реализаций theta_2 по отношению к
# истинному значению существенно слабее, чем у
# theta_1, потому что theta_2 более эффективна.
# 4. Реализации оценок theta_3 обычно далеки от
# истинного значения и не приближаются к нему
# по мере увеличения объема выборки, поскольку
# оценка theta_3 не состоятельная.
# 5. Реализации оценки theta_2 всегда меньше,
# чем theta, поскольку theta_2 смещенная.
# Примечание: графический анализ позволяет лишь сделать
#             предположения о свойствах оценок. Формальная
#             проверка соблюдения свойств требует строгого
#             математического доказательства.

# --------
# Часть №3. Распределение оценок
# --------

# Визуализируем, приблизительно,
# распределение оценки theta_2
    # Сперва получим выборку из
    # оценок, используя для
    # этого несколько независимых выборок
    # равного объема из одного и того
    # же распределения
m = 1000                                                # количество независимых выборок равного объема
                                                        # из одного и того же распределения
theta_2_vec = np.empty(m)                               # вектор, который будет содержать выборку
                                                        # из оценок theta_2
for i in range(0, m):
    x_new = q_Y(np.random.uniform(size = n), theta)
    theta_2_vec[i] = max(x_new)
theta_2_vec = np.sort(theta_2_vec)                      # для удобства отсортируем реализации оценок
    # Аналитически находим истинные функцию плотности
    # и функцию распределения оценки theta_2
F_theta_2 = F_Y(theta_2_vec, theta) ** n                # функция распределения theta_2 в точках реализаций оценок
f_theta_2 = (2 * n  / theta) * \
            ((theta_2_vec / theta) ** (2 * n))          # функция плотности theta_2 в токах реализаций оценок
    # Визуализация функции плотности оценки theta_2
plt.xlabel('x')                                         # название нижней оси графика
plt.ylabel('f(x)')                                      # название верхней оси графика
plt.plot(theta_2_vec, f_theta_2, '--', linewidth = 3,   # график теоретической функции плотности оценки theta_2
  label = "PDF", color = "limegreen")
seaborn.histplot(theta_2_vec, stat = 'density',         # гистограмма
                 color = "palevioletred",
                 label = "histogram",
                 bins = 20)
plt.legend()
    # Визуализация функции распределения оценки theta_2
plt.xlabel('x')                                         # название нижней оси графика
plt.ylabel('F(x)')                                      # название верхней оси графика
plt.plot(theta_2_vec, F_theta_2, '--', linewidth = 3,   # график теоретической функции распределеиня оценки theta_2
  label = "CDF", color = "limegreen")
seaborn.ecdfplot(theta_2_vec, stat = 'proportion',      # график выборочной функции распределения
                 color = "palevioletred",
                 label = "ECDF",
                 linewidth = 2)
plt.legend()

# --------
# Часть №4. Оценивание прочих характеристик распределения
# --------

# В качестве оценок характеристик распределения
# можно использовать как универсальные выражения,
# так и те, что учитывают специфику
# рассматриваемого распределения
    # Математическое ожидание E(Y)
2 * theta / 3                                           # истинное значение E(Y)
2 * theta_2 / 3                                         # оценка E(Y), полученная с использованием теоремы Слуцкого
np.mean(x)                                              # выборочное среднее как оценка E(Y)
    # Дисперсия Var(Y)
(theta ** 2) / 18                                       # истинное значение Var(Y)
(theta_2 ** 2) / 18                                     # оценка Var(Y), полученная с использованием теоремы Слуцкого
np.var(x)                                               # выборочная дисперсия как смещенная оценка Var(Y)
np.var(x, ddof = 1)                                     # скорректированная выборочная дисперсия
                                                        # как несмещенная оценка Var(Y)
    # Квантиль уровня 0.3
q_Y(0.3, theta)                                         # истинное значение квантили уровня 0.3 с.в. Y
q_Y(0.3, theta_2)                                       # оценка квантили уровня 0.3 с.в. Y, полученная
                                                        # при помощи теоремы Слуцкого
np.quantile(x, 0.3)                                     # выборочная квантиль уровня 0.3 как оценка квантили
                                                        # уровня 0.3 с.в. Y

# Задания
# 1. Для выборки из экспоненциального распределения с
#    параметром 'lambda = 5', ориентируясь на
#    графики реализаций оценок при различных
#    объемах выборки, предположите, какими
#    свойствами обладают следующие оценки параметра
#    lambda и какая из них является наиболее эффективной:
#    1)     np.mean(x)
#    2)     1 / np.mean(x)
#    3)     1 / (10 + np.mean(x))
#    4)     1 / (np.log(n) + np.mean(x))
#    5)     1 / (np.log(n) / n + np.mean(x))
#    6)     1 / np.median(x)
#    7)     np.log(2) / np.median(x)
# 2. Для выборки из распределения Пуассона с
#    параметром 'lambda = 2', ориентируясь на
#    графики реализаций оценок при различных
#    объемах выборки, предположите, какими
#    свойствами обладают следующие оценки параметра
#    lambda и какая из них является наиболее эффективной:
#    1)     np.mean(x)
#    2)     np.var(x)
#    3*)    Выборочная мода (если их две, берется среднее)
#    4)     np.median(x)
#    5)     np.median(x) + (1 / 3)
# 3. Для выборки из двумерного нормального распределения,
#    со стандартными нормальными маржинальными распределениями
#    и корреляцией 'rho = 0.5', ориентируясь на
#    графики реализаций оценок при различных
#    объемах выборки, предположите, какими
#    свойствами обладают следующие оценки параметра rho и
#    какая из них является наиболее эффективной:
#    1)     np.corrcoef(x, y)
#    2)     np.mean(x * y)
#    3)     0.2 * np.corrcoef(x, y) + 0.5 * np.mean(x * y)
# 4. Для экспоненциального распределения с параметром 'lambda = 5'
#    рассчитайте истинное значение и две состоятельные
#    оценки (по выборке из 1000 наблюдений) параметра lambda: с использованием
#    надлежащей выборочной характеристики и с применением теоремы Слуцкого,
#    для следующих характеристик распределения:
#    1)     Дисперсия
#    2)     Медиана
#    3)     Значение функции плотности в точке 2: только истинное значение
#           и оценка, полученная с применением теоремы Слуцкого
#    4)     Третий начальный момент
#    5)     Квантиль уровня 0.8
# 5. Для оценок, полученных в предыдущем задании:
#    1)     Осуществите графический анализ и предположите,
#           какие из них являются более эффективными.
#    2*)    Визуалирируйте оценки функции плотности и функции
#           распределения ваших оценок при помощи гистограммы и
#           выборочной функции распределения. Для этого вам понадобится
#           сгенерировать много выборок одного и того же объема из того
#           же распределения, что и у случайной величины Y и для каждой
#           из этих выборок осуществить рассчет соответствующих оценок.
#    3**)   Визуализируйте теоретические функции плотности и функции
#           распределения ваших оценок