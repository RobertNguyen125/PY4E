fruit = 'banana'
index = 0
#while index <len(fruit):
for i in fruit:
    letter = fruit[index]
    #index = index + 1, this will make the index run from 1 instead of 0
    print(index, i)
    index = index + 1
