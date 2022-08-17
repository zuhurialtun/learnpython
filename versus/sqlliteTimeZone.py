import sqlite3

conn = sqlite3.connect('dataset.sqlite')  # sql veritabani baglantisi
cur = conn.cursor()  # baglanti cur degiskeni ile acildi

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

cur.execute('SELECT MAX(calories) as maxcalories, MIN(calories) as mincalories FROM fastfood LIMIT 1')
row = cur.fetchone()
print('Max => ' + str(row[0]))
print('Min => ' + str(row[1]))