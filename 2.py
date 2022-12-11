'''
A/X: Rock
B/Y: Paper
C/Z: Scissors
'''

f = open('2_strategy.txt', 'r')
strategy = f.read()

# https://github.com/betaveros/advent-of-code-2022/blob/main/p2.noul
# https://www.freecodecamp.org/news/python-switch-statement-switch-case-example/

def points_per_round(opp, i):
    points = 0
    if i == 'X':
        points += 1
        if opp == 'A':
            points += 3
        elif opp == 'B':
            points += 0
        elif opp == 'C':
            points += 6
    elif i == 'Y':
        points += 2
        if opp == 'A':
            points += 6
        elif opp == 'B':
            points += 3
        elif opp == 'C':
            points += 0
    elif i == 'Z':
        points += 3
        if opp == 'A':
            points += 0
        elif opp == 'B':
            points += 6
        elif opp == 'C':
            points += 3
    return points

def points_per_round2(opp, i, mode):
    match opp:
        case 'A':
            opp = 1
        case 'B':
            opp = 2
        case 'C':
            opp = 3

    match i:
        case 'X':
            i = 1
        case 'Y':
            i = 2
        case 'Z':
            i = 3

    points = 0
    match mode:
        case 1:
            points += i
            points += (i - opp + 1) % 3 * 3
        case 2:
            points += (i - 1) * 3
            points += (i + opp) % 3 + 1



    return points

'''
A,X 1,1 -> 3
A,Y 1,2 -> 1
A,Z 1,3 -> 2

B,X 2,1 -> 1
B,Y 2,2 -> 2
B,Z 2,3 -> 3

C,X 3,1 -> 2
C,Y 3,2 -> 3
C,Z 3,3 -> 1
'''

def total_score(strat):
    matches = strat.split('\n')
    return sum([points_per_round2(*match.split(' '), 2) for match in matches])


print(total_score(strategy))





