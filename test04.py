a = int(input())

a1 = a // 1000
a2 = (a - a1 * 1000) // 100
a3 = (a - a1 * 1000 - a2 * 100) // 10
a4 = a % 10
# print(a1, a2, a3, a4)

if a1 > a2:
    a1, a2 = a2, a1

if a2 > a3:
    a2, a3 = a3, a2

if a3 > a4:
    a3, a4 = a4, a3
    
if a1 > a2:
    a1, a2 = a2, a1

if a2 > a3:
    a2, a3 = a3, a2

if a1 > a2:
    a1, a2 = a2, a1

# print(a1, a2, a3, a4)

print(a1 * 1000 + a2 * 100 + a3 * 10 + a4)
