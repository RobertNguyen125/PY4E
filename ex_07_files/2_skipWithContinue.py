# #convenient;y skip a line by using continue statement
# fhand = open('mbox_short.txt')
# for line in fhand:
#     line = line.rstrip()
#     if not line.startswith('From: '):
#         continue
#     print(line)

#look for string anywhere in a line as our selection criteria

fhand = open('mbox_short.txt')
for line in fhand:
    line = line.rstrip()
    if not '@uct.ac.za' in line:
        continue
    print(line)
