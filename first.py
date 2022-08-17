# x = int(98.6)
# print(x)
# -----------------------------------------------------------------------------------------------------------------
# name = input('Who are you?')
# print('Welcome', name)
# -----------------------------------------------------------------------------------------------------------------
# hrs = input("Enter Hours:")
# h = float(hrs)
# price = input("Enter Price:")
# p = float(price)
# totalPrice = 0
# if h <= 40:
# 	totalPrice = h * p
# elif h > 40:
# 	totalPrice = (40 * p) + ((h-40)*(p*1.5))
# print(totalPrice)
# -----------------------------------------------------------------------------------------------------------------
# def greet(lang):
#     if lang == 'es':
#         return 'Hola'
#     elif lang == 'fr':
#         return 'Bonjour'
#     else:
#         return 'Hello'

# print(greet('fr'),'Michael')
# -----------------------------------------------------------------------------------------------------------------
# largest = None
# smallest = None
# while True:
#     num = input("Enter a number: ")
#     if num == "done":
#         break
#     try:
#         number = int(num)
#     except:
#         print('Invalid input')
#         continue

#     if largest == None:
#         largest = number
#         smallest = number
#     if number > largest:
#         largest = number
#     if number < smallest:
#         smallest = number

# print("Maximum is", largest)
# print("Minimum is", smallest)
# -----------------------------------------------------------------------------------------------------------------
# data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
# pos = data.find('.')
# print(data[pos:pos+3])
# -----------------------------------------------------------------------------------------------------------------
# text = "X-DSPAM-Confidence:    0.8475"
# number = text.find("0")
# print(text[number:len(text)])
# -----------------------------------------------------------------------------------------------------------------
# fhand = open('words.txt')
# inp = fhand.read()
# print(inp)
# -----------------------------------------------------------------------------------------------------------------
# Use the file name mbox-short.txt as the file name
# lineCount = 0
# total = 0
# fname = input("Enter file name: ")
# fh = open(fname)
# for line in fh:
#     if line.startswith("X-DSPAM-Confidence:"):
#         lineCount += 1
#         total += float(line[(line.find(':')+1):].strip())
# print('Average spam confidence:',total/lineCount)
# -----------------------------------------------------------------------------------------------------------------
# friends = [ 'Joseph', 'Glenn', 'Sally' ]
# friends.sort()
# print(friends[0])
# -----------------------------------------------------------------------------------------------------------------
# fname = input("Enter file name: ")
# fh = open(fname)
# lst = list()
# for line in fh:
#     for word in line.rstrip().split():
#         if(word not in lst):
#             lst.append(word)
# lst.sort()
# print(lst)
# -----------------------------------------------------------------------------------------------------------------
# fname = input("Enter file name: ")
# if len(fname) < 1:
#     fname = "mbox-short.txt"
# count = 0
# fh = open(fname)
# for line in fh:
#     if('From' in line and '2008' in line):
#         print(line.split(' ')[1])
#         count += 1
# print("There were", count, "lines in the file with From as the first word")
# -----------------------------------------------------------------------------------------------------------------
# fh = open('mbox-short.txt')
# count = 0
# for line in fh:
#     line = line.rstrip()
#     wds = line.split()
#     if(len(wds) < 3 or wds[0] != 'From'):
#         continue
#     print(wds[1])
#     count += 1
# print("There were", count, "lines in the file with From as the first word")
# -----------------------------------------------------------------------------------------------------------------
# stuff = dict()
# print(stuff.get('candy',-1))
# -----------------------------------------------------------------------------------------------------------------
# x = dict()
# x['candy'] = 1
# for y in x :
#     print(y)
# -----------------------------------------------------------------------------------------------------------------
# name = input('Enter File:')
# if len(name) < 1:
#     name = "mbox-short.txt"
# handle  = open(name)

# counts = dict()
# for line in handle:
#     line = line.rstrip()
#     word = line.split()
#     if(len(word) < 3 or word[0] != 'From'):
#         continue
#     counts[word[1]] = counts.get(word[1],0) + 1

# bigcount = None
# bigword = None
# for word,count in counts.items():
#     if bigcount is None or count > bigcount:
#         bigword = word
#         bigcount = count

# print(bigword,bigcount)
# -----------------------------------------------------------------------------------------------------------------
# name = input('Enter File:')
# if len(name) < 1:
#     name = "mbox-short.txt"
# handle  = open(name)

# counts = dict()
# for line in handle:
#     line = line.rstrip()
#     word = line.split()
#     if(len(word) < 3 or word[0] != 'From'):
#         continue
#     word = word[5].split(':')[0]
#     counts[word] = counts.get(word,0) + 1

# for k,v in sorted(counts.items()):
#     print(k,v)
# -----------------------------------------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------------------------------------