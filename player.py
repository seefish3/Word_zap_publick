import random
class Player:

    def __init__(self, name):
        self.name = name
        self.letters = []
        for i in range(7):
            self.drawLetter()

    def getName(self):
        return self.name

    def getLetters(self):
        return self.letters

    def drawLetter(self):
        let = 'aaaaaaaaabbccddddeeeeeeeeeeeeffggghhiiiiiiiiijkllllmmnnnnnnooooooooppqrrrrrrssssttttttuuuuvvwwxyyz'
        self.letters.append(let[random.randint(0, len(let))])
        return self.letters[-1]

    def printLetters(self):
        letstr = ""
        for l in self.letters:
            letstr += l
        letstr = letstr.strip()
        return letstr
            
    def checkWord(self, word):
        ulet = self.letters[:]
        letc = True
        for i in word:
            if i in ulet:
                remove[ulet[i]]
        
        
                    
                 
