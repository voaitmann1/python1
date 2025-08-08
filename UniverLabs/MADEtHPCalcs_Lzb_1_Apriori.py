import pandas as pd
import numpy as np
from mlxtend.frequent_patterns import apriori, association_rules

#1 ������������ �����
df = pd.read_csv("GroceryStoreDataSet.csv", names = ['products'], sep = ',')
print(df.head())  #��������� ������ �'��� ����� �����

#2 ��������� ������� ����� ��� ��������� ���������� ������������ ��������� ������ ������������ ������
#2.1 ������������ ������ ����� �� ������
data = list(df["products"].apply(lambda x:x.split(",") ))
print(data)

#2.2 ������������ ������ �� ������� � �������� ���������� (TRUE � ���������� ������� ������ �������� ������ � ����������� ������)
from mlxtend.preprocessing import TransactionEncoder
a = TransactionEncoder()
a_data = a.fit(data).transform(data)
df = pd.DataFrame(a_data,columns=a.columns_)
df = df.replace(False,0)
print(df)

#3. ����� ������������ ������ �� ��������� ���������  apriori
#3.1 ����� ������������� � ���������, �� ������ �� ��������
df = apriori(df, min_support = 0.2, use_colnames = True, verbose = 1)
print(df)
#3.2 ����� ������������ ������, �� ���������� ���� �������� �����������
df_ar = association_rules(df, metric = "confidence", min_threshold = 0.6)
print(df_ar)
