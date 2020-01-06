# # a file handle open for read can be treated as a sequence of strings
# where each line in the file is a strong in the sequence
# Use for statement to iterate through a sequence - which is an ordered set
xfile = open('mbox.txt')
for cheese in xfile: #run this loop one time for every line the print it out
    print(cheese)
