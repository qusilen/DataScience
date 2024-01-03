#qusi
########################
#Conditions (Koşullar)
########################
#True-False
1 == 1 #True
1 == 2 #False

if 1 == 1:
    print("something")

if 1 == 2:
    print("something")

number = 11
if number == 11:
    print("True")


def number_check(number):
    if number == 10:
        print("number is 10")


number_check(10)
number_check(12)


def number_check(number):
    if number == 10:
        print("number is 10")

    else:
        print("number isn't 10")



number_check(12)


def number_check(number):
    if number > 10:
        print("number is greater than 10")

    elif number == 10:
        print("number is equal to 10")

    else:
        print("number is less than 10")

number_check(12)


########################
#Loops (Döngüler)
########################

#for loop
students = ["John", "Mark", "Venessa", "Mariam"]
for student in students:
    print(student)


salaries = [1000, 2000, 3000, 4000, 5000]
for salary in salaries:
    print(salary)

def new_salary(salary, rate):
    return int(salary * rate / 100 + salary)

new_salary(1500, 10)

for salary in salaries:
    print(new_salary(salary, 10))
