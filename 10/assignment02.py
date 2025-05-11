# 덧셈기

def add() :
    while True :
        try :
            a,b = map(int,input().split(" "))
            if type(a)==type(b)==int :
                print(a+b)
                break
        except :
            pass
add()
