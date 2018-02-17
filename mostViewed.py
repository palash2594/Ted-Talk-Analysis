import sqlite3
import ast

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

conn = sqlite3.connect('tedX.sqlite')
cur = conn.cursor()

tagsCount = dict() # contains count of each tag
allTags = list() # list of tag list
allRatings = list() # list of list of dictionaries
mostViewedTopics = dict()

cur.execute('''select tags from teddata
                where views > 10000000
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

print('Common topics of most viewed: \n')
for val, key in templist[:10]:
    print(key, val)

cur.execute('''select ratings from teddata
                where views > 10000000
                ''')

row = cur.fetchall()
for item in row:
    allRatings.append(ast.literal_eval(item[0])) # ast.literal_eval converts string to Dict or List depending on the structure

print('\nNumber of most viewed videos (views > 1 Million) =',len(allRatings), '\n')

temp = list()

for ratingList in allRatings:
    for ratingDict in ratingList:
        temp.append((ratingDict['count'], ratingDict['name']))
    temp.sort(reverse = True)
    for count, name in temp[:5]:
        mostViewedTopics[name] = mostViewedTopics.get(name, 0) + 1
    temp.clear()

templist = list()
for k, v in mostViewedTopics.items():
    templist.append((v,k))

templist.sort(reverse = True)

print('Similarities between most viewed content: \n')
for val, key in templist[:10]:
    print(key, val)

cur.close()
