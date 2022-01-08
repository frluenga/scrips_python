import requests
from requests.models import Response
import requests
import bs4
import lxml.html as html
from common import config


class NewsPage():
    def __init__(self,site_name,url):
        self._config = config()['news_page'][site_name]
        self._queries = self._config['queries']
        self._html = None
        self._visit(url)
    
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

    def _select(self,query):
        return self._html.xpath(query)

class HomePage(NewsPage):
    def __init__(self, site_name, url):
        super().__init__(site_name, url)

    @property
    def section_links(self):
        link_list = []
        for link in self._select(self._queries['section_links']):
            link_list.append(link)
        link_list_f = []
        i = 0
        for link in link_list:
            
            if i < len(link_list)-1:
                if link_list[i] == link_list[i+1]:
                    link_list_f.append(link) 
                    i += 1
                else:
                    i += 1
                    
        return link_list_f


class SectionPage(NewsPage):
    def __init__(self, site_name, url):
        super().__init__(site_name, url)
    
    @property
    def article_links(self):
        link_list = []
        for link in self._select(self._queries['article_links']):
            link_list.append(link)
        return link_list
    
