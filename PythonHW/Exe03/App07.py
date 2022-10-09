sentenceAsList = str(input()).split(" ")

#Премахваме думите с по малко от 3 символа
for x in sentenceAsList:
    if len(x) < 3:
        sentenceAsList.remove(x)

#Принтираме елементите от листа
for x in sentenceAsList:
    print(x + " ", end = "")