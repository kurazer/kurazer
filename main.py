class Students:
    id=0
    flo=''
    id_project=0
    class =''
    score=0

f=open("students.csv")
students=[]
j=0
for i in f:
    s=i.split(",")
    if int(s[3][:-1])==10:
        students.append(Students())
        students[j].fio = s[1]
        students[j].score = int(s[4])
        j+=1

for i in range(students):
    j=1
    t=students[i]
    while j>0 and students[j-1]>t.score:
        students[j] = students[j-1]
        j-=1
    students[j]=t

students_fio=students[1]
students_fio.split()


print(f'1 место: {students_fio[1]}')
print(f'2 место: {}')
print(f'3 место: {}')