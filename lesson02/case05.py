# -*- coding:UTF-8 -*-
symbol = "2330.TW"
name = "台積電"
price = 286.5
shares = int(input("請輸入股數"))

print("2330.TW 台積電成交價 286.5 買進 5000 股 (5張) 成本 1,432,500.0")
# %s(放字串) %d(放整數) %f(放浮點數)
print("%s %s成交價 %.1f 買進 %d 股 (%d張) 成本 %.1f" %
      (symbol, name, price, shares, shares/1000, price * shares))