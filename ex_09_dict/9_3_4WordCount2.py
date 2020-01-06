name = input('Enter file: ')
handle = open(name)

counts = dict()
#outer loop go along the line
for line in handle:
    words = line.split() # split the line in the file into words
    #inner loop go through each word
    for word in words:
        counts[word] = counts.get(word, 0) + 1

#print('Count:', counts)

bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word #refer to word above
        bigcount = count #refer to counts above

#since python offers the k,v; this is convenient as v will go with k

print(bigword, bigcount)
