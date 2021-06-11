import random
import time

print('\nWelcome to Hangman\n')
time.sleep(1)

pWords=list()

#Open a dictonary of words and store them in pWords as list
fhand=open('dict.txt')
for lines in fhand:
    lines=lines.strip()
    pWords.append(lines)

def findWords(): #Select a random word from dictionary
    global word, copyWord
    lastIndex=len(pWords)-1
    word=pWords[random.randint(0,lastIndex)]
    word=word.upper()
    copyWord=word
    word=list(word)

def hint(): #Returns a no. of letter to be displayed as hint
    global indexLetter
    indexLetter=list()
    displaylets=(len(word)//3)+1
    while (displaylets!=0):
        temp=random.randint(0,len(word)-1)
        if temp not in indexLetter:
            indexLetter.append(temp)
            indexLetter.sort()
            displaylets-=1

def generateRiddle(): #Generate the words with missing letters
    global riddle, nonriddle
    riddle=''
    nonriddle=''
    for i in range(0,len(word)):
        if i in indexLetter:
            riddle+=word[i]
            nonriddle+='*'
        else:
            riddle+='*'
            nonriddle+=word[i]
    riddle=list(riddle)
    nonriddle=list(nonriddle)

def displayRiddle(): #Display the Riddle
    striddle=''
    for l in riddle:
        striddle=striddle+l
    print(' '+striddle)

def showLines():
    print('x'+'-'*len(riddle)+'x')

def guessChecker(): #Check if won
    guess=8
    while guess!=0:
        if '*' not in riddle:
            print('\nYou won! You guessed '+copyWord +' correctly!')
            break
            exit()
        print('\nYou have '+str(guess)+' guesses left!')
        showLines()
        displayRiddle()
        showLines()
        print('\nGuess a letter')
        letter=input().upper()
        if letter in word and letter in nonriddle:
            while letter in word:
                pos=word.index(letter)
                riddle[pos]=word[pos]
                word[pos]='*'
            continue
        guess-=1
    if '*' in riddle:
        print('\nYou lost! The word was '+copyWord)



def main():
    findWords()
    hint()
    generateRiddle()
    guessChecker()

main()
