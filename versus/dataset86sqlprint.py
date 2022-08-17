# Ignore SSL certificate errors
import csv
import sqlite3
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

conn = sqlite3.connect('dataset.sqlite') #sql veritabani baglantisi
cur = conn.cursor() # baglanti cur degiskeni ile acildi

cur.execute('''CREATE TABLE IF NOT EXISTS dataset86
    (id INTEGER PRIMARY KEY, 
    account TEXT, 
    code INTEGER, 
    country_code INTEGER, 
    product_type TEXT, 
    value INTEGER, 
    status TEXT)''')

name = "fastfood.csv"

with open(name, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Sütun isimleri: {", ".join(row)}')
            # for column_name in row:
                # dataset_list[column_name] = list()
            line_count += 1
        else:
            x = 0
            # print(row[0])
            cur.execute('INSERT OR IGNORE INTO dataset86 (account,code,country_code,product_type,value,status) VALUES ( ?, ?, ?, ?, ?, ?)', ( row[1], row[2], row[3], row[4], row[5], row[6]) )
            conn.commit()
            # for column_name in dataset_list:
                # dataset_list[column_name].append(row[x])
                # x += 1
            line_count += 1
    print(f'{line_count} satır işlendi')

# cur.execute('INSERT OR IGNORE INTO Pages (url, html, new_rank) VALUES ( ?, NULL, 1.0 )', ( starturl, ) ) # Pages tablosuna url kaydedilir

