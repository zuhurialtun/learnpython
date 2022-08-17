# Ignore SSL certificate errors
import csv
import sqlite3
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

conn = sqlite3.connect('dataset.sqlite') #sql veritabani baglantisi
cur = conn.cursor() # baglanti cur degiskeni ile acildi

cur.execute('''CREATE TABLE IF NOT EXISTS fastfood
    (id INTEGER PRIMARY KEY, 
    restaurant TEXT, 
    item TEXT, 
    calories INTEGER, 
    cal_fat INTEGER, 
    total_fat INTEGER, 
    sat_fat INTEGER, 
    trans_fat INTEGER, 
    cholesterol INTEGER, 
    sodium INTEGER, 
    total_carb INTEGER, 
    fiber INTEGER, 
    sugar INTEGER, 
    protein INTEGER, 
    vit_a INTEGER, 
    vit_c INTEGER, 
    calcium INTEGER, 
    salad TEXT)''')

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
            cur.execute('INSERT OR IGNORE INTO fastfood (restaurant,item,calories,cal_fat,total_fat,sat_fat,trans_fat,cholesterol,sodium,total_carb,fiber,sugar,protein,vit_a,vit_c,calcium,salad) VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', ( row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17]) )
            conn.commit()
            # for column_name in dataset_list:
                # dataset_list[column_name].append(row[x])
                # x += 1
            line_count += 1
    print(f'{line_count} satır işlendi')

# cur.execute('INSERT OR IGNORE INTO Pages (url, html, new_rank) VALUES ( ?, NULL, 1.0 )', ( starturl, ) ) # Pages tablosuna url kaydedilir

