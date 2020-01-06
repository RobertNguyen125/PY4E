#tuple can be written w/o the ()
#tuole is another kind of sequence that functions like list but cant be immutable
x = 'glen', 'sally', 'joseph'
print (x[2])

# if there is single value, must include coma at the append
x = 'a',
print(type(x))

x = 'a'
print(type(x))

#below is a list
x = [9,8,7]
x[2] = 6
print (x)

#below is a tuple
#x =(5, 4, 3)
#x[2]=0
#it cant be changed because tuple is immutable

#things not to do with tuples sort, append, reverse

#tuples and assignment
(x, y) = (4, 'fred')
print(y)
