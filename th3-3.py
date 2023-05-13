def Input(namelist):
    a = []
    n = int(input('Nhap so luong phan tu: '))
    for i in range(n):
        a.append(int(input('{}[{}] = '.format(namelist, i))))
    return a

def mergelist(a, b):
    c = []
    if len(a) <= len(b):
        for i in range(len(a)):
            c.append(a[i])
            c.append(b[i])
        for i in range(i+1, len(b)):
            c.append(b[i])
    else:
        for i in range(len(b)):
            c.append(a[i])
            c.append(b[i])
        for i in range(i+1, len(a)):
            c.append(a[i])
    return c

a = Input('a')
b = Input('b')

print(a)
print(b)

print('Merge list: ',mergelist(a,b))