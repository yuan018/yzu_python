def print_score(**exam): # 有名參數 dict
    print(exam)
    print(type(exam))
    print(exam.keys())
    print(exam.values())
    print(exam.get('國文'))

print_score(國文= 100, 數學=80, english=70)