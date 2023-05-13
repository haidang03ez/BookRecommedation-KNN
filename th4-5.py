import os
import shutil

def readfile(filename):
    a = []
    f = open(filename, mode = 'r')
    n, m = f.readline().split()
    n = int(n)
    m = int(m)
    for i in range (n):
        k = list(map(float, f.readline().split()))
        a.append(k)
    f.close()
    return n, m, a

def avg(a, n, m, j):
    if j>m:
        print('Khong co cot {}'.format(j))
        return
    else:
        sum = 0
        for i in range(n):
            sum += a[i][j]
        return sum / n

def checkzero(a, n, m):
    dem = 0
    d = []
    for i in range (m):
       d.append(avg(a,n,m,i))

    for i in range(n):
        for j in range (m):
            if a[i][j]==0:
                dem = dem + 1
                a[i][j] = d[j]
    return dem, a

def nhapfile(a):
    f = open('E:/PythonCode/image2.txt', mode='w')
    f.write(str(len(a))+' ')
    f.write(str(len(a[0])) + '\n')
    for i in range(len(a)):
        for j in range(len(a[0])):
            f.write(str(a[i][j]) + ' ')
        f.write('\n')
    f.close()

def nhap100(k, filename1, filename2):
    f1 = open(filename1, mode = 'w')
    f1.write('100' + ' ')
    f1.write(str(len(k[0])) + '\n')
    for i in range(100):
        for j in range(len(k[0])):
            f1.write(str(k[i][j]) + ' ')
        f1.write('\n')
    f1.close()

    f2 = open(filename2, mode='w')
    f2.write(str(len(k) - 100) + ' ')
    f2.write(str(len(k[0])) + '\n')
    for i in range(101, len(k)):
        for j in range(len(k[0])):
            f2.write(str(k[i][j]) + ' ')
        f2.write('\n')
    f2.close()

def copydir(dirname, filename):
    os.mkdir(dirname)
    shutil.copy(filename, dirname)
    os.remove(filename)


n, m, k = readfile('E:/PythonCode/Image.data')
print(n)
print(m)
for i in range (n):
    print(k[i])

d, b = checkzero(k, n, m)
print('So luong so 0 trong tep: ',d)
print('Sau khi sua:')
for i in range (n):
    print(b[i])

nhapfile(b)

nhap100(k, 'E:/PythonCode/test1.txt', 'E:/PythonCode/test2.txt')

copydir('dir1', 'image2.txt')