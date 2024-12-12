f=open('24.2.txt')
a=f.readline()
skills=set()
for i in range(len(a)):
    skills.add(a[i])
print(len(skills))


