#Convert
n = int(input('Nhập số nguyên: '))
while n<0 or n>9999:
    n = int(input('Không hợp lệ mời nhập lại: '))

A = n//1000
B = (n//100)%10
C = (n%100)//10
D = n%10

print('Số vừa nhập là: {} nghìn {} trăm {} chục {} đơn vị'.format(A,B,C,D))