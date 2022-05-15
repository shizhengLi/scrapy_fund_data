import pymysql  # 连接数据库
import pandas as pd


def connect_mysql(host, username, password, port, database):
    conn = pymysql.connect(host=host, user=username, passwd=password, port=port, db=database, charset='utf8')
    cur = conn.cursor()  # 生成游标对象
    sql = "select * from funds; "  # SQL语句
    cur.execute(sql)  # 执行SQL语句
    data = cur.fetchall()  # 通过fetchall方法获得数据
    cols = cur.description
    col = []
    for i in cols:
        col.append(i[0])
    zq_frame = list(map(list, data))
    zq_frame = pd.DataFrame(zq_frame, columns=col)
    return zq_frame


funds_zq = connect_mysql('127.0.0.1', 'root', '123', 3306, 'django_mysql')


# 这里策略是按照近一周、一月、半年等等进行设置，可自行调整。本人在此只是简单的进行了一个保守的筛选。
def strategy(frame):
    frame = frame[(frame['dayOfGrowth'] > 0) & (frame['dayOfGrowth'] < 0.25)]
    # frame = frame[(frame['recent1Month'] > 0.7) & (frame['recent1Month'] < 1.5)]
    # frame = frame[(frame['recent1Week'] > 0.1) & (frame['recent1Week'] < 0.5)]
    # frame = frame[(frame['recent1Year'] > 6) & (frame['recent1Year'] < 15)]
    # frame = frame[(frame['recent2Year'] > 12) & (frame['recent2Year'] < 30)]
    # frame = frame[(frame['recent3Month'] > 2) & (frame['recent3Month'] < 4)]
    # frame = frame[(frame['recent6Month'] > 3.5) & (frame['recent6Month'] < 7)]
    # frame = frame[frame['serviceCharge'] < 0.1]
    return frame


result = strategy(funds_zq)
print(result)
