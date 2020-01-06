sum = 0.0
count  = 0
while True: #to ensure that the condition is met
    sval = input ('Enter number: ')
    if sval == 'done':
        break
    try:
        fval = float(sval)
    except:
        print('Please enter numeric value')
        continue #w/o continue, the code will break with the message
    sum = sum + fval #the indent to show that sum and count are included in the while loop
    count = count + 1

print('Total:', sum, 'Count:', count, 'Avg:', sum/count)
