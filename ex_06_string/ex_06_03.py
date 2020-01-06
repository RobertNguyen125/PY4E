def count(word, letter):

    count = 0

    for char in word:
        if char == letter:
            count = count + 1
    print (count)

word = input('please enter the word: ')
letter = input('please enter the letter: ')
count(word, letter)

''' the exercise is to count any letter from a string.
So you input the word then the letter that you want to count'''
