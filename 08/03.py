# 메뉴 관리

me_dict=dict()
count = 0

while True :
    a = input()
    if a=="END" :
        break
    elif (" " in a) : 
        me_key, me_value = a.split(" ")
        me_dict[me_key] = int(me_value)
        continue
    else : 
        count += me_dict[a]

print(count)