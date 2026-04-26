import pandas as pd
data = [[1, 'sumit', 20], [2, 'manish', 20], [3, 'neha', 20], [4, 'aditiya', 20], [5, 'mahak', 20]]

df = pd.DataFrame(columns = ['id', 'name', 'age'])
for i in range(5):
    df.loc[df.shape[0]] = data[i]

df.insert(loc = df.shape[1], value = (1, 2, 3, 4, 5), column = 'cheni')
print(df)
print(df.shape)

# print(df[df['id'] == 3][['name', 'age']])

print(df['id'] == 3)


