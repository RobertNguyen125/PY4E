fname = input('Enter File: ')
if  len(fname) < 1:
    fname = 'clown.txt'

hand = open(fname)

di = {}
for lin in hand:
    lin = lin.rstrip()
    #print(lin)
    wds = lin.split()
    #print(wds)
    for w in wds:
        #because -99 is assigned to not existing keys, therefore the value will be 1
        #the first time the key is found
        #print('**',w,di.get(w,-99))

        # oldcount = di.get(w, 0)
        # print(w, 'old', oldcount)
        # newcount = oldcount + 1
        # di[w] = newcount

        di[w] = di.get(w,0) + 1
        #print(w, 'new', di[w])


        # if w in di:
        #     di[w] = di[w] +1 #the key(count) of the words
        #     #print('**Existing**')
        # else:
        #     di[w] = 1
        #     #print('**New**')
        # print(w, di[w])

#print(di)

#the most common word
largest = -1
word1 = None
smallest =  None
word2 = None
for k,v in di.items():
    print(k,v)
    if v > largest:
        largest = v
        word1 = k
    if smallest is None or v < smallest:
        smallest = v
        word2 = k


print(largest, word1)
print(smallest, word2)
