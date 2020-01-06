

num_list = list()
while True:
    inp = input("Enter number: ")
    if inp == 'done':
        break
    try:
        finp = float(inp)
    except:
        print("Please enter numerical value")
        continue
    num_list.append(finp)
print(max(num_list))
print(min(num_list))
