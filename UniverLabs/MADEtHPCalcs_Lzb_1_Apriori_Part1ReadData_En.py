import pandas as pd
import numpy as np
#from mlxtend.frequent_patterns import apriori, association_rules


df = pd.read_csv("GroceryStoreDataSet_CG.csv", names = ['products'], sep = ',')
print(df.head())  #output l'erst 5 lines o'data

#data = list(df["products"].apply(lambda x:x.split(",") ))
#print(data)

