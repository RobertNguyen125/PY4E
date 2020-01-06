
xh = input('Enter hour: ')
xr = input('Enter rate: ')
try:
    fh = float(xh)
    fr = float(xr)
except:
    print('Please enter numeric input: ')
    quit()

if fh > 40:
    print('Overtime')
    reg = fh*fr
    ot = (fh-40) * (0.5*fr)
    print(reg, ot)
    xp = reg + ot
else:
    print('Regular')
    xp = fh * fr

print('Pay ', xp)
