x = [1, 2, 3]
y = [4, 5, 6]
z = x + y
print(z)

#list method
x = list()
type(x)
dir(x) #to know which methods included in list

#build a list from scratch
x = list()
x.append('book')
x.append('3')
print(x)
x.append('cookie')
print(x)

#is something in my list
list = [1, 4, 2, 6, 3]
print(4 in list)
print(20 in list)
print(20 not in list)

#sort a list
friends = ['Monica', 'Phoebe', 'Chandler']
friends.sort()
print(friends)
print(friends[0]) #Chandler is the result as the list has been sorted
