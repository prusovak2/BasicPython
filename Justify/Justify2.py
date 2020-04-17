import sys
from sys import stdin


class WordReader:
    EndOfColumn = False
    EndOfFile = False
    fileToRead = ""
    words = list()

    def __init__(self, file):
        if file == "stdin":
            self.fileToRead = stdin
        else:
            self.fileToRead = open(file, mode='r')

    def ReadColumn(self):
        line = self.fileToRead.readline()
        while line.strip() == "":
            if line == "":
                self.EndOfFile = True
            line = self.fileToRead.readline()
        while line.strip() != "":
            for word in line.split():
                self.words.append(word)
            if line == "":
                self.EndOfFile = True
            line = self.fileToRead.readline()
        while line.strip() == "":
            if line == "":
                self.EndOfFile = True
            line = self.fileToRead.readline()


class LineMaker:
    WidthOfLine = int()
    RemainingCapacity = int()
    WordsOnLine = list()
    #WordGenerator = None
    wordReader = None
    wordWaiting = ""
    ColumnBuffer = list()

    def __init__(self, width, wordReader):
        self.WidthOfLine = width
        self.RemainingCapacity = width
        #self.WordGenerator = WordReader.ReadWord(wordReader)
        self.wordReader = wordReader

    def TryAddWord(self, word):
        if len(self.WordsOnLine) == 0:
            self.WordsOnLine.append(word)  # adding the first word on line - it does always fit
            self.RemainingCapacity -= len(word)
            return True
        if self.RemainingCapacity >= (len(word) + 1):  # the word does fit current with a space before it
            self.WordsOnLine.append(word)
            self.RemainingCapacity -= (len(word) + 1)  # word and space before it
            return True
        #word does not fit the line
        self.wordWaiting = word  # store the word
        return False  # inform that line is ready to be printed

    def PrepareLineToBePrinted(self, endOfColumn):
        if len(self.WordsOnLine) == 1:  # only one word on line
            return self.WordsOnLine[0]  # to be aligned to left
        if len(self.WordsOnLine) < 1:
            print("PREPARELINE: ERROR")
            return None
        if endOfColumn:  # the last line of the column - is to be aligned to left
            line = ""
            index = 0
            while index < (len(self.WordsOnLine) - 1):
                line += self.WordsOnLine[index]
                line += " "  # one space between words
                index += 1
            line += self.WordsOnLine[len(self.WordsOnLine)-1]  # do not add a space after the last word
            return line
        # regular line
        spacesToAdd = self.RemainingCapacity  # num of chars to be added to line
        spacesToFill = (len(self.WordsOnLine) - 1)  # number of spaces between words
        baseSpaces = (spacesToAdd // spacesToFill) + 1  # an amount of space chars to be put into every space between words
        spacesToDistribute = spacesToAdd % spacesToFill  # additional spaces to be added from left
        line = ""
        i = 0
        while i < spacesToDistribute:
            line += self.WordsOnLine[i]
            j = 0
            while j < (baseSpaces + 1):  # to the first spacesToDistribute spaces add one more space above baseSpaces
                line += " "
                j += 1
            i += 1
        i = spacesToDistribute
        while i < spacesToFill:
            line += self.WordsOnLine[i]
            j = 0
            while j < baseSpaces: # rest of spaces fill with baseSpaces spaces
                line += " "
                j += 1
            i += 1
        # add the last word with no spaces behind it
        line += self.WordsOnLine[spacesToFill]  # spacesToFill = wordsOnLine.Count() -1
        return line

    def BuildAndPrintLine(self, word, endOfFile):
        added = self.TryAddWord(word)
        if added & (not self.wordReader.EndOfColumn):
            return False  # not finished line
        if(not added) & self.wordReader.EndOfColumn:
            # special case: word does not fit the previous line and it ends the column at the same time
            # I need to print what is stored in line first
            line = self.PrepareLineToBePrinted(endOfColumn=False)  # this line does not end the column
            # not fitting word is stored in self.WordWaiting
            #print(line)
            self.ColumnBuffer.append(line+'\n')
            self.ClearLine()
            self.TryAddWord(self.wordWaiting)  # add non fitting word on a new line
            self.wordWaiting = ""
            line = self.PrepareLineToBePrinted(self.wordReader.EndOfColumn)
            self.ColumnBuffer.append(line+'\n')
            if not endOfFile:
                self.ColumnBuffer.append('\n')  # one line between columns
            toPrint = ""
            print(toPrint.join(self.ColumnBuffer), end='')
            self.ColumnBuffer.clear()
        elif self.wordReader.EndOfColumn:  # the last line of the column
            line = self.PrepareLineToBePrinted(self.wordReader.EndOfColumn)
            self.ColumnBuffer.append(line + '\n')
            if not endOfFile:
                self.ColumnBuffer.append('\n')  # one line between columns
            toPrint = ""
            print(toPrint.join(self.ColumnBuffer), end='')
            self.ColumnBuffer.clear()
        else:  # a regular finished line
            line = self.PrepareLineToBePrinted(self.wordReader.EndOfColumn)
            # print(line)
            self.ColumnBuffer.append(line + '\n')
        self.ClearLine()  # it has just been printed
        if self.wordWaiting != "":
            self.TryAddWord(self.wordWaiting)  # it has to fit - it's gonna be the first word on line
            self.wordWaiting = ""
            return True  # finished line




    def Justify(self):
        wordToBeAdded = next(self.WordGenerator)
        if wordToBeAdded == "":
            wordToBeAdded = next(self.WordGenerator)
        followingWord = ""
        while True:
            try:
                followingWord = next(self.WordGenerator)
            except StopIteration:
                self.wordReader.EndOfColumn = True
                self.BuildAndPrintLine(wordToBeAdded, endOfFile=True)
                break
            self.BuildAndPrintLine(wordToBeAdded, self.wordReader.EndOfFile)
            if followingWord == "":
                try:
                    wordToBeAdded = next(self.WordGenerator)
                except StopIteration:
                    self.wordReader.EndOfColumn = True
                    self.BuildAndPrintLine(wordToBeAdded, endOfFile=True)
                    break
            else:
                wordToBeAdded = followingWord

    def Justify2(self):
        while not self.wordReader.EndOfFile:
            WordReader.ReadColumn(self.wordReader)
            i = 0
            while i < (len(self.wordReader.words) - 1):
                self.wordReader.EndOfColumn = False
                self.BuildAndPrintLine(self.wordReader.words[i], self.wordReader.EndOfFile)
                i += 1
            self.wordReader.EndOfColumn = True
            self.BuildAndPrintLine(self.wordReader.words[i], self.wordReader.EndOfFile)
            self.wordReader.words.clear()

    def ClearLine(self):
        self.WordsOnLine.clear()
        self.RemainingCapacity = self.WidthOfLine


# MAIN
'''
print("abraka")
reader = WordReader("text.txt")
reader.ReadColumn()
for i in reader.words:
    print(i)
print(reader.EndOfFile)
'''
if len(sys.argv) != 2:
    print("Error")
    exit(1)
try:
    width = int(sys.argv[1])
except:
    print("Error")
    exit(1)
if width < 1:
    print("Error")
    exit(1)

reader = WordReader("testFile.in")
lineMaker = LineMaker(width, reader)
lineMaker.Justify2()
