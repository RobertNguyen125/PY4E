fname = input('Enter name: ')
if len(fname) < 1: fname = 'clown.txt' #if hit enter, this file will be opened
handle = open(fname)

di = dict() #di is the chosen variable
for line in handle:
    line = line.rstrip()
    # print(line)
    #for word in line: this will make duplication of the list
    word = line.split() #word is python list
    #print(word)
    for w in word: #print out the words
        # print('**',w,di.get(w,-99)) #di is the dict, w is the key to look up, e.g: the, fell etc
        #if the key is not there, the count is 0
        oldcount = di.get(w, 0)
        print(w,'old', oldcount)
        newcount = oldcount + 1
        di[w] = newcount
        print(w, 'new', newcount)
        '''if w in di:
            #print(w)
            di[w] = di[w] + 1 #if it is there, increment it
            #print('**Existing**')
        else:
            di[w] = 1 #if it is not there, set 1
            #print('**NEW**')
        print(w, di[w])'''

print(di)
