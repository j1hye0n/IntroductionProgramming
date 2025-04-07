def ReLU(x):
    if x>=0 :
        return x
    else :
        return 0.0

a=float(input("x="))
print(f'ReLU({a})={ReLU(a)}')