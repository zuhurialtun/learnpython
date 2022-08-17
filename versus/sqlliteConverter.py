from asyncore import close_all
import csv
import sqlite3

name = input('Enter File: ')
if len(name) < 1:
    name = "fastfood.csv"
sqllite_table_name = input('Enter Sqllite Table Name: ')
while len(sqllite_table_name) < 1:
    print('Need table name!')
    sqllite_table_name = input('Enter Sqllite Table Name: ')
dataset_column_type = dict()

with open(name, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names: {", ".join(row)}')
            for column_name in row:
                dataset_column_type[column_name] = input(column_name + ' column data type => ')
            x = 0
            # table_create_text = "''"
            table_create_text = 'CREATE TABLE IF NOT EXISTS '
            table_create_text += str(sqllite_table_name)
            table_create_text += ' ('
            for column_name in dataset_column_type:
                # print(dataset_column_type[column_name])
                if(x == 0):
                    table_create_text += 'id INTEGER PRIMARY KEY, '
                    x += 1
                    # print(table_create_text)
                elif((x+1) == len(dataset_column_type)):
                    table_create_text += (column_name + ' ' + dataset_column_type[column_name])
                    x += 1
                    # print(table_create_text)
                else:
                    table_create_text += (column_name + ' ' + dataset_column_type[column_name] + ', ')
                    x += 1
                    # print(table_create_text)
            table_create_text += ')'

            line_count += 1
            # print(table_create_text)
close_all()

conn = sqlite3.connect('dataset.sqlite')  # sql veritabani baglantisi
cur = conn.cursor()  # baglanti cur degiskeni ile acildi
cur.execute(str(table_create_text))
