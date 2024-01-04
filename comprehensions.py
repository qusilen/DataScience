#qusi
########################
#Comprehensions
########################

########################
#List Comprehensions
########################
salaries = [1000, 2000, 3000, 4000, 5000]

def new_salary(x):
    return x * 20 / 100 + x

for salary in salaries:
    print(new_salary(salary))


for salary in salaries:
    null_list.append(new_salary(salary))

null_list = []

for salary in salaries:
    if salary > 3000:
        null_list.append(new_salary(salary))
    else:
        null_list.append(new_salary(salary * 2))



[new_salary(salary * 2) if salary < 3000 else new_salary(salary) for salary in salaries]

[salary * 2 for salary in salaries]

[salary * 2 for salary in salaries if salary < 3000]

[salary * 2 if salary < 3000 else salary * 0 for salary in salaries ]

[new_salary(salary * 2) if salary < 3000 else new_salary(salary * 0.2) for salary in salaries ]


students = ["John", "Mark", "Venessa", "Mariam"]
students_no = ["John", "Venessa"]
[student.lower() if student in students_no else student.upper() for student in students]
[student.lower() if student not in students_no else student.upper() for student in students]


########################
#Dict Comprehensions
########################

dictionary = {"a": 1,
              "b": 2,
              "c": 3,
              "d": 4}

dictionary.keys()
dictionary.values()
dictionary.items()

{k: v ** 2 for (k, v) in dictionary.items()}
{k.upper(): v for (k, v) in dictionary.items()}
{k.upper(): v ** 2 for (k, v) in dictionary.items()}


########################
#List & Dict Comprehensions Uygulamaları
########################

########################
#Bir Veri Setindeki Değişken İsimlerini Değiştirmek
########################

#before:
#["total", "speeding", "alcohol", "not_distracted", "no_previos", "ins_premium", "ins_losses", "abbrev"]

#after:
#["TOTAL", "SPEEDING", "ALCOHOL", "NOT_DISTRACTED", "NO_PREVİOS", "INS_PREMIUM", "INS_LOSSES", "ABBREV"]

import seaborn as sns

df = sns.load_dataset("car_crashes")
df.columns

A = []

for col in df.columns:
    A.append(col.upper())

df.columns = A

df = sns.load_dataset("car_crashes")

df.columns = [col.upper() for col in df.columns]


########################
#İsminde "INS" olan değişkenlerin başında FLAG diğerlerin NO_FLAG eklemek istiyoruz.
########################

#before:
#['TOTAL',
# 'SPEEDING',
# 'ALCOHOL',
# 'NOT_DISTRACTED',
# 'NO_PREVIOUS',
# 'INS_PREMIUM',
# 'INS_LOSSES',
# 'ABBREV']

#after:
#['NO_FLAG_TOTAL',
# 'NO_FLAG_SPEEDING',
# 'NO_FLAG_ALCOHOL',
# 'NO_FLAG_NOT_DISTRACTED',
# 'NO_FLAG_NO_PREVIOUS',
# 'FLAG_INS_PREMIUM',
# 'FLAG_INS_LOSSES',
# 'NO_FLAG_ABBREV']

[col for col in df.columns]

["FLAG_" + col for col in df.columns if "INS" in col]

["FLAG_" + col  if "INS" in col else "NO_FLAG_" + col for col in df.columns]

df.columns = ["FLAG_" + col  if "INS" in col else "NO_FLAG_" + col for col in df.columns]


########################
#Amaç: key'i string, value'su aşağıdaki gibi bir liste olan sözlük oluşturmak.
#Sadece sayısal değişkenler için yapmak istiyoruz.
########################

#output:
#{'total': ['mean', 'min', 'max', 'sum'],
# 'speeding': ['mean', 'min', 'max', 'sum'],
# 'alcohol': ['mean', 'min', 'max', 'sum'],
# 'not_distracted': ['mean', 'min', 'max', 'sum'],
# 'no_previous': ['mean', 'min', 'max', 'sum'],
# 'ins_premium': ['mean', 'min', 'max', 'sum'],
# 'ins_losses': ['mean', 'min', 'max', 'sum']}

import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns

num_cols = [col for col in df.columns if df[col].dtype != "O"] #"O" ifadesi objecti (kategorik değişken) ifade eder.
soz = {}
agg_list = ["mean", "min", "max", "sum"]

for col in num_cols:
    soz[col] = agg_list

#kısa yolu
new_dict = {col : agg_list for col in num_cols}

df.head()

df[num_cols].head()

df[num_cols].agg(new_dict)
#agg foksiyonu: new_dict adında bir ifade (sözlük) gönderip num_cols'a (dataframe) uygularsak
#gönderdiğimiz sözlüğün içerisindeki değişkenler, girilen dataframe'de varsa (bizimkinde var)
#değişkenleri key bölümünden tutar, value bölümüne girilen bütün fonksiyonları gidip
#değişkenlere otomatik olarak uygular.

#           total    speeding  ...   ins_premium   ins_losses
#mean   15.790196    4.998196  ...    886.957647   134.493137
#min     5.900000    1.792000  ...    641.960000    82.750000
#max    23.900000    9.450000  ...   1301.520000   194.780000
#sum   805.300000  254.908000  ...  45234.840000  6859.150000