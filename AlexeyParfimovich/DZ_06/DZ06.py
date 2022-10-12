import os
import time
import string
import shutil
import pathlib
import requests
import multiprocessing as mp
import concurrent.futures as cf

PAGE_NUM = 100
DIR_NAME = 'files'

SITE_URL = "https://en.wikipedia.org"
PAGE_NAMES = ["wiki/" + str(i) for i in range(PAGE_NUM)]

# Получаем количество логических ЦПУ = N_ядер * N_потоков   
CPU_COUNT = os.cpu_count()

# Очистить каталог скачиваемых файлов
def dir_clean(dir_name):
    if os.path.exists(dir_name):
        try:
            shutil.rmtree(dir_name)
        except OSError as e:
            print("Dir clean error: %s : %s" % (dir_name, e.strerror)) 
    os.mkdir(dir_name)

# Получить количество скачанных файлов в каталоге
def get_file_num(dir_name):
    if os.path.exists(dir_name):
        return len(list(pathlib.Path(dir_name).iterdir()))
    return 0

# Загрузить страницу по указанному URL и сохранить в файл
def save_page_from_url(page_url, file_name, timeout=10):
    responce = requests.get(url= page_url, timeout=timeout)
    if responce.status_code == 200:
        with open(file_name, 'w', encoding="utf-8") as file:
            file.write(responce.text)
            file.close()
    return responce.status_code

# Загрузить список страниц в однопоточном режиме
def save_pages_in_single_thread(site_url, page_names, dir_name):
    for page_name in page_names:
        page_url = f"{site_url}/{page_name}"
        file_name = f"{dir_name}\{page_name.replace('/','_')}.html"
        save_page_from_url(page_url, file_name)

# Загрузить список страниц в многопоточном режиме
def save_pages_in_multi_thread(site_url, page_names, dir_name):
    global CPU_COUNT
    with cf.ThreadPoolExecutor(CPU_COUNT) as executor:
        futures = []
        for page_name in page_names:
            page_url = f"{site_url}/{page_name}"
            file_name = f"{dir_name}\{page_name.replace('/','_')}.html"
            futures.append(executor.submit(save_page_from_url, page_url=page_url, file_name=file_name))

# Загрузить список страниц в многопроцессорном режиме
def save_pages_in_multi_process(site_url, page_names, dir_name):
    global CPU_COUNT
    with mp.Pool(processes=CPU_COUNT) as pool:
        for page_name in page_names:
            page_url = f"{site_url}/{page_name}"
            file_name = f"{dir_name}\{page_name.replace('/','_')}.html"
            pool.apply_async(save_page_from_url, args=(page_url, file_name, ))
        pool.close()
        pool.join()

# Тестирование функций одно-/многопоточной загрузки и многопроцессорной загрузки страниц  
if __name__ == '__main__':

    dir_clean(DIR_NAME)
    print(f'There are {get_file_num(DIR_NAME)} files in the directory .\{DIR_NAME}\n')

    print("Running tasks in a single thread:")
    start_time = time.time()
    save_pages_in_single_thread(SITE_URL, PAGE_NAMES, DIR_NAME)
    print(f"task completed in {time.time() - start_time} s")
    print(f'There are {get_file_num(DIR_NAME)} files in the directory .\{DIR_NAME}\n')

    print("Running tasks in multiple threads (asynchronously):")
    dir_clean(DIR_NAME)
    start_time = time.time()
    save_pages_in_multi_thread(SITE_URL, PAGE_NAMES, DIR_NAME)
    print(f"task completed in {time.time() - start_time} s")
    print(f'There are {get_file_num(DIR_NAME)} files in the directory .\{DIR_NAME}\n')
    
    print("Running tasks in multiple process (separately):")
    dir_clean(DIR_NAME)
    start_time = time.time()
    save_pages_in_multi_process(SITE_URL, PAGE_NAMES, DIR_NAME)
    print(f"task completed in {time.time() - start_time} s")
    print(f'There are {get_file_num(DIR_NAME)} files in the directory .\{DIR_NAME}\n')