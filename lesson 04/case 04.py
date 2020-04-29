
e1 = {'name': 'John', 'salary': 50000, 'program' : ['Java', 'python']}
e2 = {'name': 'Mary', 'salary': 60000, 'program' : ['VB', 'python']}
e3 = {'name': 'Bob', 'salary': 70000, 'program' : ['C#']}
emps = [e1, e2, e3]

# 求會python 的人名?

names = []

for emp in emps:
    for p in emp['program']:
        if p == 'python' :
            names.append(emp['name'])
            continue



print(names)