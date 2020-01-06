counts = dict()
line = input('Enter a line of text:') #to split the line of words that just typed in
words = line.split()

print('Word: ', words)
print('Counting ...')

for word in words:
    counts[word] = counts.get(word, 0)+1
print('Counts', counts)
