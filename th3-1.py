from module31 import *


a = vecinput()
b = vecinput()

print('Mang 1: ', a)
print('Mang 2: ', b)

print('Tong cac phan tu trong mang 1: ', vecsum(a))
print('Tong cac phan tu trong mang 1: ', vecsum(b))

vecinsert(a, 5, 1)
vecinsert(b, 5, 1)

print('Mang 1: ', a)
print('Mang 2: ', b)

vecdel(a, 1)
vecdel(b, 1)

print('Mang 1: ', a)
print('Mang 2: ', b)

print('Tong hai mang: ', vecadd(a,b))