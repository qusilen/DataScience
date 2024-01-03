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



########################
#break - continue - while
########################
#break: aranan koşul sağlandığında döngünün durmasını sağlar.
salaries = [1000, 2000, 3000, 4000, 5000]
for salary in salaries:
    if salary == 3000:
        break
    print(salary)


#continue: aranan koşul sağlandığında bu koşulu atma ve devam et.
salaries = [1000, 2000, 3000, 4000, 5000]
for salary in salaries:
    if salary == 3000:
        continue
    print(salary)


#while: koşul doğru olduğu sürece çalış.
number = 1
while number < 5:
    print(number)
    number += 1

########################
#Enumerate: Otomatik Counter / Indexer ile for loop
########################
students = ["John", "Mark", "Vanessa", "Mariam"]
for student in students:
    print(student)

for index, student in enumerate(students): #enumerate(students, 1) indexler 1'den başlar.
    print(index, student)


A = []
B = []
for index, student in enumerate(students):
    if index % 2 == 0:
        A.append(student)

    else:
        B.append(student)


########################
#alternating fonksiyonunun enumerate ile yazılması (çift index büyük / tek index küçük) (project1)
########################
def alternating_with_enumerate(string):
    new_string = ""
    for i, letter in enumerate(string):
        if i % 2 == 0:
            new_string += letter.upper()
        else:
            new_string += letter.lower()
    print(new_string)

alternating_with_enumerate("hi my name is john and i am learing python")


########################
#Zip: birbirinden farklı listeleri bir arada değerlendirme imkanı sağlar
########################
students = ["John", "Mark", "Vanessa", "Mariam"]
departments = ["mathematics", "statistics", "physics", "astronomy"]
ages = [23, 30, 26, 22]

list(zip(students, departments, ages))
#bir liste içinde tuple formunda bu 3 listeyi birleştirdi.


########################
#lambda / map / filter / reduce
########################


#lambda: kullan at bir fonksiyondur.
def summer(a, b):
    return a + b

new_sum = lambda a, b: a + b
new_sum(2, 5)


#map: seni döngü yazmaktan kurtarırım.
salaries = [1000, 2000, 3000, 4000, 5000]
def new_salary(x):
    return x * 20 / 100 + x

new_salary(5000)

for salary in salaries:
    print(new_salary(salary))


list(map(new_salary, salaries)) #girilen fonksiyonu, girilen nesneye mapledi.

#del new_sum #(new_sum fonksiyonunu sildik)

list(map(lambda x: x * 20 / 100 + x, salaries))

list(map(lambda x: x ** 2, salaries))


#filter: filtreleme işlemleri için kullanılır.
list_store = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list(filter(lambda x: x % 2 == 0, list_store))


#reduce: indirgemek
from functools import reduce
list_store = [1, 2, 3, 4]
reduce(lambda a, b: a + b, list_store)