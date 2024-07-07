import pandas as pd
import numpy as np
df = pd.read_csv("Datasets/imdb.csv")
result = df
result = df.columns
result = df["Series_Title"]

result = df[["Series_Title","IMDB_Rating"]].tail(10)

result = df[:51][["Series_Title","IMDB_Rating"]].query("IMDB_Rating > 8.5")

df["Released_Year"] = pd.to_numeric(df["Released_Year"], errors='coerce')
result = df[(df["No_of_Votes"] > 100000) | ((df["IMDB_Rating"] <= 9) & (df["IMDB_Rating"] >= 8 ))][["Series_Title","No_of_Votes","IMDB_Rating"]]

# result = df.groupby("Genre")
# for name, group in result:
#     print(name)
#     print(group)
# result = df.groupby("Genre")[["No_of_Votes", "IMDB_Rating"]].mean()
# result = df.groupby("Genre")[["No_of_Votes", "IMDB_Rating"]].agg(["mean", "min", "max"])
#
# data = np.random.randint(10,100,15).reshape(5,3)
#
# df = pd.DataFrame(data, index=["A", "B", "C", "D" , "E"] ,columns = ["col1", "col2", "col3"])
# df = df.reindex(["A","X" ,"B","Y" ,"C", "D" , "E"])
# newColumn = [30,np.nan,62,np.nan,96,np.nan,np.nan]
# df["col4"] = newColumn
# result = df[df["col4"].isnull()].loc[:,"col1"]
#
# result = df.dropna(how="any", axis=0)
# result = df.dropna(how="all", axis=0)
# result = df.dropna(how="any", subset=["col3","col4"])
# result = df.dropna(thresh=4 )
#
# result = df.fillna(value="no input")

df["Series_Title"] = df["Series_Title"].str.upper()
result = df[(df["No_of_Votes"] > 100000) | ((df["IMDB_Rating"] <= 9) & (df["IMDB_Rating"] >= 8 ))][["Series_Title","No_of_Votes","IMDB_Rating"]]
df["index"] = df["Series_Title"].str.find("A")
result = df[["Series_Title","index"]].head(30)
result = df.Series_Title.str.contains("THE")
result = df[["Series_Title","index"]][result].head(30)
df.dropna(thresh=17,inplace=True)
df.IMDB_Rating = df.IMDB_Rating.astype(str)
df["IMDB_Rating"] = df.IMDB_Rating.str.replace(".",",")
result = df[["Series_Title","IMDB_Rating"]]
df[["integer", "fraction"]] = df["IMDB_Rating"].str.split(",", expand=True)
result = df[["Series_Title","IMDB_Rating","integer","fraction"]]

import pandas as pd

customers = {
    "customerId" : [1, 2, 3, 4],
    "firstName" : ["Ahmet", "Ali", "Hasan", "Canan"],
    "lastName" : ["abc", "def", "ghl", "snj"]
}

orders = {
    "orderId" : [10, 11, 12, 13],
    "customerId" : [1, 2, 5, 7],
    "orderDate" : ["2010-07-04", "2010-08-04", "2010-08-04", "2010-10-04"]
}

dfCustomers = pd.DataFrame(data=customers, columns=["customerId", "firstName", "lastName"])
dfOrders = pd.DataFrame(data=orders, columns=["orderId", "customerId", "orderDate"])

result = pd.merge(dfCustomers, dfOrders, how="inner")
result = pd.merge(dfCustomers, dfOrders, how="left")
result = pd.merge(dfCustomers, dfOrders, how="right")
result = pd.merge(dfCustomers, dfOrders, how="outer")

data= {
    "column1" : [1,2,3,4,5],
    "column2" : [10,20,13,21,15],
    "column3" : ["abc" , "bca", "ade" , "cba" , "dea"]
}
df = pd.DataFrame(data)
# result = df.pivot_table(index="column1", columns="column2", values="column3")
def square(a):
    return a * a
square2 = lambda x : x * x
result = df
result = df["column2"].unique()
result = df["column2"].nunique()
result = df["column2"].value_counts()
result = df["column2"].apply(square2)

result = df.info()
result = df.sort_values("column3", ascending=False)
print(result)
