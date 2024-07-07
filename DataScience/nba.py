import pandas as pd
import numpy as np
data = pd.read_csv("Datasets/Players.csv")
df = pd.DataFrame(data)
result = df.head(10)
result = df.shape[0]
result = df.columns
result = df["born"]
result = df["height"].mean()
result = df["height"].max()
result = df["Player"][df["height"] == df["height"].max()]
result = df.loc[df['height'] == df["height"].max()]["Player"]
result = df.loc[(df['born'] <= 1999) & (df['born'] >= 1995),["Player", "collage"]].dropna().sort_values(by='collage',ascending=False)
result = df.loc[df['Player'] == "Jake Bornheimer"]["birth_city"]
result = df.groupby("collage")["weight"].mean()
result = df["collage"].nunique()
result = df["collage"].dropna().unique().size
result = df.groupby("born")["Player"].nunique()
result = df.loc[df["Player"].str.contains("and", na=False),"Player"]

print(result)