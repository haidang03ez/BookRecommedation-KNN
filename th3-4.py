def listinput(namelist):
    a = []
    n = int(input('Nhap so luong phan tu: '))
    for i in range(n):
        a.append(int(input('{}[{}] = '.format(namelist,i))))
    return a

def mergesortedlist(a,b):
    c = []
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i = i + 1
        else:
            c.append(b[j])
            j = j+1
    if i < len(a):
        for t in range(i+1, len(a)):
            c.append(a[t])
    if j < len(b):
        for t in range(j+1, len(b)):
            c.append(b[t])
    return c

a = listinput('a')
b = listinput('b')
a.sort()
b.sort()
print(a)
print(b)

print('Merge sorted list: ', mergesortedlist(a,b))