import random
word_bank={ 
    'Algorithm': 'A process or set of rules followed in problem-solving or computation.',
    'Legacy': 'Something handed down from the past, often referring to inheritance.',
    'Tranquil': 'Free from disturbance or turmoil; peaceful.',
    'Serene': 'Calm, peaceful, and untroubled.',
    'Vortex': 'A whirling mass, especially of air or water, that draws things inward.'}
word,definition=random.choice(list(word_bank.items()))
guessedWord = ['_'] * len(word)
attempts=10
hint_used=False
while attempts>0:
    
    print("\n")
    guess=input("Guess a letter (or type 'hint for a clue') : ").strip()

    #if hint is requested
    if guess.lower()=='hint':
        if not hint_used:
            print('Hint : ' + definition)
            hint_used=True
        else:
            print("Hint already used.")
        continue
    
    #eliminate invalid guesses
    if not ((guess.isalpha() and len(guess)==1) or guess.lower()=='hint'):
        print("Invalid guess. Please enter a single english letter !")
        continue

    #loop to check whether guessed letter is in the actual word
    if guess.lower() in word.lower():
        for i in range(len(word)):
            if word[i].lower()==guess.lower():
                guessedWord[i]=word[i]
        print("You guessed correctly !")
    else :
        attempts-=1
        print("Incorrect guess.")
        print("Attempts left : " + str(attempts))
        continue
    
    print('\nCurrent Word : '+ ''.join(guessedWord))

    #if user is done gussing correctly
    if '_' not in guessedWord:
        print("\nCongratulations!! You guessed the word : " + word)
        break
else:
        print("\nYou ran out of attempts. The correct word was : " + word)

