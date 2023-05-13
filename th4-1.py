def Inputmatrix():
    n = int(input('Nhap so dong: '))
    m = int(input('Nhap so cot: '))
    a = []
    for i in range(n):
        b = []
        for j in range(m):
            b.append(int(input('Nhap phan tu a[{}][{}] = '.format(i,j))))
        a.append(b)
    return a

def Xuatfile(a):
    f = open("D:/pythonProject/file.txt", mode ='w')
    f.write(str(len(a)) + ' ')
    f.write(str(len(a[0])) + '\n')
    for i in range(len(a)):
        for j in range(len(a[0])):
            f.write(str(a[i][j]) + ' ')
        f.write('\n')
    f.close()

s = Inputmatrix()
print(s)
Xuatfile(s)