import pandas as pd
from sklearn.preprocessing import MinMaxScaler

with open('abalone_attributes.txt', 'r') as f:
    columns = [line.strip() for line in f.readlines()]

df = pd.read_csv('abalone.txt', header=None)

label = df[0]
df = df.drop(columns=[0])

scaler = MinMaxScaler()
df = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)

print(label)
print(df)
