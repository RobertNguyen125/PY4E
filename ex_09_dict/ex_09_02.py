fname =  input('Enter File: ')
if len(fname) < 1: fname = 'clown.txt'
hand = open(fname)

di= dict()
for lin in hand:
    lin = lin.rstrip()
    #print(lin)
    wds = lin.split() # create the list
    #print(wds)
#if the w is not there, assign 1, if w is there assign di + 1
    for w in wds:
        di[w] = di.get(w,0) + 1
        #print(w)
        #print('**', w, di.get(w, -99)) #if the key appear first time, -99 will be next to
        '''oldcount = di.get(w,0) #look up using the key w, if dont get it, give back 0
        print(w,'old', oldcount)
        newcount = oldcount + 1
        di[w] = newcount
        print(w, "new", newcount)'''

        '''if w in di:
            di[w] = di[w] + 1
            #print('**Existing**')
        else:
            di[w] = 1'''
            #print('**New**')
        #print(w, di[w]) # w is the key and di is the index

print(di) #print the whole dictionary so we have the list with the counts

#find the most common words


largest = -1 #because the counter will be positive
theword = None
for k,v in di.items():
    print(k,v)
    if v > largest:
        largest = v
        theword = k
print(theword, largest)
