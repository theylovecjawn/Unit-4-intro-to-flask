import pymysql
import pymysql.cursors
from pprint import pprint as print
conn = pymysql.connect(host='10.100.33.60',
                             user='cjohn',
                             password='224257683',
                             database='world',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

cursor = conn.cursor()

cursor.execute("SELECT `Name`, `Population` from `country`")

results = cursor.fetchall()

print(results)

for x in results:
    print(x['Population'])