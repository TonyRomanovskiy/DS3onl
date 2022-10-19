import requests
import time
import concurrent.futures
from threading import Thread
from multiprocessing import Pool, cpu_count
from bs4 import BeautifulSoup


def get_images_list():
    list_url = ["https://unsplash.com/images/events"]
    images = []
    for url in list_url:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, features="html.parser")
        for img in soup.findAll('img'):
            img_src = img.get('src')
            if "unsplash" in img_src:
                images.append(img_src)

    return images


def request_image(image):
    response = requests.get(image)
    print(f"{image} - STATUS {response.status_code}")


def measure_execution(func, label):
    start = time.time()
    func()
    end = time.time()
    print(f"{label} заняло {end - start}ms")


def sequential_method():
    for image in images:
        request_image(image)


def threadpool_method():
    with concurrent.futures.ThreadPoolExecutor(12) as executor:
        futures = []
        for image in images:
            futures.append(executor.submit(request_image, image))
        for future in concurrent.futures.as_completed(futures):
            print(future.result())


def request_images(from_ind, count):
    for i in range(from_ind, from_ind + count):
        request_image(images[i])


def threading_method():
    thread_count = 12
    count = len(images) // thread_count
    threads = [Thread(target=request_images, args=(i * count, count)) for i in range(thread_count)]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()


def multiprocessing_method():
    process_count = cpu_count() * 2
    count = len(images) // process_count

    pool = Pool(processes=process_count)

    rs = []
    for i in range(process_count):
        rs.append(pool.apply_async(request_images, [i * count, count]))

    pool.close()
    pool.join()


if __name__ == '__main__':
    images = get_images_list()

    measure_execution(sequential_method, "Последовательное выполнение")
    measure_execution(threading_method, "Многопоточное выполнение")
    measure_execution(threadpool_method, "Многопоточное(пул потоков) выполнение")
    measure_execution(multiprocessing_method, "Многопроцессовое выполнение")

