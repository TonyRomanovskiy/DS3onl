import time
import requests
from bs4 import BeautifulSoup
from multiprocessing import Pool, cpu_count


images = []
def get_images_list(): #получаем список с ссылками на изображения
    list_url = ["https://unsplash.com/t/architecture"] #ресурс с множеством изображений
    for url in list_url:
        response = requests.get(url) #GET()-запрос на сайт и сохраним полученное в переменную 'response'; 200 или 404
        soup = BeautifulSoup(response.text, features="html.parser") #перевод ссылок в html формат
        for img in soup.findAll('img'): #поиск изображений
            img_src = img.get('src')
            if "images.unsplash.com/photo" in img_src: #фильтр лишних изображений
                images.append(img_src)
    return images

get_images_list()


def get_status(image): #функция получения статуса изображения для передачи в метод
    response = requests.get(image,  verify=False)
    return image

def pool_handler():
    start = time.time()
    p = Pool(2)
    print(p.map(get_status, images))
    end = time.time()
    print(end - start)


if __name__ == '__main__':
    pool_handler()
