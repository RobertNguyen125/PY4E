numlist = list()

while True:

    try:
        inp = input('Enter Number:')
        if inp == 'done':
            break
        value = float(inp)
    except:
        print('Please enter numeric values: ')
        numlist.append(value)

average = sum(numlist)/len(numlist)
print('Average:', average)
