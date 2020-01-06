# contruct a list of tuples of the (value,key) to sort by value
# do this with a for loop

c = {'a': 10, 'b':1, 'c': 22}
tmp = list()
for k,v in c.items():
    tmp.append((v,k)) #this will reverse the order of Key and Value by append the list a tuple
print(tmp)

tmp = sorted(tmp, reverse=True) #this will sort dictionary according to values
print(tmp)
