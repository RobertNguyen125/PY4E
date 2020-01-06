sum = 0
count = 0 #introduce a counter/sum variable that starts = 0 then add one to it each time through the loop
print ('Before ','Sum: ', sum, 'Count :', count)
for thing in [9, 12, 20, 48, 10]:
    sum = sum + thing #this is to sum
    count = count + 1
    print (thing, sum, count)
print ('After', 'Sum:', sum, 'Count:', count, 'Avg:', sum/count)
