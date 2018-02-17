import sqlite3

conn = sqlite3.connect('tedX.sqlite')
cur = conn.cursor()

tagsCount = dict() # contains count of each tag
allTags = list() # list of tag list

cur.execute('''select tags from teddata
                where comments > 1000
                order by comments
                ''')

row = cur.fetchall()
for item in row:
    allTags.append(item[0])

for tagList in allTags:
    internal_list = tagList.replace('[', '').replace(']', '').replace("'", '').split(', ')
    for item in internal_list:
        tagsCount[item] = tagsCount.get(item, 0) + 1

templist = list()
for k, v in tagsCount.items():
    templist.append((v,k))

templist.sort(reverse = True)

for val, key in templist[:10]:
    print(key, val)

cur.close()
