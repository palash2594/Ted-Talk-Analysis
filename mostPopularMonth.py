from datetime import datetime
import sqlite3

conn = sqlite3.connect('tedX.sqlite')
cur = conn.cursor()

dateFreq = dict() # counts the frequency of month when ted talks happened
cur.execute('select publishdate from teddata')
row = cur.fetchall()
for item in row:
    date = datetime.fromtimestamp(int(item[0])).strftime("%B")
    dateFreq[date] = dateFreq.get(date, 0) + 1

temp = list()

for key, val in dateFreq.items():
    temp.append((val, key))

temp.sort( reverse = True)

for val, key in temp:
    print(key, val)

cur.close()
