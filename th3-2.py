
def listinput(namelist):
    a = []
    k = int(input('Nhap so luong: '))
    for i in range(k):
        a.append(int(input('{}[{}] = '.format(namelist, i))))
    return a

def matrixfromlist(list1):
    n = int(input('Nhap so dong: '))
    m = int(input('Nhap so cot: '))
    b = []
    if m*n > len(list1):
        print('Khong xay dung duoc ma tran')
    else:
        for i in range(n):
            k = a[i*m:i*m + m]
            b.append(k)
        return b

a = listinput('a')
print(type(a[0]))

b = matrixfromlist(a)
for i in range(len(b)):
    print(b[i])
