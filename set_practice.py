work_week = {"Mon","Tues","Wed","Thurs","Fri"}
week_end = {"Sat","Sun"}

#union
days_week = work_week|week_end
print(days_week)

#difference
students_a = {"Alice","Bob","Charlie","David"}
Student_b = {"Bob","David","Eve","Frank"}

#who is only in Class A
print("Only A",students_a-Student_b)

#Who is in exactly one class
print("Exclusive",students_a ^ Student_b)

#who is in both classes
print("Both Classes",students_a & Student_b)

#who is atleast in one class
print("atleast in one class",students_a|Student_b)