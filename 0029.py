# https://acmp.ru/index.asp?main=task&id_task=29

def play(platforms):
    if len(platforms) == 1: return 0
    
    steps = [float('inf')] * len(platforms)
    steps[0] = 0
    steps[1] = abs(platforms[0] - platforms[1])
    
    for i in range(2, len(platforms)):
        x = steps[i-1] + abs(platforms[i-1] - platforms[i])
        y = steps[i-2] + 3 * abs(platforms[i-2] - platforms[i])
        steps[i] = min(x, y)
        
    return steps[-1]

n = int(input())
platforms = [int(i) for i in input().split()]
print(play(platforms))
