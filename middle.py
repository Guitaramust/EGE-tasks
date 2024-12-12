
f=open('24.1.txt')
a=f.readline()
gardens=['']
flag=0
for i in range(len(a)):
    if a[i]=="[":
        gardens.append(a[i])
        flag=1
    elif a[i]=="]" and flag==1:
        gardens[-1]+=a[i]
        flag=0
    elif flag==1 and a[i]!=']' and a[i]!='[':
        gardens[-1]+=a[i]
mx=0
for i in range(len(gardens)-1):
    if len(gardens[i])>=2:
        if gardens[i][0]=='[' and gardens[i][-1]==']' and gardens[i][1:-1]==gardens[i][::-1][1:-1]:
            mx=max(mx,len(gardens[i]))
print(mx)


f=open('24.2.txt')
a=f.readline()
skills=set()
for i in range(len(a)):
    skills.add(a[i])
print(len(skills))





