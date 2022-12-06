

data = ""
with open('day6.txt', 'r') as f:
    data = f.readlines()

def checkIfDuplicates_1(listOfElems):
    ''' Check if given list contains any duplicates '''
    if len(listOfElems) == len(set(listOfElems)):
        return False
    else:
        return True

for item in data:
    numChar = 4
    tempArr = []
    for letter in item:
        tempArr.append(letter)
        if len(tempArr) == 4:
            result = checkIfDuplicates_1(tempArr)
            if result:
                numChar += 1
                tempArr.pop(0)
    print(numChar)

for item in data:
    numChar = 14
    tempArr = []
    for letter in item:
        tempArr.append(letter)
        if len(tempArr) == 14:
            result = checkIfDuplicates_1(tempArr)
            if result:
                numChar += 1
                tempArr.pop(0)
    print(numChar)