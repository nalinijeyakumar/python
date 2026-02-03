# def can_drive(age,has_license):
#     status = age >=18 and has_license == True
#     print("Can drive:",status)


# can_drive(11,True)


# def login(username,pwd):
#     status = username == "admin" and pwd == "1234"
#     print("Login successful:", status)


# login("admin","1234")

# def offer(age,student_id):
#     eligible = age <= 25 and student_id #its boolean check only no need to check again
#     print("Eligible for offer:", eligible)


# offer(25,True)


##Number divisible by 3 and 5

def check(value):
    no_val  = value%3 == 0 and value%5 == 0
    print("Number is divisible by 3 and 5:", no_val)


check(10)

##candidate age limit 21-32

def agecheck(age):
    age_check = age>=21 and age<=32
    print("User is eligibile for interview:",age_check)


agecheck(21)

##day falls on week end
def weekend(input_day):
    input_day = input_day.lower()
    day_check = input_day == "saturday" or input_day == "sunday"
    print("Entered day falls on weekend:",day_check)


weekend("Sunday")

##primay color check
def primarycol(input):
    input = input.upper()
    color_check = input=="RED" or input == "GREEN" or input == "BLUE"
    print("Enter color is a primay color:",color_check)


primarycol("red")