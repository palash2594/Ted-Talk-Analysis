import sqlite3
import csv

conn = sqlite3.connect('tedX.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS teddata')

cur.execute(''' CREATE TABLE IF NOT EXISTS teddata
        (description TEXT UNIQUE, duration INTEGER, tedevent TEXT,
        languages INTEGER, main_speaker TEXT, publishdate INTEGER,
        ratings TEXT, tags TEXT, title TEXT, url TEXT, views INTEGER, comments INTEGER)''')

def csv_dict_reader(file_obj):
    """
    Read a CSV file using csv.DictReader
    """
    count = 0
    reader = csv.DictReader(file_obj, delimiter=',')
    for line in reader:
        cur.execute(''' INSERT OR IGNORE INTO teddata (description, duration, tedevent, languages,
            main_speaker, publishdate, ratings, tags, title, url, views, comments) values
            (?,?,?,?,?,?,?,?,?,?,?,?)''', (line['description'], int(line['duration']), line['event'], int(line['languages']),
            line['main_speaker'], int(line['published_date']), line['ratings'], line['tags'], line['title'], line['url'],
            int(line['views']), int(line['comments'])))
    conn.commit()
with open('ted_main.csv', encoding = "utf-8") as f_obj:
    csv_dict_reader(f_obj)

cur.close()
