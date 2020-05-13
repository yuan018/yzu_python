# -*- coding:UTF-8 -*-
import keyword

print("我是中文")

if 2 < 0 :
    print("A")
    print("B")
else:
    print("C")
    print("D")
print("E")

a = 100
b = 0b101
c = 0o12   # 八進位
print(a, b, c)

# 型態
a = 10
b = 99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
c = 1+2j
print(type(a), type(b), c, type(c))

# 變數
age, name = 18, 'Don'
print(age, name)

check = True
print(check, type(check))

score = 100
mark = score >= 50
print(mark, type(mark))

kw = keyword.kwlist
print(kw)

# 刪除變數
a = 10
print(a)
del a
print(a)
