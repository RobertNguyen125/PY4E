
#1 open the file
fname = input('Enter filename: ')
if len(fname) < 1:
    fname ='clown.txt'
hand = open(fname)

#2 Create a dict() to store the value
di = {}
for lin in hand:
    lin = lin.rstrip()
    wds = lin.split()
    for w in wds:
        di[w] = di.get(w,0) + 1
print(di)

#3 Create a list to store new tuple
lst = []
for (key,val) in di.items():
    newtup = (val,key)
    lst.append(newtup)
#4 sort the lst with tuple
lst = sorted(lst, reverse=True)

print(lst[:5])

#to flip the key in front of the value:
for v,k in lst[:5]:
    print(k,v)
