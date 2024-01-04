#qusi
########################
#Uygulama - Mülakat Sorusu
########################

#Amaç: çift sayıların karesi alınarak bir sözlüğe eklenmek istenmektedir.
#Keyler orijinal, valuelar değiştirilmiş değerler olacak.

numbers = range(10)
new_dict = {}

for n in numbers:
    if n % 2 == 0:
        new_dict[n] = n ** 2


#comprehensions
{n: n ** 2 for n in numbers if n % 2 == 0}