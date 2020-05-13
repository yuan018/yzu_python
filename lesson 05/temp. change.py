C = 0
F = 0
def ctof(c):
    global F
    F = c * (9 / 5) + 32

def ftoc(f):
    global C
    C = (f -32) * 5 / 9

ctof(-10)
print('F=', F)

ftoc(-10)
print("C=", C)