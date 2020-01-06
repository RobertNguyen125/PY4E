#open the file then count all the words
fhand= open('romeo.txt')
counts = dict()
for line in fhand:
    words = line.rstrip()
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

#print(sorted([v,k] for k,v in counts.items()))
#create a list to reverse key and values
lst = list()
for key, val in counts.items():
    newtup = (val, key)
    lst.append(newtup)

lst = sorted(lst, reverse=True)

for val, key in lst[:10]: #only for most 10 common words
    print(key, val)
