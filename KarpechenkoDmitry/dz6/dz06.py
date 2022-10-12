#Карпеченко Дмитрий, dz06, v.0.1, 28.09.2022
import requests
import time
import threading
from bs4 import BeautifulSoup
from multiprocessing import Pool

#Функция для выкачки изображений из сайта
def dowload_img():
    list_url = ["https://klike.net/844-nyashnye-kotiki-milye-kartinki-30-foto.html"]
    images = []

    for url in list_url:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, features="html.parser")
        for img in soup.findAll('img'):
            images.append(img.get('src'))
    print(len(images))
#Выполняем нашу функцию обычным способом (последовательно)
start=time.time()
dowload_img()
end=time.time()
print('Время выполнения последовательного кода: ', end-start)
#Выполняем нашу функцию с помощью 2 потоков
def Thred_ex():
    start = time.time()
    if __name__=='__main__':
        t1=threading.Thread(target=dowload_img())
        t2=threading.Thread(target=dowload_img())
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        end=time.time()
        print('Время выполнения при Threads: ', end-start)

#Выполняем нашу функцию с помощью процессов
def proc_ex():
    start = time.time()
    if __name__=='__main__':
        pool=Pool(processes=1)
        r1=pool.apply_async(dowload_img())
        pool.close()
        pool.join()
        end=time.time()
    print('Время выполнения при multiprocessing: ', end-start)

Thred_ex()
if __name__ == '__main__':
    proc_ex()

# Выводы: т.к. не понял как в данной задаче разделить задачу на несколько процессов, сделал на одном:)
# время выполнения последовательным способом и через процессы практически одинаковы, но через процессы выполнение происходит быстрее.
# Потоки почему то значительно уступают двум другим способам. Причем при увеличении количества потоков и увеличивается время выполнение.\
# Смею предположить, что я реализовал все неправильно :)
# P.S. не судите строго