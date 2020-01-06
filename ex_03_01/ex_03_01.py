#this exercise recyle  the code from exercise from lesson 2
sh = input("Enter hour: ") #sh means string
sr = input ("Enter rate: ") #sr means string
fh = float(sh) # convert here so you dont have to convert later
fr = float(sr) # fr float rate
# print(fh, fr)
if fh > 40:
        #print ('Overtime')
        reg = fr * fh
        OT = (fh - 40.0) * (fr * 0.5)
        print(reg,OT)
        xp =  reg + OT
else:
        #print('Regular')
        xp = fr * fh
# xp = fr * fh -- this was a mistake so the result will be w/o OT
#
print("Pay:", xp)
