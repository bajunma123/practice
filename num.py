num = ['00', '00', '00', '00', '80', '10', '00', '00', '00']
repeat = raw_input('please input a int: ')

m = num * int(repeat)

t = dict(enumerate(m, start=1))
#print(len(t.keys()))
for a, b in t.items():
    #print(a, b)
    if a % 4 == 0:
        print(' '.join((t[a-3], t[a-2], t[a-1], t[a] + '\n')))
        k = a
#print(k)
if len(m) > k:
    print(' '.join(m[k:]))


