file = open('salary.txt.py', 'r', encoding='UTF-8')
rows = file.readlines()
print(rows)

#求總薪資
employees = []
for row in rows:
    data = row.split(", ")
    dict = {'name':data[0], 'salary':int(data[1].strip('\n'))}
    employees.append(dict)

print(employees)

sum = 0
for emp in employees:
    sum = sum + emp['salary']

print(sum)
