#task1
# def multip(a,b):
#     if(b==1):
#         return a
#     else:
#         return a+multip(a,b-1)
    
# print(multip(89,2))

#task2
# def sumdig(n):
#     cnt=0
#     if(n==0):
#         return 0
#     else :
#         cnt+=n%10
#         return cnt+sumdig(n//10)
    
# print(sumdig(156))

# task3
# def countdig(n):
#     cnt=0
#     if(n==0):
#         return 0
#     else:
#         n%10
#         cnt+=1
#         return cnt+countdig(n//10)
# print(countdig(1111))

#task4
def st(t):
    if len(t)==0:
        return ''
    else :
        return t[::-1]+st(0)
print(st('hello'))