import pymysql
from datetime import datetime

conn = pymysql.connect(host = "localhost", user = 'root', password = 'root', db = 'farma', charset = 'utf8mb4', cursorclass = pymysql.cursors.DictCursor)

try:
    with conn.cursor() as cursor:
        sql = "INSERT INTO `data` (`area`, `temperature`, `humidity`, `pH`, `daylight`, `overflow`, `proximity`, `time`) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"
        v = ('salata', 24.5, 13.7, 5.5, True, False, False, datetime.now().time().replace(microsecond = 0))
        cursor.execute(sql, v)
        conn.commit()
except e:
    print(e)

finally:
    conn.close()
