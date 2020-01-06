fname = input('Enter name: ')
if len(fname) < 1 : fname = 'clown.txt'
handle = open(fname)

di = dict() # to start the dictionary and work with dictionary from here
for line in handle:
    line = line.rstrip()
    words = line.split() #words is python list
    for word in words:
        di[word] = di.get(word, 0) + 1
        print(word ,di[word])

print (di) # print the dictionary {}
