import requests
from bs4 import BeautifulSoup


class UrlProvider:

    def get_urls(self):
        pass


class UrlProviderFile(UrlProvider):

    def __init__(self, path) -> None:
        self.path = path

    def get_urls(self):
        file1 = open(self.path, 'r')
        return file1.readlines()


class UrlProviderHtmlParser(UrlProvider):

    def __init__(self, url) -> None:
        self.url = url

    def get_urls(self):
        urls = []
        response = requests.get(self.url)
        print(response.text)
        soup = BeautifulSoup(response.text, features="html.parser")
        for img in soup.findAll('img'):
            urls.append(img.get('src'))
        return urls
