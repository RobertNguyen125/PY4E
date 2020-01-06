while True:
    line = input('> ')
    if line[0] == '#':
        continue # the code runs back to the start until the break condition is satisfied
    if line == 'done':
        break
    print(line)
print('Done')
