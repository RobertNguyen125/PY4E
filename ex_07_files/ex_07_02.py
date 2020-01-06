'''prompt file name
look for file witth pattern: “X-DSPAM-Confidence: 0.8475
When encounter, pull the floating number on these lines
count these lines then compute the total number
of spam confidence. When reach the end of the file,
print the AVG spam confidnce'''

fname = input('Enter file name: ')
fhand = open(fname)
count = 0
total = 0
for line in fhand:
    line = line.rstrip()
    if line.startswith('X-DSPAM-Confidence:'):
#count how many times the text appear:
        count = count+1
        colon = line.find(':')
#look for the number and convert to float to calculate the total        
        number = line[colon+1:]
        number = number.lstrip()
        number = float(number)
        total = total + number

print('Average spam confidence: ', total/count)
