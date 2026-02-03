# Input
# Name, City, Math, Science, Language
# John, Chennai, 40, 60, 50
# Dave, Chennai, 34, 60, 50
# Steve, Bangalore, 34, 60, 50

# Expected Output
# Name, City, Math, Science, Language, Total, Average, Top Score
# John, Chennai, 40, 60, 50, 150, 50, 60
# Dave, Chennai, 34, 60, 50
# Steve, Bangalore, 34, 60, 50

data = "Name, City, Math, Science, Language \n John, Chennai, 100, 60, 50 \n Dave, Chennai, 34, 60, 50 \n Steve, Bangalore, 34, 60, 50"

# string
# - split \n
#   ignore first line
# - split by , -> 5 tokens or words
# process numerics, POS 2,3,4 []
# calculate sum, average, top
# add it back to the line
# using join / concatenation
# combine all lines

#print(data)
def gettockens(line):
    newline = line.split(",")
    values = newline[2:5:1]
    calculate_line = get_stat(values)
    result = line + "," + calculate_line
    return result

    

def get_stat(values):
    total = int(values[0]) + int(values[1]) + int(values[2])
    average = total/3
    top = max(int(values[0]),int(values[1]),int(values[2]))
    newline = ",".join([str(total),str(average),str(top)])
    return newline

 

def getline(source):
    lines = source.split("\n")  
    lines = lines[1:4:1]
    for i in lines:
        a = gettockens(i)
        print(a)
        #print (i)

getline(data)

