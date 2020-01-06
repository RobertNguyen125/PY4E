





'''fhand = open('mbox_short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '): continue
    words = line.split()
    email = words[1]
    name = email.split('@')
    name = name[0]
    print(name)'''

#list() can be used to convert a string into a list
#use split() to convert a string w multiple words into a list with separate words
t = 'spam'
s = list(t)
print(s)

t = 'stop spamming'
s = list(t)
print(s)

#join() is the opposite of split()
t = ['please', 'keep', 'your', 'gabbage']
delimited = ' '
s = delimited.join(t)
print(s)
