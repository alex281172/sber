abcis = list(map(int,input().split(' ')))
ordin = list(map(int,input().split(' ')))
lenth = 0
for i in range(len(abcis)-1):
    lenth = lenth + ((abcis[i+1] - abcis[i]) **2 +  (ordin[i+1] - ordin[i]) **2) ** 0.5
print(lenth)
print('{:.2f}'.format(lenth))