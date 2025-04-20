word=input().strip().upper()
key=input().strip().upper()

word = word.replace(" ","").replace("'","")
key = key.replace(" ","").replace("'","")

if len(word) == len(key):
    if set(word) == set(key) :
        print("YES")
else :
    print("NO")