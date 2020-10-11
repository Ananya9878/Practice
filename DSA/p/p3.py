import random
def hangman():
    word = random.choice(['pugger', 'littlepugger','tiger','superman','thor','pokemon','avengers','savewater','earth','anabella'])
    validLetters = 'abcdefghijklmnopqrstuvwxyz'
    turns = 10
    guessmade = ''
    while len(word) > 0:
        main = ''
        missed = 0

        for letters in word:
            if letters in guessmade:
                main = main + letters
            else:
                main = main + "_" + " "


        if main == word:
            print(main)
            print('You Win!')
            break
        print('Guess the word:' , main)
        guess = input()


        if guessmade in validLetters:
            guessmade = guessmade + guess
        else:
            print('Enter a valid character')
            guess = input()

        if guess not in word:
            turns = turns - 1

        if turns == 9:
            print('9 turns left')
            print(' ---------- ')

        if turns == 8:
            print('8 turns left')
            print(' ---------- ')
            print('     0      ')

        if turns == 7:
            print('7 turns left')
            print(' ---------- ')
            print('     0      ')
            print('     |      ')

        if turns == 6:
            print('6 turns left')
            print(' ---------- ')
            print('     0      ')
            print('     |      ')
            print('    /       ')

        if turns == 5:
            print('5 turns left')
            print(' ---------- ')
            print('     0      ')
            print('     |      ')
            print('    / \     ')

        if turns == 4:
            print('4 turns left')
            print(' ---------- ')
            print('   \ 0      ')
            print('     |      ')
            print('    / \     ')

        if turns == 3:
            print('3 turns left')
            print(' ---------- ')
            print('   \ 0 /    ')
            print('     |      ')
            print('    / \     ')

        if turns == 2:
            print('2 turns left')
            print(' ---------- ')
            print('   \ 0 /|   ')
            print('     |      ')
            print('    / \     ')

        if turns == 1:
            print('1 turns left')
            print('Last breath counting')
            print(' ---------- ')
            print('   \ 0_/|   ')
            print('     |      ')
            print('    / \     ')

        if turns == 0:
            print('You Loose')
            print('You let a kind man die')
            print(' ---------- ')
            print('     0_|    ')
            print('    /|\     ')
            print('    / \     ')
            break


name = input('Enter your Name')
print('Welcome', name)
print('---------------')
print('Try to guess the name in less than 10 attempts')
hangman()
print()