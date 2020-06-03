import sys
import traceback

x = 10
y = int(input('請輸入數字:'))
try:
    z = x / y
except Exception as e:
    print('捕獲到錯誤', e)
    print(e.__class__.__name__)
    cl, exc, tb = sys.exc_info()
    lastCallStack = traceback.extract_tb(tb)[-1]
    print(lastCallStack)
else:
    print(z)