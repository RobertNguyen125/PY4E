abc = 'With 3 words'
stuff = abc.split() # this will split string into list
print(stuff) #the result is a list
for w in stuff:
    print(w)
print(len(stuff)) # 3 as there are 3 elements
print(stuff[0]) # with
