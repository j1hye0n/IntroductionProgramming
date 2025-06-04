def ctrl_f(T,P):
    term = list(T)
    key = list(P)
    for i in range(len(term)-len(key)+1) :
        flag = 0
        for j in range(len(key)) :
            if key[j] == term[i+j] :
                flag +=1
        if flag == len(key) :
            return i
    return -1
            

## debug
#id =ctrl_f("HELLO WORLD","SS")
#print(id)