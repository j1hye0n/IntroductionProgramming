# do exercise 4, page 32A using fibonacci algo

def step(n):
    if n<=1:
        return 1
    else :
        return step(n-1)+step(n-2)
x=int(input())
print(step(x))