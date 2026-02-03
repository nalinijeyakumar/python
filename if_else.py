# # def num_check(x):
# #     if x==0:
# #         print("ZERO")
# #     elif x>0:
# #         print("Positive")
# #     else:    
# #         print("Negative")


# # num_check(5)
# # num_check(0)
# # num_check(-2)

# # def day_converter(num):
# #     if num==1:
# #         print("Monday")
# #     elif num==2:
# #         print("Tuesday")
# #     elif num == 3:
# #         print("Wednesday")
# #     elif num==4:
# #         print("Thursday")
# #     elif num==5:
# #         print("Friday")
# #     elif num==6:
# #         print("saturday")
# #     elif num==7:
# #         print("Sunday")
# #     else:
# #         print("Enter valid input")

# # day_converter(1)
# # day_converter(8)
# # day_converter(0)

# ##compute Indian income tax rate 
# def rate_compute(salary):
#     if salary >=4 and salary<8:
#         print("Income tax rate:",5,"%")
#     elif salary >=8 and salary<12:
#         print("Income tax rate:",10,"%")
#     elif salary >=12 and salary<16:
#         print("income tax rate:",15,"%")
#     elif salary >=16 and salary<20:
#         print("Income tax rate:",20,"%")
#     elif salary >=20 and salary<24:
#         print("Income tax rate:",25,"%")
#     elif salary >=24:
#         print("Income tax rate:",30,"%")
#     else:
#         print("No tax")

# rate_compute(1)
# rate_compute(25)
# rate_compute(13)

# ##Metal name and their price

# def metal_price(metal_name):
#     metal_name = metal_name.lower()
#     if metal_name =="gold":
#         print("Gold price:",12000)
#     elif metal_name =="silver":
#         print("Silver price:",300)
#     elif metal_name =="platinum":
#         print("Platinum price:",13000)
#     else:
#         print("Enter valid metal Name")

# metal_price("Gold")
# metal_price("SILVER")
# metal_price("platinum")
# metal_price("diamond")

# ##give no odd double it else return same no

# def check_no(value):
#     if(value%2 ==0):
#         value_a = value*2
#         print(value_a)
#     else:
#         print(value)

# check_no(6)
# check_no(3)

# ##find min no between two numbers
def find_min(a,b):
        c=a<b
        if (c):
            print(a,"is smaller")
        else:
            print(b,"is smaller")
find_min(3,5)
find_min(3,3)
find_min(8,0)
c=None
if c: ##Truthy values - True or False
    print("True")
else:
    print("False")

##find max no between two numbers

def find_max(a,b):
     c = a>b
     if(c):
          print(a,"is greater")
     else:
          print(b,"is greater")


find_max(0,2)
find_max(3,5)
find_max(10,3)

##pass score 36 find pass or fail
def exam_result(mark):
    if(mark>=36):
        print("Pass")
    else:
        print("Fail")


exam_result(50)
exam_result(25)


###Find given number positive,negative or zero
def no_check(value1):
    if(value1>0):
         print("Positive")
    elif(value1==0):
        print("Zero")
    else:
         print("Negative")
        

no_check(9)
no_check(0)
no_check(-10)

##Toom termperature - Normal,Hot or Cold
def room_temp(temp1):
    if(temp1>=24):
        print("Hot")
    elif(temp1<21):
        print("Cold") 
    else:
         print("Normal")


room_temp(23)
room_temp(19)
room_temp(32)



