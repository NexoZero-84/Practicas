import pandas as pd

df = pd.read_csv(r'Pandas\age_at_mar.csv', index_col=0)
print(df.head(15))
# En estas encuestas podemos hacer un condicion simple como:
# edad menores 25, edad mayor o igual a 18, edad igual a 30
print('\nMayores de 18:\n',df.loc[df['age'] > 18].head(15))

# También se pueden hacer condiciones compuestas como:
print('\nMayores de 18 y menores de 25:\n', df.loc[(df['age'] > 18) & (df['age'] < 25)].head(15))