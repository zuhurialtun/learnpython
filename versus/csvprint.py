import csv

name = input('Enter File:')
if len(name) < 1:
    name = "fastfood.csv"
dataset_list = dict()

row_limit = int(input('Enter Row Limit:'))

with open(name, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Sütun isimleri: {", ".join(row)}')
            for column_name in row:
                dataset_list[column_name] = list()
            line_count += 1
        else:
            x = 0
            for column_name in dataset_list:
                dataset_list[column_name].append(row[x])
                x += 1
            line_count += 1
    column_name = input('Enter Column Name: ')
    if(len(column_name) > 0):
        max_item = None
        min_item = None
        skip_item_count = 0
        for item in dataset_list[column_name]:
            if(max_item is None or min_item is None):
                max_item = float(item)
                min_item = float(item)
            try:
                if(max_item < float(item)): max_item = float(item)
                if(min_item > float(item)): min_item = float(item)
            except:
                skip_item_count += 1
        print('Selected column => ',column_name)
        print('Max => ',max_item)
        print('Min => ',min_item)
        print('Value is not number/ Count => ',skip_item_count)
        # print(dataset_list[column_name])
    else:
        if row_limit > 1:
            for row in dataset_list.items():
                if row_limit > 1:
                    print(row)
                    row_limit -= 1
                else:
                    break
        else:
            print(dataset_list.items()) # bicimlendirme ekle
    print(f'{line_count} satır işlendi')