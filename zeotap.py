# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 18:36:40 2025

@author: SAGNIK GHOSHAL
"""

import pandas as pd
import matplotlib.pyplot as plt
cus=pd.read_csv("C:\\Users\SAGNIK GHOSHAL\Downloads\\Customers.csv")
prod=pd.read_csv("C:\\Users\SAGNIK GHOSHAL\Downloads\\Products.csv")
tran=pd.read_csv("C:\\Users\SAGNIK GHOSHAL\Downloads\\Transactions.csv")
df=tran.merge(cus,on="CustomerID",suffixes=["_Tran","_Cus"]).merge(prod,on="ProductID",suffixes=["_Tran","_Prod"])
print(df)
#df.to_csv("C:\\Users\SAGNIK GHOSHAL\Downloads\\Bussiness.csv")
df["TransactionDay"]=[i.split()[0].split('-')[2] for i in df["TransactionDate"]]
df["TransactionMonth"]=[i.split()[0].split('-')[1] for i in df["TransactionDate"]]
df["TransactionYear"]=[i.split()[0].split('-')[0] for i in df["TransactionDate"]]
df["TransactionTime"]=[i.split()[1].split(':')[0] for i in df["TransactionDate"]]
print(df.head())
df1=df.groupby(by=["TransactionMonth","Category"]).sum()
print(df1['TotalValue'])
cate=df["Category"].unique()
n=len(cate)
for i in range(n):
    plt.plot(sorted(df['TransactionMonth'].unique()),df1['TotalValue'][i::n],label=sorted(df["Category"].unique())[i])
plt.plot(sorted(df['TransactionMonth'].unique()),df.groupby(by=["TransactionMonth"]).sum()['TotalValue']/n,label="Average")
plt.xlabel('TransactionMonth')
plt.ylabel('TotalValue')
plt.legend()
plt.show()
plt.bar(sorted(df["TransactionTime"].unique()),df.groupby(by=["TransactionTime"]).sum()['TotalValue'])
plt.xlabel('TransactionTime')
plt.ylabel('TotalValue')
plt.show()
df["SignupDay"]=[i.split()[0].split('-')[2] for i in df["SignupDate"]]
df["SignupMonth"]=[i.split()[0].split('-')[1] for i in df["SignupDate"]]
df["SignupYear"]=[i.split()[0].split('-')[0] for i in df["SignupDate"]]
print(df.groupby(by=["SignupYear"]).count())
plt.bar(sorted(df['SignupYear'].unique()),df.groupby(by=["SignupYear"]).size())
plt.xlabel('SignupYear')
plt.ylabel('SignupUserCount')
plt.show()
df1=df.groupby(by=["SignupYear","Category"]).sum()
for i in range(n):
    plt.plot(sorted(df['SignupYear'].unique()),df1['TotalValue'][i::n],label=sorted(df["Category"].unique())[i])
plt.plot(sorted(df['SignupYear'].unique()),df.groupby(by=["SignupYear"]).sum()['TotalValue']/n,label="Average")
plt.xlabel('SignupYear')
plt.ylabel('TotalValue')
plt.legend()
plt.show()
plt.bar([i for i in cate],[df.where((df['SignupDate']>df['TransactionDate']) & (df['Category']==i)).dropna().size/df.where((df['SignupYear']=='2024') & (df['Category']==i)).dropna().size for i in cate])
plt.show()
