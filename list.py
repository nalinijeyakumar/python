# numbers = [10,20,30,40]

# for i in numbers:
#     print(i)
# # # print(dir(numbers))

# # # LIST

# # # ADD
# # # - append
# # # - insert
# # # - extend

# # # DELETE
# # # - pop
# # # - remove
# # # - clear

# # # RE-ORDER
# # # - reverse
# # # - sort

# # fruits = ["apple","banana","orange"]
# # fruits.append("strawberry")


# # fruits.insert(7,"strawberry")


# # fruits.extend([1,2,3])


# # fruits.remove("strawberry")

# # fruits.pop()
# # # fruits.clear()
# # # fruits.remove("papaya")


# # # fruits[0] = "strawberry"
# # # print(fruits)

# # list_no = [167,212,3,44,500]
# # list_no.reverse()
# # print(list_no)

# # list_no.sort(reverse=True) 
# # print(list_no)

# list_a = [1,2,3,4,5]

# for i in range(0,len(list_a),1):
#     list_a[i]=list_a[i]*2
   
# #    print(i*2)

# # print(list_a)

# list_b = [1,2,3]
# list_c = []
# size = len(list_b)-1
# for i in range(size,-1,-1):
#     x = list_b[i]
#     list_c.append(x)
# print(list_c)

# # list_c.clear()

# # for i in range(0,len(list_b),1):
# #     x = list_b.pop()
# #     list_c.append(x)
# # print(list_c)

# #double them in places
# given_numbers = [1,2,3,4,5]

# for i in range(0,len(given_numbers),1):
#     given_numbers[i]=given_numbers[i]*2
# print(given_numbers)

# #sort nos
# original_order = [5,1,10,3,55]
# for i in range(0,len(original_order)-1,1):
#     temp = original_order[i]
#     if (original_order[i] > original_order[i+1]):
#         original_order[i] = original_order[i+1]
#         original_order[i+1] = temp

# print(original_order)

# #rotate them in place
list_order = [1,2,3,4,5]
size = len(list_order)
def rotate_number():
    temp = list_order[size-1] 
    for i in range(size-1,0,-1):
           
        list_order[i] = list_order[i-1]
        list_order[i-1] = list_order[0]
    list_order[0] = temp
rotate_number()
print(list_order)