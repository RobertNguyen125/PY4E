fhand = open('mbox_short.txt')

count = 0
for line in fhand:
    line = line.rstrip()
    #if the line doesnt start with 'From', skip it then continue
    if not line.startswith('From '):
        count = count + 1
        continue
    words = line.split()
    #print(words)
    #after spliting, the word has become a list so we can use index
    print(words[2])
