#read the *whole* file into a single string

fhand = open('mbox_short.txt')
inp = fhand.read()
print(len(inp))

print(inp[:20])
