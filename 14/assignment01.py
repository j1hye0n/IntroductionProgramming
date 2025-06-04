def oper(num1,num2,num3,op1,op2) :
    if (op2=='*' or op2== '/') and (op1=='+' or op1=='-'):
        temp = cal(num2,num3,op2)
        return cal(num1,temp,op1)
    else :
        temp = cal(num1,num2,op1)
        return cal(temp,num3,op2)

def cal (num1,num2,op) :
    if op == '+' :
        return num1+num2
    elif op == '/':
        return num1/num2
    elif op == '*':
        return num1*num2
    elif op == '-' :
        return num1-num2
    else :
        return None
    
prefin = set()
def main (num_list,num_dict) :
    target = int(num_list[0])
    for i in range(1,len(num_list)) :
        #a_ = num_list[i]
        ##print(len(num_list[i]))     #debug
        ##num1 = int(a_[1]) if len(num_list[i])==2 else int(a_[1]+a_[2])     # fixed below
        #num1 = int(''.join(str(bbin) for bbin in a_[1:]))
        #print(f'first part : {num_dict.get(a_)} > num1 : {num1}') #debug
        a = num_list[i]
        num1 = int(a[1:])
        for j in range(1,len(num_list)) :
            if j!=i :
                #b = [ ch for ch in num_list[j]]
                #b_ = num_list[j]
                ##num2 = int(b[1]) if len(num_list[j])==2 else int(b[1]+b[2])    #fixed below
                #num2 = int(''.join(str(bbinb) for bbinb in b_[1:]))
                #print(f'second part : {num_dict.get(b_)} > num2 : {num2}')     #debug
                b = num_list[j]
                num2 =int(b[1:])
            else :
                continue
            for k in range(1,len(num_list)) :
                if k!= j and k!=i :
                    #c = [chs for chs in num_list[k]]
                    #c_ = num_list[k]
                    ##num3 = int(c[1]) if len(num_list[k])==2 else int(c[1]+c[2])    # fixed below
                    #num3 = int(''.join(str(bbinc) for bbinc in c_[1:]))
                    #print(f'third part : {num_dict.get(c_)} > num3 : {num3}')     #debug
                    c = num_list[k]
                    num3 = int(c[1:])
                else :
                    continue

                #step_result = oper(num1,num2,num3,b[0],c[0])

                #if (step_result == int(num_list[0])) :
                    #prefin.add(num_dict.get(a)+num_dict.get(b_)+num_dict.get(c_))
                    ##print(f"{num1}{b[0]}{num2}{c[0]}{num3}")
                    ##print(f"{a_}{b_}{c_} = {step_result} \n >> {num_dict.get(a_)}{num_dict.get(b_)}{num_dict.get(c_)}")      #debug
                step_result = oper(num1,num2,num3,b[0],c[0])
                if step_result==target:
                    prefin.add(num_dict.get(a)+num_dict.get(b)+num_dict.get(c))

    return prefin


# main code
num_list = []
for bbin in range(11) :
    line = input().strip()
    num_list.append(line)

#print(f"nume_list's length : {len(num_list)}")    #debug

num_dict = dict()
for i,v in enumerate(num_list) :
    num_dict[v] = chr(ord('@')+i)

#print(f'num_dict : {num_dict}')     #debug

temp = main(num_list,num_dict)
fin = "\n".join(sorted(temp, reverse=True))
print(f'{fin}')