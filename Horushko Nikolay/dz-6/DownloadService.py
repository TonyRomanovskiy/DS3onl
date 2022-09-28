import requests
import time
import concurrent.futures
import pandas as pd
from multiprocessing.pool import ThreadPool

# модель для отображения результата
class Result:

    def __init__(self, handled_amount, execution_time, thread_count=1) -> None:
        self.handled_amount = handled_amount
        self.execution_time = execution_time
        self.thread_count = thread_count

    def __str__(self) -> str:
        return f'urls handled: {self.handled_amount} in {self.thread_count} threads, execution time: {self.execution_time} ms'

    @staticmethod
    def to_series(result_list):
        time_threads = dict()
        for result in result_list:
            time_threads[result.execution_time] = result.thread_count
        return pd.Series(time_threads)


# супер класс для сервисов скачивания файлов содержит шаблонный метод download
# в конструкторе принимает сервис который предоставляет список ссылок
# наследники должны реализовать метод do_download_all
class DownloadServiceAbstract:

    def __init__(self, url_provider) -> None:
        self.url_provider = url_provider

    def download(self):
        start = time.time()
        urls = self.url_provider.get_urls()
        print(f'Files: {len(urls)} Downloading... ')
        self.do_download_all(urls)
        end = time.time()
        return Result(len(urls), (end - start), self.get_thread_pool())

    def do_download_all(self, urls):
        pass

    def get_thread_pool(self):
        return 1


# Реализация для последовательного скачивания файлов
class DownloadServiceSerial(DownloadServiceAbstract):

    def __init__(self, url_provider) -> None:
        super().__init__(url_provider)

    def do_download_all(self, urls):
        for url in urls:
            self.do_download(url)

    def do_download(self, url):
        requests.get(url=url)


# Реализация для скачивания файлов с помощью ThreadPool
class DownloadServiceThreadPool(DownloadServiceSerial):

    def __init__(self, url_provider, threads) -> None:
        super().__init__(url_provider)
        self.threads = threads

    def do_download_all(self, urls):
        with concurrent.futures.ThreadPoolExecutor(self.threads) as executor:
            futures = []
            for url in urls:
                futures.append(executor.submit(self.do_download, url))

    def get_thread_pool(self):
        return self.threads


# Реализация для скачивания файлов с помощью multiprocessing
class DownloadServiceMultiprocessing(DownloadServiceThreadPool):

    def __init__(self, url_provider, threads) -> None:
        super().__init__(url_provider, threads)

    def do_download_all(self, urls):
        t = ThreadPool(processes=self.threads)
        t.map(self.do_download, urls)
        t.close()
