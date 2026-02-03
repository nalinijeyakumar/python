# def total(n):
#     i = 1
#     tot = 0
#     while i<=n:
#         tot = tot +i
#         i = i+1
        
#     return tot

# result = total(2)
# print(result)

# def add(x,y):
#     return x+y

# output = add(10,20)
# print(output)

def increment(x,y=1):
    return x+y

output = increment(10,20)
print(output)
output1 = increment(10)
print(output1)
output2 = increment(y=2,x=10)    
print(output2)
    