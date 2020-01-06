rawstr = input('Enter a number:')
try:
    ival = int(rawstr) # this refers to the rawstr above
except:
    ival = -1

if ival > 0:
    print('Nice work')
else:
    print('Not a number')

'''inp = input('Enter Fahrenheit Temperature: ')
try: # for user to enter the numerical value
    fahr = float(inp)
    cel = (fahr - 32.0) * 5.0 / 9.0
    print(cel)
except: #when user enter a value other than numerical
    print ("please enter a number: ")'''
