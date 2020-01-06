#when you dont specify a delimiter, multiple spaces are treated like 1 delimiter
#the example below there are lot of spaces
line = 'a lot           of spaces'
list_line = line.split()
print(list_line)


#split can be used to split specific delimiter
line = 'first;second;third'
thing = line.split()
thing1 = line.split(';')
print(thing)
print(thing1)
