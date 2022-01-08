import requests
import bs4
from common import config
import lxml.html as html
import re


class NewsPage:
    def __init__(self,news_site_uid,url):
        self._config = config()['news_sites'][news_site_uid]
        self._queries = self._config['queries']
        self._html = None
        self._visit(url)

    def _select(self,query_string):
        return self._html.xpath(query_string)

    def _visit(self,url):
        try:
            response = requests.get(url)

            if response.status_code == 200:
                notice = response.content.decode('utf-8')
                self._html = html.fromstring(notice)
            else:
                raise ValueError(f'Error {response.status_code}')

        except ValueError as ve:
            print(ve)


class HomePage(NewsPage):

    def __init__(self,news_site_uid,url):
        super().__init__(news_site_uid,url)

    @property
    def article_links(self):
        url_valid = re.compile(r'^https?://.+/.+$')
        link_list = []
        for link in self._select(self._queries['homepage_article_links']):
            if link and url_valid.match(link):
                link_list.append(link)
        return link_list

class Article_Page(NewsPage):
    def __init__(self, news_site_uid, url):
        super().__init__(news_site_uid, url)

    #Reutilizar codigo, metodo _select
    @property
    def body(self):
        result = self._select(self._queries['article_body'])

        return result

    @property
    def title(self):
        result = self._select(self._queries['article_title'])

        return result