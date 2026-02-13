filename_test = r"C:\Users\nalini.j\OneDrive - ascendion\Desktop\Python\Test.txt"

file_open = open(filename_test,"r")
file_read = file_open.readline()
while file_read != "":
    print(file_read)
    file_read = file_open.readline()

file_open.close()

#print(file_read)
#print(file_read2)