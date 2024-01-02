#qusi 01.01.2024

########################
#Veri Yapıları (Data Structures)
########################

#Veri Yapıları: Programlama sürecindeki en küçük parçalar.

#Sayılar (Numbers): int, float, complex
x = 46 #integer
type(x)

x = 10.3 #float
type(x)

x = 2j + 1 #complex
type(x)

#Üstlerinde matematiksel ve mantıksal işlemler yapılabilir.


########################
#Tipleri Değiştirmek
########################

a = 3
b = 12.3
int(b)
float(a)
int(a * b / 10)

#################################################################################################################

#Karakter Dizileri (Strings): str
x = "Hello ai era"
type(x)

print("Esra")
print('Esra')
"Esra"
name = "Esra"

########################
#Çok Satırlı Karakter Dizileri
########################
long_str = """
E
S
R
A
"""

########################
#Karakter Dizilerinin Elemanlarına Erişmek
########################
name[0]

########################
#Karakter Dizilerinde Slice İşlemi
########################
name[0:2]

########################
#String İçerisinde Karakter Sorgulamak
########################
"E" in long_str
"e" in long_str

########################
#String (Karakter Dizisi) Metodları
########################
dir(int)
dir(str) #kullanılacak metodları listeler

#len: stringin uzunluğunu veren fonksiyon
#(build in funct.): gömülü hazır fonksiyon
len(name)
len("esra")

#Fonksiyonlar ve metodlar aynı şeylerdir. (görev itibariyle) farklılıkları:
#Not: Bir fonksiyon, class yapısı içerisinde tanımlandıysa buna metod denir.
#Class yapısı içerisinde değilse buna fonksiyon denir.

#upper() lower(): büyük - küçük dönüşümleri (bunlar metoddur (class içerisinde tanımlılar))
"esra".upper()
"ESRA".lower()

#replace: karakter değiştirmek için kullanılır.
hi = "Hello AI Era"
hi.replace("l", "p")

#split: böler
"Hello AI Era".split()

#Not: Metodlar ve fonksiyonlar ihtiyaçlara göre öğrenilmeli. (bkz. dir)

#################################################################################################################

#Boolean (TRUE-FALSE): bool
True
False
type(True)
5 == 3
4 == 5
1 == 1
type(3 == 2)

#################################################################################################################

#Liste (List)
    #Değiştirilebilir.
    #Sıralıdır. Index işlemleri yapılabilir.
    #Kapsayıcıdır.
x = ["btc", "eth", "xrp"]
type(x)

notes = [1, 2, 3, 4]
type(notes)

not_nam = [1, 2, 3, "a", "b", True, [1, 2, 3]]
type(not_nam)
not_nam[0]
not_nam[6][1]
type(not_nam[6])
type(not_nam[6][1])

notes[0] = 99
notes

not_nam[0:4]

########################
#Liste Metodları (List Method)
########################
dir(notes)

#append: sona ekleme
notes.append(100)
notes

#pop: indexe göre eleman siler
notes.pop(0)
notes

#insert: indexe ekler
notes.insert(2, 34)
notes

#################################################################################################################

#Sözlük (Dictionary)
    #Değiştirilebilir.
    #Sırasız. (3.7 sonrasında sıralı)
    #Kapsayıcı.
    #key-value
x = {"name": "Peter", "Age": 36} #"key": value
type(x)

dictionary = {"REG": "Regression",
              "LOG": "Logistic Regression",
              "CART": "Classification and Regression"}
dictionary["REG"]

dictionary_1 = {"REG": ["RMSE", 10],
                "LOG": ["MSE", 20],
                "CART": ["SSE", 30]}
dictionary_1["REG"]
dictionary_1["CART"][1]

dictionary_2 = {"REG": 10,
                "LOG": 20,
                "CART": 30}
dictionary_2["REG"]

########################
#Key Sorgulama
########################
"REG" in dictionary
"YSA" in dictionary

########################
#Key'e Göre Value'ya Erişmek
########################
dictionary["REG"]
dictionary.get("REG")

########################
#Value Değiştirmek
########################
dictionary["REG"] = ["YSA", 10]
dictionary

########################
#Tüm Keylere / Valuelara Erişmek
########################
dictionary.keys()
dictionary.values()

########################
#Tüm Çiftleri Tuple Halinde Listeye Çevirme
########################
dictionary.items()

########################
#Key-Value Değerini Güncellemek
########################
#Değer bulunuyorsa günceller. Bulunmuyorsa sözlüğe ekler.
dictionary.update({"REG": 11})
dictionary

dictionary.update({"RF": 10})
dictionary

#################################################################################################################

#Demet (Tuple)
    #Değiştirilemez. (Listeden farkı)
    #Sıralıdır.
    #Kapsayıcıdır. (Birden farklı veri yapısını tutabiliyor.)
    #Listelere benzer ama daha güvenli bir çalışma imkanı sağlar.
    #Kullanım sıklığı çok azdır.
x = ("python", "ml", "ds")
type(x)

t = ("john", "mark", 1, 2)
type(t)
t[0]
t[0:3]
t[0] = 99 #Değiştirilemez

t = list(t)#tuple'ı listeye dönüştürüp
t[0] = 99#elemanı değiştirip
t = tuple(t)#liste'yi tekrar tuple'a dönüştürebiliriz.

#################################################################################################################

#Set
    #Değiştirilebilir.
    #Sırasız + Eşsizdir.
    #Kapsayıcıdır.
    #Kümeler gibi düşünülebilir.
    #Kullanımı azdır.
x = {"python", "ml", "ds"}
type(x)

set1 = set([1, 3, 5])
set2 = set([1, 2, 3])
#set1'de olup set2'de olmayan kimler var?
set1.difference(set2)
set1 - set2
#set2'de olup set1'de olmayan kimler var?
set2.difference(set1)
set2 - set1
########################
#symmetric_difference(): İki kümede de birbirlerine göre olmayanlar.
########################
set1.symmetric_difference(set2)
set2.symmetric_difference(set1)

########################
#intersection(): İki kümenin kesişimi
########################
set1.intersection(set2)
set2.intersection(set1)
set1 & set2

########################
#union(): İki kümenin birleşimi
########################
set1.union(set2)
set2.union(set1)

########################
#isdisjoint(): İki kümenin kesişimi boş mu? ("is" ifadesi varsa kod True ya da False döndürür.)
########################
set1.isdisjoint(set2)
set2.isdisjoint(set1)

########################
#issubset(): Bir küme diğer kümenin alt kümesi mi?
########################
set1.issubset(set2)
set2.issubset(set1)

########################
#issuperset(): Bir küme diğer kümeyi kapsıyor mu?
########################
set1.issuperset(set2)
set2.issuperset(set1)

#################################################################################################################

#Not: liste, tuple, set, dictionary veri yapıları aynı zamanda Python Collections (Arrays) olarak geçmektedir.
