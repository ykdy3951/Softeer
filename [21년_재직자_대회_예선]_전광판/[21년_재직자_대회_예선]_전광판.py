l = {
    -1: 0b0000000,
    0: 0b1110111,
    1: 0b0010010,
    2: 0b1011101,
    3: 0b1011011,
    4: 0b0111010,
    5: 0b1101011,
    6: 0b1101111,
    7: 0b1110010,
    8: 0b1111111,
    9: 0b1111011
}

for i in range(int(input())):
    x, y = input().split()
    x = list(map(int, list(x))); y = list(map(int, list(y)))
    x = [-1] * (5-len(x)) + x
    y = [-1] * (5-len(y)) + y

    cnt = 0
    for i in range(5):
        cnt += bin(l[x[i]] ^ l[y[i]])[2:].count('1')
    
    print(cnt)
