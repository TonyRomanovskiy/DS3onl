# Нарисовать график функций зависимости градусов Цельсия от Фарингейта. 
# Внести случайную ошибку в формулу и построить новый график. 
# *Попробовать решить данную задачу через LinearSVR*

import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.svm import SVR
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Зависимость градусов Цельсия от градусов Фаренгейта F = C * 1.8 + 32
def Celsius2Fahrenheit(xValues):
    return xValues * 1.8 + 32

# Зависимость градусов Фаренгейта от градусов Цельсия C = (F - 32) * 5/9
def Fahrenheit2Celsius(xValues):
    return (xValues - 32)*5/9

# Зависимость градусов Фаренгейта со случайной ошибкой
def Fahrenheit2CelsiusWithRandomDev(xValues):
    yValues = []
    for x in xValues:
        yValues.append((x - 32)*5/(np.random.normal(9.0, 1.0)))
    return yValues

# Восстановленная зависимость по методу Ordinary least squares (простых наименьших квадратов)
def ValuesByOLS(xValues, yValues):

    # средние арифметические
    x_mean = np.mean(xValues)
    y_mean = np.mean(yValues)

    df = pd.DataFrame({'x': xValues, 'y': yValues})

    # ковариация х,y
    df['xycov'] = (df['x'] - x_mean) * (df['y'] - y_mean)
    # дисперсия х
    df['xvar'] = (df['x'] - x_mean)**2

    # параметры прогнозной функции
    beta = df['xycov'].sum() / df['xvar'].sum()
    alpha = y_mean - (beta * x_mean)

    # прогнозируемые значения 
    return alpha + beta * xValues


# Функция отрисовки графиков зависимостей
def DrowFunctionGraph(initialValue, finalValue, scaleUnit = 1):
    # Build and plot valid function
    x = np.arange(initialValue, finalValue, scaleUnit) 
    y = Fahrenheit2Celsius(x)
    plt.plot(x, y, c='b', label= u'Базовая функция')

    # Build and plot function with random deviation
    y_bad = Fahrenheit2CelsiusWithRandomDev(x)
    plt.scatter(x, y_bad , s=2, c='r', label= u'Функция со случайной ошибкой' )

    # Build and plot data predicted by OLS
    y_OLS_predicted = ValuesByOLS(x, y_bad)
    plt.scatter(x, y_OLS_predicted, s=2, c='y', label= u'Прогрозируемая функция по методу OLS')

    # Using sklearn
    # Prepare train and test data
    x_train, x_test, y_train, y_test = train_test_split(x.reshape(-1,1), y_bad, test_size = 0.25)
    
    #Build and plot data predicted by Linear regression
    model = LinearRegression().fit(x_train, y_train)
    y_pred = model.predict(x_test)
    plt.scatter(x_test, y_pred, s=2, c='c', label= u'Прогрозируемая функция используя sklearn.linear_model')

    #Build and plot data predicted by Linear SVR
    linear_svr=SVR(kernel='linear')
    linear_svr.fit(x_train,y_train)
    linear_svr_y_pred=linear_svr.predict(x_test)
    plt.scatter(x_test, linear_svr_y_pred, s=2, c='k', label= u'Прогрозируемая функция используя sklearn.linear_svr')

    plt.title('Графики функций зависимости градусов Цельсия от Ферингейта')
    plt.ylabel('Функция, градусы Цельсия')
    plt.xlabel('Аргумент, градусы Фарингейта') 
    plt.grid(True)
    plt.legend()

    plt.show()


DrowFunctionGraph(-200, 200, 0.1)