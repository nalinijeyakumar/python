def print_table(n):
    value=1
    while value<=10:
        # print(value*n)
       # print(str(n) +" x "+ str(value)+" = "+str(value*n))
        #print(n, " x ", value , " = ", (value*n))
        result = "{0} x {1} = {2}".format(n,value,n*value)
        print(result)
        value=value+1

print_table(2)