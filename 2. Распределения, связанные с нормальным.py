# --------
# Потанин Богдан Станиславович
# Математическая Статистика в Python
# Урок 2. Распределения, связанные с нормальным
# --------

import sys
import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import t, chi2, f, norm

# --------
# Часть №1. Распределение Хи-Квадрат
# --------

# Информация: https://docs.scipy.org/doc/scipy-0.15.1/reference/generated/scipy.stats.chi2.html

# Пусть случайная величина X имеет распределение
# хи-квадрат с 5-ю степенями свободы,
# то есть X~chi2(5).
df = 5                                                # число степеней свободы (degrees of freedom)
chi2.cdf(0.7, df = df)                                # F(0.7) = P(X <= 0.7)    - функция распределения в точке 0.7
chi2.pdf(0.7, df = df)                                # f(0.7) = F'(0.7)        - функция плотности в точке 0.7
chi2.mean(df = df)                                    # E(X)                    - математическое ожидание X
chi2.var(df = df)                                     # Var(X)                  - дисперсия X
chi2.median(df = df)                                  # Median(X)               - медиана X
chi2.moment(n = 5, df = df)                           # E(X ^ 5)                - пятый (не центральный) момент X
chi2.ppf(q = 0.6, df = df)                            # q: P(X < q) = 0.6       - квантиль уровня 0.6 с.в. X
chi2.rvs(size = 1000, df = 5)                         #                         - выборка объема 1000 из X

# График функции плотности и
# функции распределения
x = np.linspace(0,                                    # точки, между которыми будет
                chi2.ppf(q = 0.999, df = df),         # строиться график
                1000)                                 # количество точек (чем больше, тем больше детализация)
f_x = chi2.pdf(x, df = df)                            # значение функции плотности в соответствующих точках
F_x = chi2.cdf(x, df = df)                            # значение функции распределения в соответствующих точках
plt.xlabel('x')                                       # название нижней оси графика
plt.ylabel('f(x)')                                    # название верхней оси графика
plt.plot(f_x, 'ro', markersize = 1)                   # график функции плотности
plt.plot(F_x, 'ro', markersize = 1)                   # график функции распределения

# Хи-Квадрат распределение с 2-мя степенями
# свободы совпадает с экспоненциальным
# распределение с математическим ожидананием 2,
# то есть с параметром lambda = 0.5.
alpha = 1.6                                           # берем произвольную точку
chi2.cdf(alpha, df = 2)                               # убеждаем что функция распределения chi2(2) в этой точке
1 - math.exp(-0.5 * alpha)                            # равняется функции распределения EXP(0.5)

# --------
# Часть №2. Распределение Стьюдента
# --------

# Информация: https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.t.html

# Пусть случайная величина X имеет распределение
# стьюдента с 5-ю степенями свободы,
# то есть X~t(5).
df = 5                                                # число степеней свободы
t.cdf(0.7, df = df)                                   # F(0.7) = P(X <= 0.7)    - функция распределения в точке 0.7
t.pdf(0.7, df = df)                                   # f(0.7) = F'(0.7)        - функция плотности в точке 0.7
t.mean(df = df)                                       # E(X)                    - математическое ожидание X
t.var(df = df)                                        # Var(X)                  - дисперсия X
t.median(df = df)                                     # Median(X)               - медиана X
t.moment(n = 5, df = df)                              # E(X ^ 5)                - пятый (не центральный) момент X
t.ppf(q = 0.6, df = df)                               # q: P(X < q) = 0.6       - квантиль уровня 0.6 с.в. X
t.rvs(size = 1000, df = 5)                            #                         - выборка объема 1000 из X

# По мере увеличения числа степеней свободы
# распредедление Стьюдента стремится к
# стандартному нормальному
alpha = 1.6                                           # рассмотрим произвольную точку
t.cdf(alpha, df = 10000)                              # убедимся, что функции распределения
norm.cdf(alpha)                                       # обоих распредедений в этой точке очень близки

# График функции плотности и
# функции распределения
x = np.linspace(t.ppf(q = 0.001, df = df),            # точки, между которыми будет
                t.ppf(q = 0.999, df = df),            # строиться график
                1000)                                 # количество точек (чем больше, тем больше детализация)
f_x = t.pdf(x, df = df)                               # значение функции плотности в соответствующих точках
F_x = t.cdf(x, df = df)                               # значение функции распределения в соответствующих точках
plt.xlabel('x')                                       # название нижней оси графика
plt.ylabel('f(x)')                                    # название верхней оси графика
plt.plot(f_x, 'ro', markersize = 1)                   # график функции плотности
plt.plot(F_x, 'ro', markersize = 1)                   # график функции распределения

# --------
# Часть №3. Распределение Фишера
# --------

# Информация: https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.f.html

# Пусть случайная величина X имеет распределение
# стьюдента с 5-ю и 10-ю степенями свободы,
# то есть X~F(5, 10).
df1 = 5                                               # число степеней свободы
df2 = 10
f.cdf(0.7, dfn = df1, dfd = df2)                      # F(0.7) = P(X <= 0.7)    - функция распределения в точке 0.7
f.pdf(0.7, dfn = df1, dfd = df2)                      # f(0.7) = F'(0.7)        - функция плотности в точке 0.7
f.mean(dfn = df1, dfd = df2)                          # E(X)                    - математическое ожидание X
f.var(dfn = df1, dfd = df2)                           # Var(X)                  - дисперсия X
f.median(dfn = df1, dfd = df2)                        # Median(X)               - медиана X
f.moment(n = 3, dfn = df1, dfd = df2)                 # E(X ^ 3)                - третий (не центральный) момент X
f.ppf(q = 0.6, dfn = df1, dfd = df2)                  # q: P(X < q) = 0.6       - квантиль уровня 0.6 с.в. X
f.rvs(size = 1000, dfn = df1, dfd = df2)              #                         - выборка объема 1000 из X

# Рассмотрим квантиль соответствующего уровня
alpha = 0.7
# Произведение соответствующих квантилей всегда
# будет равняться единице (догадайтесь почему)
f.ppf(q= 1 - alpha, dfn = df1, dfd = df2) * \
f.ppf(q = alpha, dfn = df2, dfd = df1)

# График функции плотности и
# функции распределения
x = np.linspace(f.ppf(q = 0.001,
                      dfn = df1, dfd = df2),          # точки, между которыми будет
                f.ppf(q = 0.999,                      # строиться график
                      dfn = df1, dfd = df2),
                1000)                                 # количество точек (чем больше, тем больше детализация)
f_x = f.pdf(x, dfn = df1, dfd = df2)                  # значение функции плотности в соответствующих точках
F_x = f.cdf(x, dfn = df1, dfd = df2)                  # значение функции распределения в соответствующих точках
plt.xlabel('x')                                       # название нижней оси графика
plt.ylabel('f(x)')                                    # название верхней оси графика
plt.plot(f_x, 'ro', markersize = 1)                   # график функции плотности
plt.plot(F_x, 'ro', markersize = 1)                   # график функции распределения

# Задания
# 1. Случайная величина X имеет Хи-квадрат распредедение
#    с 10-ю степенями свободы
#    Рассчитайте:
#    1)     P(X <= 1.5)
#    2)     P(X > 1.5)
#    3)     P(1.5 <= X <= 2)
#    4)     E(X), Var(X), Median(X)
#    5)     E(X ^ 3)
#    6*)    Cov(X, X ^ 2)
#    7)     Квантиль уровня 0.1
#    8**)   Повторите предыдущие пункты, не используя
#           встроенные функции, а запрограммировав
#           их самостоятельно
#    Подсказка: P(X <= x, Y >= y) = P(X <= x, -Y <= -y)
# 2. Повторите предыдущее задание предполагая, что:
#    1)     X имеет распределение Стьюдента с 10
#           степенями свободы
#    2)     X имеет распределение Фишера с 10 и 8
#           степенями свободы
