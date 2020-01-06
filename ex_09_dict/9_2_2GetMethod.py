# to check if a key is already in the dictionary, and assuming a default value
 # if the key is not there, is common. Therefore get() can do this for us
 # to count how many times a name appears, we can use get() with a default value
 # of 0

# dictionary[key] = dictionary.get(key,0)
# get(key, value)
# key: the key that we look up
# value is optional, it is the value we assign to key if it is not found
counts =dict()
names = ['csev', 'cwen', 'csev','zqian', 'cwen']
for name in names:
    counts[name] = counts.get(name, 0) + 1 #create new and update existing entry in dict
#this is used to add new key as well as update the existing ones
#get() will need to be after the dictionary, in the above example counts is the dctionary
'''for name in names:
    if name not in counts:
        counts[name] = 1 #if python found a name that is not included in the list yet, assigned 1
    else:
        counts[name] = counts[name] +1'''
# the get() method is the same as the loop above
print(counts)
