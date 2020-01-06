fname = input ('Enter file name: ')

#to prevent users from entering bad file names
try:
    fhandle = open(fname)
except:
    print('Invalid File Name')
    quit()
count = 0
for line in fhandle:
    if line.startswith('Subject:'):
        count = count + 1
print('There were', count, 'subject lines in', fname)
