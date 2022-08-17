# Finding Numbers in a Haystack
# dosya icerisindeki sayilari bul ve topla
import re

name = input('Enter File:')
if len(name) < 1:
    name = "regex_sum_42.txt"
handle = open(name)
text = handle.read()
numbers = re.findall('[0-9]+', text)
total = 0
for number in numbers:
    total += int(number)
print(total)
