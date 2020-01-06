#range() function returns a list of numbers that range from 0
#to one less than the parameters
#can construct an index loop using for and and interger iterator

#1
x = range(6)
for n in x:
    print(n)

#2
friends = ['Joseph', 'Glenn', 'Sally']
print(range(len(friends)))

#3
friends = ['Joseph', 'Glenn', 'Sally']
#need len() to create the list from range()
for i in range(len(friends)):
    friend = friends[i]
    print('Happy New Year: ', friend)
