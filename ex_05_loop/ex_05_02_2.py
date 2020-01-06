# need to check the code as the result is not correct
largest = None
smallest = None
while True:
    snum = input('enter number: ') #snum = string num
    if snum == 'done':
        break
    try:
        inum = int(snum) # inum = integer num
    except:
        print('invalid input')

    if largest is None or largest < inum:
        largest = inum
    if smallest is None or smallest > inum:
        smallest = inum

print('maximum is ', largest)
print('minimum is ', smallest)

'''the problem seems to be that I need to Enter
a value that is not numerical for the code to run
correctly'''

'''we use if here instead of elif because elif will link to the
the above if, 'while' will only consider the first one without
the second one '''
