#qusi
########################
#Python ile Veri Analizi (Data Analysis with Python)
########################
#NumPy: Matematiksel İşlemler
#Pandas: Veri Analizi
#Veri Görselleştirme: Matplotlib(Low Level) & Seaborn(High Level)
#Gelişmiş Fonksiyonel Keşifçi Veri Analizi (Advanced Functional Exploratory Data Analysis)


########################
#NumPy (Numerical Python)
########################
#Bilimsel hesaplamalar için kullanılır.
#Arrayler ve Matrisler üzerinde yüksek performanslı çalışma imkanı sağlar.
#Verimli veri saklama imkanı sağlar.
#Daha az çabayla daha fazla işlem yapabilme imkanı sağlar.

import numpy as np
a = [1, 2, 3, 4]
b = [1, 2, 3, 4]

ab = []

for i in range(0, len(a)):
    ab.append(a[i] * b[i])

#bu işlem numpy ile bu şekilde yapılır:
a = np.array([1, 2, 3, 4])
b = np.array([1, 2, 3, 4])

a * b
#Yani listelere göre hızlı


########################
#NumPy Array'i Oluşturmak (Creating Numpy Arrays)
########################
import numpy as np
np.array([1, 2, 3, 4, 5])
type(np.array([1, 2, 3, 4, 5]))

np.zeros(10, dtype=int)

np.random.randint(0,10,size=10)

np.random.normal(10, 4, (3, 4))


########################
#NumPy Array Özellikleri (Attibutes of NumPy Arrays)
########################
import numpy as np

#ndim: boyut sayısı
#shape: boyut bilgisi
#size: toplam eleman sayısı
#dytpe: veri tiği bilgisi

a = np.random.randint(10, size=5)
a.ndim
a.shape
a.size
a.dtype


########################
#Yeniden Şekillendirme (Reshapeing)
########################
import numpy as np

np.random.randint(1, 10, size=9)
np.random.randint(1, 10, size=9).reshape(3, 3) #10 elemanlı olsaydı bunu 3'e 3'lük bir arraye çeviremezdi. Hata alırdık.

ar = np.random.randint(1, 10, size=9)
ar.reshape(3, 3)


########################
#İndex Seçimi (Index Selection)
########################
import numpy as np

a = np.random.randint(10, size=10)
a[0] #index selection
a[0:5] #sliceing

a[0] = 999

m = np.random.randint(10, size=(3,5))
m[0, 0]
m[1, 1]
m[2, 3] = 34
m[2, 3] = 3.2 #inte dönüştürür çüntü arrayin belirli bir dtypeı vardır.

m[:,0]
m[1, :]
m[0:2, 0:3]


########################
#Fancy Index
########################
import numpy as np

v = np.arange(0, 30, 3)
v[1]
v[4]

catch = [1, 2, 3]
v[catch]


########################
#NumPy'da Koşullu İşlemler (Conditions on NumPy)
########################
import numpy as np

v = np.array([1, 2, 3, 4, 5])
#array içindeki elemanların 3'ten küçük olanlara erişmek istiyoruz.

#klasik bir döngü ile:
ab = []
for i in v:
    if i < 3:
        ab.append(i)

#NumPy ile:
v < 3
v[v < 3]


########################
#NumPy'da Matematiksel İşlemler (Mathematical Operations)
########################
import numpy as np
v = np.array([1, 2, 3, 4, 5])

v / 5
v * 5 / 10
v ** 2
v - 1

np.subtract(v, 1) #çıkarma
np.add(v, 1) #toplama
np.mean(v) #ortalama
np.sum(v) #toplam alma
np.min(v) #minimum
np.max(v) #maksimum
np.var(v) #varyans


########################
#NumPy ile İki Bilinmeyenli Denklem Çözümü
########################
#5*x0 + x1 = 12
#x0 + 3*x1 = 10

a = np.array([[5, 1], [1, 3]]) #1. elemanlar = 1. değişkenin katsayıları / 2. elemanlar = 2. değişkenin katsayıları
b = np.array([12, 10]) #sonuçlar

np.linalg.solve(a, b)
