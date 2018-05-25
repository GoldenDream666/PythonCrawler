#Python 爬虫
这是一个简易的 Python Spider，仅供个人学习爬虫入门使用。

##目标分析
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
