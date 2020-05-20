import random

n = random.randint(1, 10)
if n % 2 == 0:
    print('%d 偶數 ' % n)
else:
    print('%d 奇數 ' % n)
# 類三源運算子的寫法
print('%d %s' % (n, "偶數" if n % 2 == 0 else "奇數"))

# 建構是否是偶數的涵式
def isOdd(n):
    return True if n % 2 == 0 else False

print('%d %s' % (n, isOdd(n)))
