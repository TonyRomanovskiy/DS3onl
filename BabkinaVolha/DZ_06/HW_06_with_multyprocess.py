import time
import requests
from bs4 import BeautifulSoup
import os
import shutil

list_url = ["https://www.onliner.by/"]
images = []
for url in list_url:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, features="html.parser")
    for img in soup.findAll('img'):
        images.append(img.get('src'))

cleaned_img = []
for i in range(len(images)):
    if images[i]==None or images[i].startswith('//'):
        continue
    elif images[i].endswith('jpg'):
        cleaned_img.append(images[i])
len(cleaned_img)

len(cleaned_img)#количество скачанных изображений

from multiprocessing import Pool, cpu_count

try: 
    os.mkdir('MultyProcess')
except FileExistsError:
    shutil.rmtree ('MultyProcess')
    os.mkdir('MultyProcess')

def img_downl_mult(url):
    file_path='MultyProcess\\image' + str(cleaned_img.index(url)) + '.jpg'
    img=requests.get(url)
    open(file_path,"wb").write(img.content)

if __name__ == '__main__':
    pool = Pool(15)
    start = time.time()
    results = pool.map(img_downl_mult, cleaned_img)
    pool.close()
    pool.join()
    end = time.time()
    print('Time taken in seconds -', end - start)
