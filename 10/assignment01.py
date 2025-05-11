# 가위바위보 게임

try:
    st=["가위","바위","보"]
    mine, your = map(str,(input(), input()))

    id=st.index(mine)
    s=st[id-1]+" "+st[id]+" "+st[id-2]
    st_=list(s.split())

    if st_.index(your)==2 :
        print("패배")
    elif st_.index(your)==1 :
        print("무승부")
    elif st_.index(your)==0 :
        print("승리")
except :
    raise ValueError