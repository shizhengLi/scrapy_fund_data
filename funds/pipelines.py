# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


import pymysql.cursors


class FundsPipeline(object):
    def process_item(self, item, spider):
        # 连接数据库
        connection = pymysql.connect(host='127.0.0.1',
                                     user='root',
                                     password='123',
                                     # db='funds',
                                     db='django_mysql',

                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)

        sql = "INSERT INTO funds(code,name,unitNetWorth,day,dayOfGrowth,recent1Week,recent1Month,recent3Month,recent6Month,recent1Year,recent2Year,recent3Year,fromThisYear,fromBuild,serviceCharge,upEnoughAmount)\
                                      VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (
            item['code'], item['name'], item['unitNetWorth'], item['day'], item['dayOfGrowth'], item['recent1Week'], \
            item['recent1Month'], item['recent3Month'], item['recent6Month'], item['recent1Year'], item['recent2Year'],
            item['recent3Year'], item['fromThisYear'], item['fromBuild'], item['serviceCharge'], item['upEnoughAmount'])

        with connection.cursor() as cursor:
            cursor.execute(sql) # 执行sql

        connection.commit()  # 提交到数据库执行
        connection.close()

        return item