#qusi
########################
#Pandas
########################

#Veri manipülasyonu ya da veri analizi denildiğinde akla gelen ilk Python kütüphanelerinden biridir.

########################
#Pandas Series
########################
#tek boyutludur ve index bilgisi barındır.
import pandas as pd

s = pd.Series([10, 77, 12, 4, 5])
type(s)

s.index
s.dtype
s.size
s.ndim
s.values
type(s.values)
s.head(3)
s.tail(3)


########################
#Veri Okuma (Reading Data)
########################
#Amaç: Bilgisayardaki .cvs uzantılı dosyayı okumak.
import pandas as pd
df = pd.read_csv("dosyanın_dizin_bilgisi")
df.head()
#ctrl + ilgili pd ordandan da ctrl + fonkisyona tıklarsak fonksiyonun dokümantasyonuna ulaşılır.


########################
#Veriye Hızlı Bakış (Quick Look at Data)
########################
import pandas as pd
import seaborn as sns

sns.load_dataset("titanic")
df.head()
#titanic kazası esnasında yolcuların hayatta kalıp kalmadığı bilgisini veren bir veri setidir.
#survived değişkeni bu data setinin ana odağıdır. Bağımlı değişkenidir.
#survived: 1 => yolcu hayatta kalmış
#survived: 0 => yolcu hayatını kaybetmiş

df.tail()
df.shape #satır sütun bilgisi verir
df.info() #değişkenler ve tiplerini verir (dolu gözlem bilgisi)
#kategorik değişkenler: object, category
df.colums #değişkenlerin isimlerini verir
df.index #index bilgisi
df.describe().T #değişkenlerin istatistikleri
#.T: transpozunu alır. (daha okunabilir hale gelir.)
df.isnull().values.any() #null değeri var mı
df.isnull().sum() #her bir değişkende kaç tane null var bilgisini verir
df["sex"].head()
df["sex"].value_counts() #kategorik değişken içindeki sınıfları ve bunlardan data setinde kaçar adet bulubduğu bilgisini verir


########################
#Pandas Seçim İşlemleri (Selection in Pandas)
########################
import pandas as pd
import seaborn as sns

df = sns.load_dataset("titanic")
df.head()

df.index
df[0:13]
df.drop(0, axis=0).head() #indexlerde silme işlemi (kalıcı olarak kaydetmedik)
#axis=0 => satırlar, axis=1 => sütunlar

delete_indexes = [1, 3, 5, 7]
df.drop(delete_indexes, axis=0).head(10)

#silme işlemi yukarıdakilerde kalıcı değildir.
#bu işlemi kalıcı olarak yapmak için:
#df = df.drop(delete_indexes, axis=0)
#df.drop(delete_indexes, axis=0, inplace=True) #inplace kalıcı olsun mu olmasın mı argünamıdır


########################
#Değişkeni İndexe Çevirmek
########################
df["age"].head()
df.age.head()

df.index = df["age"]
df.drop("age",axis=1).head()
df.drop("age",axis=1, inplace=True)
df.head()


########################
#İndexi Değişkene Çevirmek
########################
#1. Yol:
df.index
df["age"] = df.index #age adında bir sütun oluşturduk ve indexdeki değerleri içine atadık
df.head()
df.drop("age", axis=1, inplace=True)

#2. Yol:
df.reset_index().head() #indexde yer alan değeri siler. bunu sütun olarak (yeni bir değişken olarak) ekler.
df = df.reset_index()
df.head()


########################
#Değişkenler Üzerinde İşlemler
########################
import pandas as pd
import seaborn as sns

pd.set_option("display.max_columns", None) #aradaki gösterilmeyen columnlardan (üç noktalardan) kurtulma işlemi
df = sns.load_dataset("titanic")
df.head()

"age" in df #"age" değişkeni df data setinin içinde var mı
df["age"].head()
df.age.head()
type(df["age"].head()) #tek bir değişken seçince bu pandas series olur

#eğer data frame olarak kalmasını istiyorsak:
df[["age"]].head() #2 köşeli parantez
type(df[["age"]].head())

df[["age", "alive"]]

col_names = ["age", "adult_male", "alive"]
df[col_names]


df["age2"] = df["age"]**2 #yaşın karesi yeni bir değişken olarak data setine eklenmiş oldu
df["age3"] = df["age"] / df["age2"]


df.drop("age3", axis=1).head() #değişken silme işlemi


col_names = ["age", "adult_male", "alive"]
df.drop(col_names, axis=1).head() #birden fazla değişken silme işlemi


#veri setinde belirli bir ifadeyi barındıran değişkenleri silmek istiyoruz:
#age, age1, age2,... gibi
df.loc[:, df.column.str.contains("age")] #içinde "age" ifadesi barındıran satırları seçti
#loc: dflerde seçme işlemleri için kullanılan özel yapıdır
#str: string operasyonu yapıcam
#contains: stringin içinde verdiğin string var mı yok mu bakayım

df.loc[:, ~df.column.str.contains("age")]  #~: dediğimin dışındakilerini seç (değildir)
#yani yaşla ilgili tüm değişkenleri seçmi olduk


########################
#iloc & loc
########################
#data framelerde seçim işlemi yapmak için kullanılır.
#iloc: integer base selection
df.iloc[0:3]
df.iloc[0, 0]
#loc: label base selection (isimlendirmenin kendisini seçer.)
df.loc[0:3]

df.iloc[0:3, "age"] #hatalı index isyitor bizden
df.loc[0:3, "age"]

col_names = ["age", "embarked", "alive"]
df.loc[0:3, col_names]


########################
#Koşullu Seçim (Conditional Selection)
########################
import pandas as pd
import seaborn as sns
pd.set_option("display.max_columns", None)
df = sns.load_dataset("titanic")
df.head()

df[df["age"] > 50].head()
df[df["age"] > 50].count() #yaşı 50den büyük kaç kişi var
df[df["age"] > 50]["age"].count()

df.loc[df["age"] > 50, "class"].head()
df.loc[df["age"] > 50, ["age", "class"].head()
df.loc[(df["age"] > 50) & (df["sex"] == "male"), ["age", "class"].head()
df.loc[(df["age"] > 50)
       & (df["sex"] == "male")
       & (df["embark_town"] == "Cherbourg"),
       ["age", "class", "embark_town"].head()

df.loc[(df["age"] > 50)
       & (df["sex"] == "male")
       & ((df["embark_town"] == "Cherbourg") | df["embark_town"] == "Southampton")),
       ["age", "class", "embark_town"].head()


########################
#Toplulaştırma ve Gruplama (Aggregation & Grouping)
########################
#Toplulaştırma: bir veri yapısının içindeki verileri topu bir şekilde ifade etmek.
# count()
# first()
# last()
# mean()
# median()
# min()
# max()
# std()
# var()
# sum()
# pivot lable

import pandas as pd
import seaborn as sns

pd.set_option("display.max_coulmns", None)
df = sns.load_dataset("titanic")
df.head()

df["age"].mean()

df.groupby("sex")["age"].mean() #df değişkenini "sex değişkenine göre grupla yaşlarının ortalamasını al"
df.groupby("sex").agg({"age" : "mean"}) #aynı işlemi yapar. (buna alışsan daha iyi)
df.groupby("sex").agg({"age" : ["mean", "sum"]})
df.groupby("sex").agg({"age" : ["mean", "sum"],
                       "survived" : "mean"})
df.groupby(["sex", "embark_town"]).agg({"age" : ["mean"],
                       "survived" : "mean"})


########################
#Pivot Table
########################
#Groupby işlemlerine benzer şekilde veri setini kırılımlar açısından değerlendirmek ve ilgilendiğimiz özet istatistiği bu kırılımlar üzerinden görmemizi sağlar
import pandas as pd
import seaborn as sns

pd.set_option("display.max_coulmns", None)
df = sns.load_dataset("titanic")
df.head()

df.pivot_table("survived", "sex", "embarked") #kesişimler, index(satır), sütun
#kesişimlerin default tanımı meandir. (ortalama)
df.pivot_table("survived", "sex", "embarked", aggfunc="std")
df.pivot_table("survived", "sex", ["embarked", "class"]) #sütunlarda 2 index oldu

df["new_age"] = pd.cut(df["age"], [0, 10, 18, 25, 40, 90]) #sayısal değişkeni kategorik değişkene çevirir
#ayıracağımız kategorileri tnımlayabiliyorsak cut, tanımlayamıyorsak qcut kullanılır.

df.pivot_table("survived", "sex", "new_age")
df.pivot_table("survived", "sex", ["new_age", "class"])

pd.set_option("display_width", 500) #çıktıyı yanyana ne kadar alanda yazılsın


########################
#Apply & Lambda
########################
import pandas as pd
import seaborn as sns

pd.set_option("display.max_coulmns", None)
pd.set_option("display.width", 500)
df = sns.load_dataset("titanic")
df.head()

#apply: satır ya da sütunlarda otomatik olarak fonksiyon çalıştırma imkanı sağlar.
#lambda: kullan at fonksiyon

df["age2"] = df["age"] * 2
df["age3"] = df["age"] * 5

(df["age"] / 10).head()
df["age2"] / 10
df["age3"] / 10

for col in df.columns:
    if "age" in col:
        #print((df[col] / 10).head())
        df[col] = df[col] / 10


#bu işlem apply ve lambda kullanılarak şu şekilde yapılır:
df[["age", "age2", "age3"]].apply(lambda x: x / 10).head()

df.loc[:, df.colums.str.contains("age")].apply(lambda x: x / 10).head()


#standartlaştırma (normalleştirme) fonksiyonu
df.loc[:, df.colums.str.contains("age")].apply(lambda x: (x - x.mean()) / x.std()).head()


def standart_scaler(col_name):
    return (col_name - col_name.mean()) / col_name.std()

df.loc[:, df.colums.str.contains("age")].apply(standart_scaler).head()

df.loc[:, ["age", "age2", "age3"]] = df.loc[:, df.colums.str.contains("age")].apply(standart_scaler).head() #kaydetme işlemi
df.loc[:, df.colums.str.contains("age")] = df.loc[:, df.colums.str.contains("age")].apply(standart_scaler).head() #üsttekinin otomatik hali


########################
#Birleştirme İşlemleri
########################


########################
#Join
########################
import numpy as np
import pandas as pd
m = np.random.randint(1, 30, size=(5, 3))
df1 = pd.DataFrame(m, columns = ["var1", "var2", "var3"])
df2 = df1 + 99

pd.concat([df1, df2]) #dfleri birleştirir ama index bigisini olduğu gibi tutar
pd.concat([df1, df2], ignore_index = True) #bunu yapınca indexler 0dan başlar ve devam eder.

pd.concat([df1, df2], axis=1) #axis default olarak 0dır.(alt alta) bunu 1 yaparsak yanyana olacak şekilde birleştirir.


########################
#Merge
########################
df1 = pd.DataFrame({"employees": ["john", "dennis", "mark", "maria"],
                    "group": ["accounting", "engineering", "engineering", "hr"]})
df2 = pd.DataFrame({"employees": ["mark", "john", "dennis", "maria"],
                    "start_date": [2010, 2009, 2014, 2019]})

pd.merge(df1, df2)
pd.merge(df1, df2,on="employees")

#Amaç: Her çalışanın müdür bilgisine erişmek istiyoruz.
df3 = pd.merge(df1, df2)

df4 = pd.DataFrame({"group": ["accounting", "engineering", "hr"],
                    "manager": ["Caner", "Mustafa", "Berkcan"]})

pd.merge(df3, df4)  #groupa göre birleştirdik.