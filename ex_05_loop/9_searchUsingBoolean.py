found = False
print ('Before', found)
for value in [9, 41, 12, 3, 74, 15]:
    if value == 3:
        found = True
        print(found, value)
    #found = False
    else:
        print(value)


print('After', found)
#if we want to search and know if a value was found, we use a variable
#starting at False and set to True as soon as we find what we are looking for
