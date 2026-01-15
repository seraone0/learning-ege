#date 15.01
#2_25341
'''
print('z w x y')
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                if ((w == z) or not(y <= w) or not(x)) == False:
                    print(z, w, x, y)
z w x y
1 0 1 0
0 1 1 0
0 1 1 1
'''
#2_23739 
'''
print('z y x w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if ((x or y) and not(y==z) and not(w)) == True:
                    print(z, y, x, w)
z y x w
0 1 0 0
1 0 1 0
0 1 1 0
'''
#2_23548
'''
print('w y x z')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if (((x or y) <= z) or (y == w) or z) == False:
                    print(w, y, x, z)
w y x z
0 1 0 0
1 0 1 0
0 1 1 0
'''
#2_23361
'''
print('z x w y')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if (not(y <= (x == z)) and (w <= x)) == True:
                    print(z, x, w, y)
z x w y
1 0 0 1
0 1 0 1
0 1 1 1
'''
#2_23261
'''
print('y x w z')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if (not(w <= ( x == y )) and (z <= x)) == True:
                    print(y,x,w,z)
y x w z
1 0 1 0
0 1 1 0
0 1 1 1
'''
#5_23551
'''
result = []
for N in range(1,100):
    Rs = bin(N)[2:]

    if N % 2 == 0:
        Rs = '10' + Rs
    else:
        Rs = '1' + Rs + '01'

    R = int(Rs, 2)

    if R < 30:
        result.append(N)
if result:
    print(max(result)) # 6
'''
#5_25344 
'''
def to_3(n):
    s = ''
    while n > 0:
        s = str(n % 3) + s
        n //= 3
    return s

res_r = []
for n in range(1, 1000):
    s3 = to_3(n)
    
    if n % 3 == 0:
        s3 = s3 + s3[-2:]
    else:
        sum_digits = sum(int(d) for d in s3)
        add = to_3(sum_digits * 3)
        s3 = s3 + add
        
    r = int(s3, 3)
    
    if r > 208 and r % 2 != 0:
        res_r.append(r)

print(min(res_r)) # 243
'''
#5_25138 
'''
result = []
for N in range(10000, 100000):
    s = str(N)
    digi = [int(b) for b in s]
    
    S = sum(digi)
    M = max(digi) + min(digi)
    L = int(s[0])
    R = int(s[-1])
    
    p1 = S - L
    p2 = M - R
    
    parts = sorted([p1, p2])
    
    z = str(parts[0]) + str(parts[1])
    
    if z == '222':
        result.append(N)

if result:
    print(max(result)) #99607
''' 
