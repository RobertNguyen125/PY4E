
str = 'X-DSPAM-Confidence: 0.8475'

colon = str.find(':')
print(colon)

number = str[colon+1:]
print(float(number))
