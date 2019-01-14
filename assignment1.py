import os

inputFile = open("input.txt","r+")
output = open("output.txt","w")

letterFreq = {'a' : 0, 'b' : 0, 'c' : 0, 'd' : 0, 'e' : 0, 'f' : 0, 'g' : 0,
              'h' : 0, 'i' : 0, 'j' : 0, 'k' : 0, 'l' : 0, 'm' : 0, 'n' : 0,
              'o' : 0, 'p' : 0, 'q' : 0, 'r' : 0, 's' : 0, 't' : 0, 'u' : 0,
              'v' : 0, 'w' : 0, 'x' : 0, 'y' : 0, 'z' : 0 }
data = inputFile.readlines() #read in the data

totalLetters = 0
for line in range(0,len(data)): #count how many of each letter occurs in the text
    for char in data[line]:
        totalLetters = totalLetters + 1
        if char in letterFreq:
            letterFreq[char] = letterFreq[char] + 1

print(letterFreq)
print(totalLetters) #print out total number of letters (just in case you need it)

dictDecrypt = {'l' : 'B', 'y' : 'O', 'i' : 'E', 'm' : 'A', 'f' : 'H',
               'u' : 'S', 'z' : 'N', 'e' : 'I', 't' : 'T', 's' : 'U',
               'j' : 'D', 'w' : 'Q', 'v' : 'R', 'b' : 'L', 'h' : 'F',
               'g' : 'G', 'q' : 'W', 'c' : 'K', 'x' : 'P', 'o' : 'Y',
               'k' : 'C', 'a' : 'M', 'r' : 'V', 'p' : 'X', 'n' : 'Z'}
#I just stared at the text, and filled out the translation above
for line in range(0,len(data)):
    for char in data[line]:
        if char in dictDecrypt:
            data[line] = data[line].replace(char, dictDecrypt[char])
    print(data[line])
    output.write(data[line]) #write translated output to text file

output.close()
