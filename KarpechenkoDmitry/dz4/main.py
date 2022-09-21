''' Karpechenko Dmitry, DZ4, v.0.1
Домашнее задание
С использованием библиотек Numpy и Pandas написать программу реализующую:

Загрузку текстового файла из корневого каталога объемом не менее 20000 символов включая пробелы и все символы.
Подсчет частоты встречаемости слов в загруженном файле (критерий схожести слов выбрать самостоятельно).
Подсчет длин предложений и их количества.
Ввод полученных данных в объект DataFrame и Series, а также отображение полученных результатов в виде таблицы "объекты - признаки".
Построение гистограммы частоты встречаемости слов.

'''



import array
import codecs
import re
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

#Отрыкрываем файл для чтения
file_obj = open('1.txt', 'r', encoding="UTF8")
#Объявляем строковую переменную, в которую будем записывать текст
s=''
#Проходим по тексту. Переводим регистр на строчный и удаляем всю пунктуацию, кроме точек
for line in file_obj:
    s+=line.strip().lower().replace(',','').replace('—',' ').replace(':','').replace(';','')+'\n' #записываем строку строчными буквами, удаляем запятые
s = re.sub(r"\d+", "", s, flags=re.UNICODE) #даляем числа
s=s.replace('  ','').replace('   ','').replace('[] ','').replace(' (','').replace(') ',' ')
s=s.replace('?','.').replace('!','.').replace('-',' ').replace('.','').replace('\n','')
s=s.replace('\n','')

#Разделяем текст на слова
s1=s.split()

#Проходим по тексту и удаляем слова длина которых меньше 3 (исключаем предлоги, союзы и т.п)
i=0
while i<len(s1):
    if len(s1[i])<=4:
        s1.pop(i)
    i+=1

words=pd.Series(s1)

freq=pd.Series.value_counts(np.array(s1))
temp_df=pd.DataFrame({'Freq': freq})
data=temp_df.sort_values(by="Freq",ascending=False)
data=data.head(20)
data.hist(bins=20)
plt.show()
print(data)
#print(s1)