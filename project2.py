#qusi
########################
# Uygulama - Mülakat Sorusu
########################

#divide_students fonksiyonu yazınız.
#Çift indexte yer alan öğrencileri bir listeye alınız.
#Tek indexte yer alan öğrencileri başka bir listeye alınız.
#Fakat bu iki liste tek bir liste olarak return olsun.

students = ["John", "Mark", "Vanessa", "Mariam"]
def divide_students(students):
    groups = [[], []]
    for index, student in enumerate(students):
        if index % 2 == 0:
            groups[0].append(student)
        else:
            groups[1].append(student)
    print(groups)
    return groups

st = divide_students(students)
st[0]
st[1]