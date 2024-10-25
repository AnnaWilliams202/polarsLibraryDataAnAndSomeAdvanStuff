import polars as pl

df = pl.read_csv('/Users/annawilliams/Desktop/filterindDataWithPolars/iris.csv')
print(df.head())
print(df.describe())

setosa = df.filter(pl.col('species')=='setosa')
print(setosa.head())

sepal_length= df.group_by('species').agg(pl.col('sepal_length').mean())
print(sepal_length)

setosa.write_csv('setosa.csv')