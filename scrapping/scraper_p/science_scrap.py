import argparse
import requests
import logging
from common import config
from yaml import parser
from requests.models import Response
import lxml.html as html
import HomePage as news
import re


is_well_formed_link = re.compile(r'^https?://.+/.+$')
is_root_path = re.compile(r'^/.+$')


def _news_scraper(site_name):
    host_l = config()['news_page'][site_name]['url']
    host_s = config()['news_page'][site_name]['url_section']
    print('Beginning scraper for {}'.format(host_s))

    sectionpage = news.SectionPage(site_name,host_s)
    articles = []

    for link in sectionpage.article_links:
        
        articles.append(_build_link(host_l,link))
    
    print(articles)

def _fetch_section(site_name,host_s,link):

    section = news.SectionPage(site_name,_build_link(host_s,link))
    
    return section.article_links


def _build_link(host,link):
    if is_well_formed_link.match(link):
        return link
    elif is_root_path.match(link):
        return '{}{}'.format(host,link)
    else:
        return '{host}/{uri}'.format(host=host,uri=link)
    

def run():

    site_name = 'laopinion'
    _news_scraper(site_name)

if __name__ == '__main__':
    run()