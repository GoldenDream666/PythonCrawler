# coding=utf-8

import re
import urlparse
from bs4 import BeautifulSoup


# HTML 解析器
class HtmlParser(object):

    # 获取页面中所有的 URL
    def _get_new_urls(self, page_url, soup):

        new_urls = set()

        # 查找页面的 URL
        links = soup.find_all('a', href=re.compile(r"/item/*"))
        # print(len(links))
        for link in links:
            new_url = link['href']
            # 将 new_url 按照 page_url 的格式拼接
            new_url_join = urlparse.urljoin(page_url, new_url)
            new_urls.add(new_url_join)

        return new_urls

    # 获取页面中想要的 DATA
    def _get_new_data(self, page_url, soup):

        res_data = {}

        # url http://baike.baidu.com/item/*
        res_data['url'] = page_url

        # 查找页面的 DATA title <dd class="lemmaWgt-lemmaTitle-title"><h1> *** </h1></dd>
        title_node = soup.find('dd', class_="lemmaWgt-lemmaTitle-title").find('h1')
        res_data['title'] = title_node.get_text()

        # 查找页面的 DATA summary <div class="lemma-summary"> *** </div>
        summary_node = soup.find('div', class_="lemma-summary")
        res_data['summary'] = summary_node.get_text()

        return res_data

    # 解析网页获取 new_urls 与 new_data
    def parse(self, page_url, html_cont):

        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)

        return new_urls, new_data