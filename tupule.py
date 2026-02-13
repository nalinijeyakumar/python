data = ("John", "Chennai", 40, 60, 50)

sliced_data = data[2:5:1]

total = sum(sliced_data)
avg = total/len(sliced_data)
max_no = max(sliced_data)
print(total)
print(avg)
print(max_no)

#un packing
a,b,c = (10,20,30)
