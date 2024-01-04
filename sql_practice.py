import pymysql
import pymysql.cursors
from pprint import pprint as print

connection = pymysql.connect(
    database = 'world',
    user = 'cvasquez',
    password = '242590909',
    host = '10.100.33.60',
    cursorclass = pymysql.cursors.DictCursor
)

cursor = connection.cursor()

cursor.execute("SELECT `Name`, `HeadOfState` FROM `country`")

results = cursor.fetchall()

print(results[0]['HeadOfState'])

for hos in results:
    print(hos['HeadOfState'])