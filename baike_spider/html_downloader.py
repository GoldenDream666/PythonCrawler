# coding=utf-8

import urllib2

# HTML 下载器
class HtmlDownloader(object):

    #   下载当前页，返回下载信息
    def download(self, url):

        if url is None:
            return None

        response = urllib2.urlopen(url)

        if response.getcode() != 200:
            return None

        return response.read()