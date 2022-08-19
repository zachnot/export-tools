from pandas import read_csv as read
from pandas import isnull as isnull 

isnotnull = lambda x: not isnull(x)
df = read("data/mcolumns.csv", encoding="unicode_escape")

for i, row in df.iterrows():
    stack = ""
    for j, column in enumerate(row):
        if (j>1 and isnotnull(column)):
            stack += column
            stack += "\n"
    df["Unnamed: 30"][i] = stack

for i, c in enumerate(df.columns):
    if i == 0:
        continue
    if i == 1:
        continue
    if i == 30:
        continue
    df.drop(c, inplace=True, axis=1)

df.rename(columns={"Unnamed: 30": "Screen3"}, inplace=True)
df.to_csv('fixedmcolumns.csv')


