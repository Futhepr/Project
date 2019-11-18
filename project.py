import random



filename = input("Input name of input file: ")
fileInput = open(filename, 'r')

initialText = fileInput.read()
fileInput.close()
sentenceNumber = int(input('Input ammount of sentences: '))
initialText = initialText.replace('\n', ' ')
text = ''
acceptableSymbols = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM' + \
                    'ЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ' + \
                    'ёйцукенгшщзхъфывапролджэячсмитьбю' + '!,.? '
for char in initialText:
    if char in acceptableSymbols:
        text = text + char


wordList = text.split()
wordListSorted = sorted(wordList)
wordListUnique = []
for wordPos in range(len(wordListSorted)):
    try:
        if not wordListSorted[wordPos] == wordListSorted[wordPos + 1]:
            wordListUnique.append(wordListSorted[wordPos])
    except IndexError: 
        wordListUnique.append(wordListSorted[wordPos])


follow = dict()
for wordPos in range(len(wordList)):
    if wordList[wordPos] in follow:
        try:
            follow.update(dict([(wordList[wordPos], follow[wordList[wordPos]] + ' ' + wordList[wordPos + 1])]))
        except IndexError:
            continue   
    else:
        try:
            follow.update(dict([(wordList[wordPos],' ' + wordList[wordPos + 1])]))
        except IndexError:
            continue


trash = ''
sentenceCount = 0
while sentenceCount < sentenceNumber:
    sentence = random.choice(wordListUnique) 
    word = sentence
    while sentence[-1] not in '!.?': 
        word = random.choice(follow[word].split())
        sentence = sentence + ' ' + word
    if not len(sentence.split()) < 5: 
        trash = trash + sentence + ' '
        sentenceCount += 1
        
output = ""
sym_num = 1
while sym_num < len(trash)-2:
    if trash[sym_num] in "!.?":
        output += trash[sym_num] + trash[sym_num+1] + str(trash[sym_num+2]).upper()
        sym_num += 2
    else:
        output += trash[sym_num]
    sym_num += 1
output = trash[0].upper() + output
output += trash[-2] 

filename = input("Input name of output file: ")
fileOuput = open(filename, 'w')
fileOuput.write(output)
fileOuput.close()

