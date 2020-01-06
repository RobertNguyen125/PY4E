def computepay(hours, rate):
    if hours > 40:
        reg = hours * rate
        ot = (hours - 40) * (rate *0.5)
        pay = reg + ot
        return pay #return the result for the print() below

    else:
        pay = hours * rate
        return pay# return the result for the print() below



sh = input("Enter hours: ")
sr = input("Enter rate: ")
fh = float(sh)
fr = float(sr)

xp = computepay(fh,fr)# call the function def above

print('Pay: ', xp)
