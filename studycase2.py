########################
#List Comprehensions
########################

########################
#Soru - 1
########################
########################
#NOT: Numerik olmayanların da isimleri büyümeli, tek bir list comp yapısı ile yapılmalı.
########################
import seaborn as sns
import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)

df = sns.load_dataset("car_crashes")
df.columns
df.info()

["NUM_" + col.upper() if df[col].dtype != "O" else col.upper() for col in df.columns]


########################
#Soru - 2
########################
[col.upper() + "_FLAG" if "no" not in col else col.upper() for col in df.columns]


########################
#Soru - 3
########################
og_list = ["abbrev", "no_privious"]
new_cols = [col for col in df.columns if col not in og_list]
new_df = df[new_cols]
new_df.head()


########################
#Soru - 4
########################
import numpy as np
import seaborn as sns
import pandas as pd

pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 1000)

df = sns.load_dataset("titanic")
df.head()
df.shape
#alt+shift+e
