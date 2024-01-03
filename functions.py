#qusi
########################
#Fonksiyonlar (Functions)
########################
#Belirli bir görevi yerine getirmek için yazılan kod parçalarıdır.

?print #fonksiyonun dokümantasyonunu verir.
help(print) # dokümantasyon

########################
#Fonksiyon Tanımlama
########################
def calculate(x):
    print(x * 2)


calculate(5)


#iki argümanlı/parametreli fonksiyon
def summer(arg1, arg2): #argüman sıralaması önemli!!
    print(arg1 + arg2)


summer(4, 6)


########################
#Docstring
########################
def summer(arg1, arg2):
    # 3" girince numpy otomatik docstring yazıyor.
    """
    Sum of two numbers

    :param arg1: int, float
    :param arg2: int, float

    :return:
        int, float

    :example:
    :note:
    """
    print(arg1 + arg2)

?summer

summer(1,4)


########################
#Fonksiyonların Statement/Body Bölümü
########################
#def function_name(parameters/arguments):
    #statements (function body)

def say_hi(string):
    """
    :param string: str

    :return:
    """
    print(string)
    print("Hi")
    print("Hello")

say_hi("esra")


#Girilen değerleri çarpıp bir liste içinde saklayacak fonksiyon.

list_store = [] #global değişken list_store
#global etki alanı

def add_element(a, b):
    #local etki alanı
    c = a * b #local değişken c
    list_store.append(c)
    print(list_store)


add_element(1,8)
add_element(24,676)


########################
#Ön Tanımlı Argünamnlar/Parametreler (Default Parameters/Arguments)
########################

def divides(a, b = 1):
    print(a / b)


divides(3)


########################
#Ne zaman fonksiyon yazma ihtiyacımız olur?
########################
#DRY (Don't Repeat Yourself)
#varm, moisture, change
(12 / 3) + 3
(45 / 5) + 4
(24 / 2) + 8

def calculate(varm, moisture, change):
    print((varm / moisture) + change)


calculate(24,2,8)

########################
#Return
########################

def calculate(varm, moisture, change):
    return (varm / moisture) + change


calculate(22,2,2) *2


########################
#Fonksiyon İçinde Fonksiyon Çağırmak
########################

def calculate(varm, moisture, change):
    return (varm / moisture) + change

def standardization(a, p):
    return a * 10 / 100 * p * p


def all_calculation(varm, moisture, change, p):
    a = calculate(varm, moisture, change)
    b = standardization(a, p)
    print(b * 10)

all_calculation(24,2,2,2)


########################
#Local (Local Scope) ve Global (Global Scope) Değişkenler
########################
#yukarıda listeye ekleme kısmında yazdım.
#Global Scope: Global etki alanında olan bir değişkendir ve programın herhangi bir bölümünden erişilebilir.
#Local Scope: Bir değişkenin veya fonksiyonun local etki alan tanımlandığı yerde veya daha özel bir kapsam içinde erişilebilir olduğu alandır.


