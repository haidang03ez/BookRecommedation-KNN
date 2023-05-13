def Docfile(filename):
    f = open(filename, mode = 'r')
    n, m = f.readline().split()
    n = int(n)
    print(n, m)
    for i in range(n):
        print(f.readline(), end = '')
    f.close()

Docfile('D:/pythonProject/file.txt')

def Docfile1(filename):
    s = []
    a = b = 0
    f = open(filename, mode = 'r')
    a, b = f.readline().split()
    a = int(a)
    b = int(b)
    for i in range (a):
        k = list(map(float, f.readline().split()))
        s.append(k)
    f.close()
    return s, a, b

a, n , m = Docfile1('D:/pythonProject/file.txt')
print(a, n, m)