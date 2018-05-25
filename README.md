# Python 爬虫
这是一个入门级的 PythonCrawler，仅供 f_zyj 个人学习爬虫入门使用，也欢迎大佬们指点。

## 目标分析
目标：
    百度百科 Python 词条相关词条网页-标题和简介

入口页：
```
    http://baike.baidu.com/view/21087.html
```

URL 格式：
> 词条页面 URL：
```
    http://baike.baidu.com/item/*
```

数据格式：
> 标题：
```
    <dd class="lemmaWgt-lemmaTitle-title"><h1> *** </h1></dd>
```
> 简介：
```
    <div class="lemma-summary"> *** </div>
```

页面编码：
```
    UTF-8
```

## 源码
### 环境及第三方库需求
```
    Python 2.7.10
    BeautifulSoup4
```

### spider_main.py
PythonCrawler 主程序，涵盖主要爬取逻辑。

### url_manager
URL 管理器，用来管理 URL，将 URL 分为新旧两部分，新的是未爬取过的 URL，旧的是已经爬取过的 URL。

### html_downloader
HTML 下载器，用来下载想要爬取的网址 HTML 源码并且留给 HTML 解析器解析。

### html_parser
HTML 解析器，用来解析下载好的页面 HTML 源码，并从中检索新的 URL 留给 URL 管理器管理、获取想要的数据信息留给 HTML 输出器输出。

###  html_outputer
HTML 输出器，用来将 HTML 解析器提取出来的信息输出成 HTML 格式。

### test
用来做一些简单的测试，例如 bs4、re 等等，可以忽略不计。

## 关于 f_zyj
Python 初学者，养猫爱好者，强迫症患者！！！

CSDN：http://blog.csdn.net/f_zyj

知乎：https://www.zhihu.com/people/f-zyj/activities

倦鸟
2018.5.25 17:15

