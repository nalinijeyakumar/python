# age_to_vote = 18
# user_age = 17
# can_vote = user_age >= age_to_vote

# print("Can user vote?",can_vote)

# def can_drive(user_age):
#     result = user_age >=18
#     print("Can user driver?",result)

# age = int( input("Enter user age:")) #str to int conversion method - 1
# age = int(age) #str to int conversion method - 2
# can_drive(int(age)) #str to int conversion method - 3
    

def mark_check(mark):
        result = mark >=36
        print("Student qualified in the subject:",result)

mark_check(30)

def mark_check(mark):
        result = mark ==100
        print("Student scored Centum:", result)

mark_check(90)

def login_auth(pwd):
        check = pwd == "1234"
        print("Authentication success:",check)

login_auth("1234")

def value_check(user_input):
        check = user_input >= 0
        print("Is entered value positive:",check)

value_check(int(0))


        




    


