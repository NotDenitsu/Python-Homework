#Разделяме стринга в масив и връщаме размера му, т.е. броя думи
def word_Count (moveToList):
    return len(moveToList)

#Взимаме вход за стринга
t = str(input())

#Подаваме стринга разделяйки го при всяко разстояние
print(word_Count(t.split(" ")))


