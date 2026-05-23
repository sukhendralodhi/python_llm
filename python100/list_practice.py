def change(L):
    print(id(L))
    L.append(5)
    print(id(L))


L1 = [1,2,3,4,5]

# print(id(L1))

# print(L1)
# change(L1[:])
# print(L1)


def change1(L2):
    print(id(L2))
    L2 = L2 + (6,7)
    print(id(L2))



L3 = (1,2,3,4,5)

print(id(L3))
print(L3)
change1(L3)
print(L3)
    