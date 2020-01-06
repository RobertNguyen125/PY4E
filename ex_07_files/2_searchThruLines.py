#search through lines
fhand = open('mbox_short.txt')
for line in fhand:
    line = line.rstrip()
    if line.startswith('From:'):
        print(line)#print add additional line
