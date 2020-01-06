# we should use the first number of the list as the first measurement
#using None which is a python value, it will automatically take the first value of the list
smallest = None # the N is capitalised
print('before', smallest)
for value in [9, 102, 8, 2, 32, 1]:
    if smallest is None: #'is' is stronger than ==
        smallest = value
    elif value < smallest:
        smallest = value
    print (smallest, value)
print ('after', smallest)
