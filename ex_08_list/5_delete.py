# use pop to delete the element if you know the index
#if index is not provided, pop() will remove the last element
friends = ['carlo', 'monica', 'rachel', 'ross']
x = friends.pop()
print(x)
print(friends)

#del() operator doesnt remove the elements
t = ['a', 'b', 'c']
del t[1]
print(t)

#remove() used to remove elements w/o index
# the return value from remove() is None
t = ['a', 'b', 'c']
t.remove('b')
print(t)

#del can be used to remove multiple elements
t = ['a', 'b', 'c', 'd', 'e', 'f']
del t[1:3]
print(t)
