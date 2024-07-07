import pandas as pd

df = pd.read_csv("Datasets/GBvideos.csv")

result = df.head(10)
result = df.iloc[5:11]
result = df.columns
result = df.shape[1]

result = df.drop(['thumbnail_link', 'comments_disabled', 'ratings_disabled','video_error_or_removed', 'description'], axis=1)
result = df[["likes","dislikes"]].mean()

result = df.loc[:,["likes","dislikes"]].head(50)

result = df[df["views"] == df["views"].max()][["title","views"]]
result = df[df["views"] == df["views"].min()][["title","views"]].iloc[0]
result = df.sort_values(by='views',ascending=False)[["title","views"]].head(10)
result = df.groupby("category_id")["likes"].mean().sort_values()
result = df.groupby("category_id")["comment_count"].sum().sort_values(ascending=False)
result = df["category_id"].value_counts()

df["len_title"] = df["title"].apply(len)
result = df[["title","len_title"]]

df["tag_count"] = df["tags"].str.split("|").apply(len)
df["tag_count"] = df["tags"].apply(lambda x : len(x.split("|")))
result = df

def like_dislike(df):
    likesList = list(df["likes"])
    dislikesList = list(df["dislikes"])
    zipped_list = zip(likesList, dislikesList)
    ratioList = []
    for i, j in zipped_list:
        if i + j == 0:
            ratioList.append(0)
        else:
            ratioList.append(i / (i + j))
    return ratioList

df["like-dislike"] = like_dislike(df)

result = df.sort_values(by="like-dislike", ascending=False)[["title","likes","dislikes","like-dislike"]]

print(result)

