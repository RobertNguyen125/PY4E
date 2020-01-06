largest = None
smallest = None
while True:
    num = input("Enter a number: ")

    try:
        fnum = float(num)
        if num == "done" :
                break
            #print(num)
    except ValueError:
        print("please enter a number:")
        continue


for value in [fnum]:
    if largest is None or fnum < largest:
        fnum = largest
    print ("maximum", largest)

for value in [fnum]:
    if smallest is None or fnum > smallest:
        fnum = smallest
    print("Minimum", smallest)
