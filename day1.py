
cals = []
with open('/Users/sburgholzer/Documents/Advent of Code/2022/day1.txt', 'r') as f:
    for line in f.readlines():
        cals.append(line)


totalCals = []

total = 0
for cal in cals:
    if cal == "\n":
        totalCals.append(total)
        total = 0
        continue
    
    total += int(cal.strip("\n"))
totalCals.append(total)

print(max(totalCals))

totalCals.sort(reverse=True)

print(totalCals[0] + totalCals[1] + totalCals[2])