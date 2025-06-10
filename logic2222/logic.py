# exercise1
for i in range(11):
    print(i)
for i in range(1,11):
    print(i)
h=11-1
for i in range(11):
    print(h-i)
for i in range(16):
    if i%2==1:
        print(i)
for i in range(15):
    if i%2==0:
        print(i)
for i in range(15):
    if i>4 and i<8:
        print(i)
# exercise2
string="banana"
counter=0
for i in range(len(string)):
  counter+=1
print(counter)
string="banana"
print(string[4])
srting='banana'
'when we try to access to index 6'
"it will show you the error result because index 6 dosen't have in that code"
'it have only 5 of index'
string='banana'
for i in range(len(string)):
    print(string[i])
string='banana'
h=len(string)-1
result=""
for i in range(len(string)):
    result +=string[h-i]
print(result)
string='banana'
counter=0
for i in range(len(string)):
    if string[i]== 'a':
        counter+=1
print(counter)
# exercise3
student_ages = [15, 18, 20, 17, 16, 25]
min=student_ages[0]
for i in range(len(student_ages)):
    if student_ages[i]<min:
        min=student_ages[i]
print(min)
student_ages = [15, 18, 20, 17, 16, 25]
max=student_ages[0]
for i in range(len(student_ages)):
    if student_ages[i]>max:
        max=student_ages[i]
print(max)
student_ages= [15, 18, 20, 17, 16, 25]
sum=0
for i in range(len(student_ages)):
    sum+=student_ages[i]
print(sum/student_ages[i])
student_ages= [15, 18, 20, 17, 16, 25]
student_ages.append(19)
print(student_ages)
student_ages= [15, 18, 20, 17, 16, 25]
for i in range(len(student_ages)):
    if student_ages[i]<=18:
        student_ages[i]=22
print(student_ages)


student_ages= [15, 18, 20, 17, 16, 25]
for i in range(len(student_ages)):
    if student_ages[i]<18:
        student_ages[i]=22
print(student_ages)
# exercise4
student_score = [90, 49, 68, 40, 92, 50, 45, 59]
counter=0
for i in range(len(student_score)):
    if student_score[i]<50:
        counter+=1
print(counter)
student_score = [90, 49, 68, 40, 92, 50, 45, 59]
counter=0
for i in range(len(student_score)):
    if student_score[i]>80:
        counter+=1
print(counter)
student_score = [90, 49, 68, 40, 92, 50, 45, 59]
sum=0
for i in range(len(student_score)):
    sum+=student_score[i]
print(sum/student_score[i])
student_score = [90, 49, 68, 40, 92, 50, 45, 59]
for i in range(len(student_score)):
    if student_score[i]<=45 and student_score[i]<50:
        student_score[i]=50
print(student_score)
print("Hello world")
for i in range(10):
    print(i)
w=0
while w <10:
    print(w)
    w+=1
