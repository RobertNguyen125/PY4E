score = input("Enter Score: ")
x = float(score) # need to declare because the range 0.1 and 1 wont work with string
if 0.0 < x and x < 1:
 if x >= 0.9:
        print("A")
 elif x >= 0.8:
        print("B")
 elif x >= 0.7:
        print("C")
 elif   >= 0.6:
        print("D")
 else:
        print("F")
else:
 print("error")
