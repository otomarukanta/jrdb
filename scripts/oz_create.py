start = 10
length = 5
repeat = 18

a = 1

for i in range(repeat):
    name = "win_odds_{:02d}".format(a)
    print('        {{"start": {:3d}, "end": {:3d}, "type": "string", "name": "{}"}},'.format(
        start, start+length, name))
    start += length
    a += 1

a = 1
for i in range(repeat):
    name = "show_odds_{:02d}".format(a)
    print('        {{"start": {:3d}, "end": {:3d}, "type": "string", "name": "{}"}},'.format(
        start, start+length, name))
    start += length
    a += 1

a = 1
b = 2
for i in range(153):
    name = "quinella_odds_{:02d}_{:02d}".format(a, b)
    print('        {{"start": {:3d}, "end": {:3d}, "type": "string", "name": "{}"}},'.format(
        start, start+length, name))
    start += length
    if b == 18:
        a += 1
        b = a + 1
    else:
        b += 1
