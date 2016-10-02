num = ['00', '00', '00', '00', '80', '10', '00', '00', '00']

method 1:

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

method 2:
m = num * 64
#we = [[m[a],m[a+1],m[a+2],m[a+3]] for a in range(len(m)) if a % 4 == 0]
we = [[m[a],m[a+1],m[a+2],m[a+3]] for a, _ in enumrate(m) if a % 4 == 0]
for i in we:
    for a in i:
        print(a, end=' ')
    print('\n')
    
    
    
     
