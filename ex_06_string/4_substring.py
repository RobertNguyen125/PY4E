'''this is also known as the string method where there is
a python library to deal with string'''

fruit = 'banana'
pos = fruit.find('na')
print(pos)

#str.replace(old, new[, count])
greet = 'Hello Bob'
nstr = greet.replace('Bob', 'Jane')
print(nstr)

#stripping white space lstrip(), rstrip(), strip
greet = '    Hello Bob  '
greet = greet.strip()
print(greet)

data = ' from stephen.sth@uts.com.au sat jan 5 9:00:9'
atpos = data.find('@') #find the position of '@'
print(atpos)

sppos = data.find(' ', atpos)# find the first space after '@'
print(sppos)

host = data[atpos+1 : sppos]# because python counts from 0 -> + 1
print(host)
