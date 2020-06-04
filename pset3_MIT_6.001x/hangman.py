# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 18:30:22 2018

@author: luong hoang anh
"""
#problemset3_hangman.py
#Player will have to guess a secret word which is randomly chosen by computer
#Player is allowed 8 guesses and only able to submit one letter at a time
#One guess will be only lost when you guess incorrectly

import string
print(string.ascii_lowercase)

def isWordGuessed(secretWord, lettersGuessed):
   for letter in secretWord:
      if letter not in lettersGuessed :
        return False
   return True

def getGuessedWord(secretWord, lettersGuessed):
    output = ' '
    for i in range(len(secretWord)):
        if secretWord[i] in lettersGuessed:
           output += secretWord[i]
        else : 
           output += '_ '
    return output

def getAvailableLetters(lettersGuessed):
    notguessed = ' '
    for i in string.ascii_lowercase :
       if i not in lettersGuessed :
         notguessed += i
    return notguessed

def hangman(secretWord):   
    
    print('Welcome to the game, Hangman!')

    print('I am thinking of a word that is', len(secretWord), "letters long.")
    
    mistakesMade = 0

    lettersGuessed = []
    
    while 8 - mistakesMade  > 0 :
        
        if isWordGuessed(secretWord, lettersGuessed) == True :
           
           print('------------')
           
           print('Congratulations, you won!')
           
           break
        
        else :
           
           print('------------')
           
           print('You have', 8 - mistakesMade, 'guesses left.')

           print('Available letters:', getAvailableLetters(lettersGuessed))
           
           guess = str(input('Please guess a letter:')).lower()
           
           
           if guess  in secretWord and guess not in lettersGuessed :
                
                lettersGuessed.append(guess)
                
                print('Good guess :', getGuessedWord(secretWord, lettersGuessed))
           
          
           
           elif guess in lettersGuessed:
                
                print("Oops! You've already guessed that letter:", getGuessedWord(secretWord, lettersGuessed))
           
           elif guess not in secretWord:
                
                print('Oops! That letter is not in my word :', getGuessedWord(secretWord, lettersGuessed))
                
                lettersGuessed.append(guess)
                
                mistakesMade += 1
        
        if 8 - mistakesMade == 0 :
           
           print('-----------')
           
           print('Sorry, you ran out of guesses. The word was', secretWord, '.')

           break
        
        else :
         
           continue
hangman('pretty girl')