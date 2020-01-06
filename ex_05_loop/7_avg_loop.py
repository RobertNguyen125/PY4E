count = 0
sum = 0
print ('Before', count, sum)
for value in [ 9, 10, 89, 20, 43]:
    count = count + 1
    sum = sum + value
    print (count, sum)
print ('After', count, sum, sum/count)  
