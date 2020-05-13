# -*- coding:UTF-8 -*-

# BMI資料表
h = float(input("Height:"))
w = float(input("weight:"))
BMi = w / (h/100)**2
result = 18 <= BMi < 23
print("身高: %.1f 體重: %.1f BMI: %.2f 結果: %.1f" %
      (h, w, BMi, result))