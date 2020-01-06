d = {'a': 10, 'b': 1, 'c': 22}
print(d.items())
print(sorted(d.items()))

d = {'a': 10, 'b': 1, 'c': 22}
t = sorted(d.items())
for (k,v) in sorted(d.items()):
    print(k,v)

d = {'a': 10, 'b': 1, 'c': 22}
print(sorted([(v,k) for k,v in d.items()]))
#the objects inside () is considered a list as sorted() work with list()
#the objects inside [] is called list comprehension, a list dynamic
