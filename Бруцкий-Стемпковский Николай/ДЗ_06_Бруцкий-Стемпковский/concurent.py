"""
27092022
Бруцкий-Стемпковский

v. 02

GIL. Исследование мультипоточности и многопроцессорности.
Thread download
"""
import re
import os
import time
import requests
import shutil
import concurrent.futures

def saving_images(link):

    global path

    file_name = link.split("/")[-1]
    response = requests.get(url=link, timeout=10)

    if response.status_code == 200:
        open(path + file_name, "wb").write(response.content)

start = time.time()

file_obj = open("html.txt")
code = file_obj.readlines()
file_obj.close()

valid_string = re.compile(r"/thumb/(\S*?)jpg")

list_of_links = []
for string_ in code:
    ans = valid_string.findall(string_)
    if len(ans) == 1:
        list_of_links.append("https://ardom.by/thumb/" + ans[0] + "jpg")

if os.path.isdir("folder_for_images"):
    shutil.rmtree(os.getcwd() + "\\folder_for_images")
if not os.path.isdir("folder_for_images"):
    os.mkdir("folder_for_images")

path = os.getcwd() + "\\folder_for_images\\"

with concurrent.futures.ThreadPoolExecutor(8) as executor:
    executor.map(saving_images, list_of_links)

end = time.time()
print("Время при одиночной загрузке " + str(round(end - start, 3)) + " c")