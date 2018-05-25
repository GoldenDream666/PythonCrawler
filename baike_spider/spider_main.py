# coding=utf-8

import url_manager, html_downloader, html_parser, html_outputer


# 爬虫主调程序，主要逻辑
class SpiderMain(object):

    # 初始化，设置 URL 管理器、下载器、解析器、输出器
    def __init__(self):

        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):

        # 下载成功页面计数
        count = 1

        # 添加第一个 URL
        self.urls.add_new_url(root_url)

        # URL 管理器中存在 URL 时处理
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()

                print("craw %d : %s" % (count, new_url))

                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)

                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)

                if count == 20:
                    break

                count = count + 1

            except:
                print("craw failed")

        self.outputer.output_html()


if __name__ == "__main__":
    # 设置入口页 URL
    root_url = "http://baike.baidu.com/view/21087.htm"

    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
