

fname = input("enter file name: ")
fhand = open(fname)

line1 = list() #declare the lust
for line in fhand:
    #line = line.rstrip()
    words = line.split() #split the paragraph
    for word in words:
        if word in line1:
            continue    #disregard duplication
        line1.append(word) #update the list
print(sorted(line1))

# my_list = []
# fhand = open('romeo.txt')
# for line in fhand:
#     words = line.split()
#     for word in words:
#         if word in my_list:
#             continue
#         my_list.append(word)
# print(sorted(my_list))
