plays = {"A": "Rock", "B": "Paper", "C": "Scissors", "X": "Rock", "Y": "Paper", "Z": "Scissors"}
upDatedPlays = {"A": "Rock", "B": "Paper", "C": "Scissors", "X": "lose", "Y": "draw", "Z": "win"}
shapeScores = {"Rock": 1, "Paper": 2, "Scissors": 3}

elve = []
me = []

with open('day2.txt', 'r') as f:
    for line in f.readlines():
        elve.append(line.split(" ")[0])
        me.append(line.split(" ")[1].strip("\n"))

completeTotal = 0
for i, elvePlay in enumerate(elve):
    elvePlays = elvePlay
    iPlays = me[i]

    shapeScore = shapeScores[plays[iPlays]]

    if plays[iPlays] == "Rock" and plays[elvePlays] == "Scissors":
        roundScore = 6
    elif plays[iPlays] == "Scissors" and plays[elvePlays] == "Paper":
        roundScore = 6
    elif plays[iPlays] == "Paper" and plays[elvePlays] == "Rock":
        roundScore = 6
    elif plays[iPlays] == plays[elvePlays]:
        roundScore = 3
    else:
        roundScore = 0

    totalRoundScore = shapeScore + roundScore
    completeTotal += totalRoundScore

print(completeTotal)

completeTotal = 0
for i, elvePlay in enumerate(elve):
    elvePlays = upDatedPlays[elvePlay]
    iPlays = upDatedPlays[me[i]]

    if elvePlays == "Rock":
        if iPlays == "win":
            iPlaysShape = "Paper"
            shapeScore = shapeScores[iPlaysShape]
            roundScore = 6
        elif iPlays == "draw":
            iPlaysShape = "Rock"
            shapeScore = shapeScores[iPlaysShape]
            roundScore = 3
        elif iPlays == "lose":
            iPlaysShape = "Scissors"
            shapeScore = shapeScores[iPlaysShape]
            roundScore = 0


    elif elvePlays == "Scissors":
        if iPlays == "win":
            iPlaysShape = "Rock"
            shapeScore = shapeScores[iPlaysShape]
            roundScore = 6
        elif iPlays == "draw":
            iPlaysShape = "Scissors"
            shapeScore = shapeScores[iPlaysShape]
            roundScore = 3
        elif iPlays == "lose":
            iPlaysShape = "Paper"
            shapeScore = shapeScores[iPlaysShape]
            roundScore = 0
    
    elif elvePlays == "Paper":
        if iPlays == "win":
            iPlaysShape = "Scissors"
            shapeScore = shapeScores[iPlaysShape]
            roundScore = 6
        elif iPlays == "draw":
            iPlaysShape = "Paper"
            shapeScore = shapeScores[iPlaysShape]
            roundScore = 3
        elif iPlays == "lose":
            iPlaysShape = "Rock"
            shapeScore = shapeScores[iPlaysShape]
            roundScore = 0
        
    totalRoundScore = shapeScore + roundScore
    completeTotal += totalRoundScore

print(completeTotal)
