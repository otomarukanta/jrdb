start = 10
length = 6
repeat = 306

a = 1
b = 2

for i in range(repeat):
    name = "odds_{:02d}_{:02d}".format(a, b)
    print('        {{"start": {:3d}, "end": {:3d}, "type": "string", "name": "{}"}},'.format(
        start, start+length, name))
    start += length

    if b == 18:
        a += 1
        b = 1
    else:
        b += 1

    if a == b:
        b += 1
