import random

hangman = [

    '''
  +---+
      |
      |
      |
     ===''',
    '''
  +---+
  O   |
      |
      |
     ===''',
    '''
  +---+
  O   |
  |   |
      |
     ===''',
    '''
  +---+
  O   |
 /|   |
      |
     ===''',
    '''
  +---+
  O   |
 /|\  |
      |
     ===''',
    '''
  +---+
  O   |
 /|\  |
 /    |
     ===''',
    '''
  +---+
  O   |
 /|\  |
 / \  |
     ==='''
]

words = 'siema kamkar rzemis pawel witek czesc elo dzien kot pies drzewo'.split()


def getRandomWord(wordList):
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]


def tablica(pozostaleLitery, odgadnieteLitery, haslo, nietrafioneProby):
    print(hangman[nietrafioneProby])
    print()

    print('Nietrafione litery:', end=' ')
    for letter in pozostaleLitery:
        print(letter, end=' ')
    print()

    blanks = '_' * len(haslo)

    for i in range(len(haslo)):
        if haslo[i] in odgadnieteLitery:
            blanks = blanks[:i] + haslo[i] + blanks[i + 1:]

    for letter in blanks:
        print(letter, end=' ')
    print()

    print('Liczba pozostałych prób:', maxNietrafioneProby - nietrafioneProby)


def getGuess(odgadniete):
    while True:
        print('Wpisz literę lub odgadnij całe hasło')
        guess = input()
        guess = guess.lower()
        if len(guess) == len(haslo):
            return guess
        elif len(guess) == 1 and guess.isalpha() and guess not in odgadniete:
            return guess
        else:
            print('Wprowadź poprawną literę lub spróbuj odgadnąć całe hasło')


def playAgain():
    print('Chcesz zagrać ponownie? (t/n)')
    return input().lower().startswith('t')


print('H A N G M A N')
pozostaleLitery = ''
odgadnieteLitery = ''
haslo = getRandomWord(words)
end = False
nietrafioneProby = 0
maxNietrafioneProby = 6

while True:
    tablica(pozostaleLitery, odgadnieteLitery, haslo, nietrafioneProby)

    guess = getGuess(pozostaleLitery + odgadnieteLitery)

    if len(guess) == len(haslo):
        if guess == haslo:
            print('Gratulacje, zgadłeś! Poprawne słowo to "' + haslo + '"!')
            end = True
        else:
            print('Niepoprawne hasło.')
            nietrafioneProby += 1
            if nietrafioneProby == maxNietrafioneProby:
                tablica(pozostaleLitery, odgadnieteLitery, haslo, nietrafioneProby)
                print('Przegrałeś! Wykorzystałeś wszystkie próby. Poprawne hasło to "' + haslo + '"')
                end = True
    else:
        if guess in haslo:
            odgadnieteLitery += guess

            odgadlesHaslo = all(letter in odgadnieteLitery for letter in haslo)
            if odgadlesHaslo:
                print('Gratulacje, zgadłeś! Poprawne słowo to "' + haslo + '"!')
                end = True
        else:
            pozostaleLitery += guess
            nietrafioneProby += 1

            if nietrafioneProby == maxNietrafioneProby:
                print('Przegrałeś! Wykorzystałeś wszystkie próby. Poprawne hasło to "' + haslo + '"')
                end = True

    if end:
        if playAgain():
            pozostaleLitery = ''
            odgadnieteLitery = ''
            nietrafioneProby = 0
            end = False
            haslo = getRandomWord(words)
        else:
            break