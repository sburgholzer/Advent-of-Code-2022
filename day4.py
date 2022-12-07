
pairs=[]
assignments = []

data = open('day4.txt').read().strip()
lines = data.split('\n')

partOne = 0
partTwo = 0

for line in lines:
    one,two = line.split(',')
    s1,e1 = one.split('-')
    s2,e2 = two.split('-')

    s1,e1,s2,e2 = [int(x) for x in [s1,e1,s2,e2]]

    if s1<=s2 and e2<=e1 or s2<=s1 and e1<=e2:
        partOne += 1
    
    if not (e1 < s2 or s1 > e2):
        partTwo += 1

print(partOne)
print(partTwo)