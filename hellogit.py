from itertools import product

for i in range(5):
    for j in range(1,i+1):
        print('{}*{}={}'.format(i,j,i*j),end=' ')
    print()


