import pandas as pd
import numpy as np
from mlxtend.frequent_patterns import apriori, association_rules

#1 Loading data
df = pd.read_csv("GroceryStoreDataSet.csv", names = ['products'], sep = ',')
print(df.head())  #output l'erst 5 lines o'data

#2 Pre- data elab uz ablyi far utf algs o'search l'assoc'l rules
#2.1 Transform data set inti list
data = list(df["products"].apply(lambda x:x.split(",") ))
print(data)

#2.2 Transform list to table co kogic val (TRUE in fit'n col means es'i o'goodin concr basket)
from mlxtend.preprocessing import TransactionEncoder
a = TransactionEncoder()
a_data = a.fit(data).transform(data)
df = pd.DataFrame(a_data,columns=a.columns_)
df = df.replace(False,0)
print(df)

#3. Search l'assoc'l rules by help apriori alg
#3.1 search l'succs co support, no less than min
df = apriori(df, min_support = 0.2, use_colnames = True, verbose = 1)
print(df)
#3.2 Search l'assoc'l rules, icfit l'cond o'min true'i
df_ar = association_rules(df, metric = "confidence", min_threshold = 0.6)
print(df_ar)
