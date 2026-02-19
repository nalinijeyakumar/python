# filename_test = r"C:\Users\nalini.j\OneDrive - ascendion\Desktop\Python\Test.txt"

# file_open = open(filename_test,"r")
# file_read = file_open.readline()
# while file_read != "":
#     print(file_read)
#     file_read = file_open.readline()

# file_open.close()

#print(file_read)
#print(file_read2)


file_test = open(r"C:\Users\nalini.j\OneDrive - ascendion\Desktop\Python\Filehandling_Input.txt","r")
file_output = open(r"C:\Users\nalini.j\OneDrive - ascendion\Desktop\Python\Filehandling_Output1.txt","w")
line = file_test.readline()
while line != "":

    file_output.write(line)
    line = file_test.readline()
    
    
file_test.close()
file_output.close()
    
# while True:
#     line = file.readline()
#     if(line != ""):
#         print(line)
#     else:
#         break