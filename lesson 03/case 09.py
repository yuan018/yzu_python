# 切割
text = "ridus = 10"
# 求圓面積
name, r = text.split('=')
r = int(r) # str(字串) 轉 int(數字)
print("%s 為 %d 的圓面積是 %.2f" % (name, r, r*r * 3.14))