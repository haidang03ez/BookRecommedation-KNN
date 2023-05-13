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
        print('khong co cot {} '.format(j))
    else:
        sum = 0
        for i in range(n):
            sum += a[i][j]
        return sum/n


n,m,a = readfile('D:/pythonProject/Iris.txt')
print(n)
print(m)
for i in range(n):
    print(a[i])

for i in range(m):
    print(avg(a,n,m,i))