#enter number until 'done'.
#if anything but numeric enterred, use try/except to warn the users
#find the max/min of enterred number


maxVal = None
minVal = None
while True:
    sval = input('Enter the number: ')
    if sval == 'done':
        break
    try:
        fval = float(sval)
    except:
        print('Invalid Input')
        continue
    if maxVal is None or maxVal < fval:
        maxVal = fval
    if minVal is None or minVal > fval:
        minVal = fval

print('Max: ', maxVal, 'Min:', minVal)
