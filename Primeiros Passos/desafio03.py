v1 = int(input("numero 1: "))
v2 = int(input("numero 2: "))
v3 = int(input("numero 3: "))

if v1> v2 > v3:
    print(v1, v2, v3)
elif v2 > v1 > v3:
    print(v2, v1, v3)
elif v1 > v3 > v2:
    print(v1, v3, v2)
elif v3 > v1 > v2:
    print(v3, v1, v2)
elif v2 > v3 > v1:
    print(v2, v3, v1)
elif v3 > v2 > v1:
    print(v3, v2, v1)


