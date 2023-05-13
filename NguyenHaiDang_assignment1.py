#Bài 1:
print('Bài 1:')
n = int(input('Nhập số lượng phần tử: '))
dict_a = {}

for i in range(n):
    print('Nhập phần tử thứ',i+1)
    k = int(input('Nhập key: '))
    v = int(input('Nhập value: '))
    dict_a[k] = v**2

print(dict_a)

#Bài 2:
print('Bài 2:')
set_a = {(12,3,7,11),(2,9,5,13),(1,4,8)}

set_b = set({})

for x in set_a:
    sum = 0
    d = 0

    for i in x:
        sum = sum + i
        d = d + 1
    tbc = sum / d

    tuple_a = (x,tbc)
    set_b.add(tuple_a)

print('Tập hợp mới: ',set_b)
