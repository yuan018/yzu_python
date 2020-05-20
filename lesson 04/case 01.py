# 數組 List, Set, Dict

scores = [100, 90, 80]
scores.append(70)
print(scores)

for x in scores:
    print(scores.index(x), x)

for (i, x) in enumerate(scores):
    print(i, x)

tt = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(tt.pop(0))

poker = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
count = poker.count(2)
print(count)