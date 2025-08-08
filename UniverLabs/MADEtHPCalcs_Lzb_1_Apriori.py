import pandas as pd
import numpy as np
from mlxtend.frequent_patterns import apriori, association_rules

#1 Завантаження даних
df = pd.read_csv("GroceryStoreDataSet.csv", names = ['products'], sep = ',')
print(df.head())  #виведення перших п'яти рядків даних

#2 Попередня обробка даних для можливості подальшого застосування алгоритмів пошуку асоціативних правил
#2.1 Перетворення набору даних на список
data = list(df["products"].apply(lambda x:x.split(",") ))
print(data)

#2.2 Перетворення списку на таблицю з логічними значеннями (TRUE у відповідному стовпці означає наявність товару у конкретному кошику)
from mlxtend.preprocessing import TransactionEncoder
a = TransactionEncoder()
a_data = a.fit(data).transform(data)
df = pd.DataFrame(a_data,columns=a.columns_)
df = df.replace(False,0)
print(df)

#3. Пошук асоціативних правил за допомогою алгоритму  apriori
#3.1 Пошук послідовностей з підтримкою, не нижчою за мінімальну
df = apriori(df, min_support = 0.2, use_colnames = True, verbose = 1)
print(df)
#3.2 Пошук асоціативних правил, що відповідають умові мінімальної достовірності
df_ar = association_rules(df, metric = "confidence", min_threshold = 0.6)
print(df_ar)
