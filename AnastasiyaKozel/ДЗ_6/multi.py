#импортируем требуемый библиотеки
import requests
from bs4 import BeautifulSoup
import time
import requests
import concurrent.futures
from threading import Thread
from multiprocessing import Pool, cpu_count


#Сохраним URL в переменную
cat_100 = 'https://bipbap.ru/jivotnie/samye-krasivye-foto-kotikov-100-foto.html'
#Отправим GET()-запрос на сайт и сохраним полученное в переменную 'page'
page = requests.get(cat_100)
#Проверим подключение
print(page.status_code)

#создадим пустой лист
list_cat = []
soup = BeautifulSoup(page.text, "html.parser")
#Если вызвать print(soup) вылезет весь html-код нашей страницы.

#Воспользуемся функцией поиска в BeautifulSoup4
for img in soup.findAll('img'):
    list_cat.append(img.get('src'))
#в list_cat есть лишние ссылки
#необходимо отфильтровать список от лишнего
list_cat_picture=[]
for img1 in list_cat:
    if 'https:' in img1:
        list_cat_picture.append(img1)
#смотрим сколько картинок
len(list_cat_picture)


from multiprocessing import Pool

def f(cat_picture):
    for cat in cat_picture:
        print(cat)
start_4 = time.time()
if __name__ == '__main__':
    with Pool(3) as p:
        print(p,f(list_cat_picture))
print("Multi time:", time.time() - start_4)  