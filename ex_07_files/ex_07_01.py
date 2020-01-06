fname = input ('Enter file name: ')
try:
    fhand = open(fname)
except:
    print ('file name invalid')
    quit()

for line in fhand:
    line = line.rstrip().upper()
    print(line)
