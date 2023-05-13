def Rotnuoc(matran, T0, goal):
    M0 = [T0]
    Cha = {T0: None}
    DONG = [T0]

    while M0:
        n = M0.pop(0)
        if n == goal:
            road = []
            while n is not None:
                road.append(n)
                n = Cha[n]
            return list(reversed(road))
        else:
            An = [i for i in range(len(matran[n])) if matran[n][i] == 1]
            for i in An:
                if i not in DONG:
                    M0.append(i)
                    DONG.append(i)
                    Cha[i] = n
    return None



matran = [
    [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

check = Rotnuoc(matran, 0, 8 or 13)
if check is None:
    print("Khoong tim thay duong di tu dinh 0 den dinh 5")
else:
    print("Duong di tu dinh A den dinh I:", check)