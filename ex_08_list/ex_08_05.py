fhand = open('mbox_short.txt')
count = 0
for line in fhand:
    line = line.rstrip()
    if line.startswith('From '):
        count = count + 1
        words = line.split()
        print(words[1]) #pay attention to indentation here
print('There were ', count, ' lines in the file with From as the first words')
