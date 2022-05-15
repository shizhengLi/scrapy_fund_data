# Scrapy Fund data into MySQL



This repo contains a python scrapy project.

Crawl fund data from https://fund.eastmoney.com/, then score them in MySQL database.



爬取的数据如下

![image-20220515121133223](https://raw.githubusercontent.com/shizhengLi/image_bed_02/main/img/image-20220515121133223.png)





同时进行基金选取

```bash
        code         day  ...  unitNetWorth  upEnoughAmount
2     005513  2022-05-13  ...        1.4533             10元
3     005514  2022-05-13  ...        1.4549             10元
7     003073  2022-05-13  ...        1.3126             10元
8     002644  2022-05-13  ...        1.1740             10元
14    290003  2022-05-13  ...        1.0524             10元
...      ...         ...  ...           ...             ...
1394  005892  2022-05-13  ...        1.0642             10元
1396  005893  2022-05-13  ...        1.0146             10元
1398  003384  2022-05-13  ...        0.9096             10元
1401  003382  2022-05-13  ...        0.8907             10元
1402  003383  2022-05-13  ...        0.8768             10元

[1049 rows x 16 columns]

Process finished with exit code 0

```



## Structure



```bash
├── README.md
├── funds
│   ├── __init__.py
│   ├── items.py
│   ├── middlewares.py
│   ├── pipelines.py
│   ├── settings.py
│   └── spiders  # 爬虫程序
│       ├── __init__.py
│       ├── fund.py
│       └── strategy.py  # 筛选策略
├── scrapy.cfg
└── scrapy_start.py  # 运行爬虫
```





## Run

打开数据库

```
net start mysql
```



运行爬虫

```bash
python scrapy_start.py
```

