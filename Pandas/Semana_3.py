import pandas as pd
df = pd.read_csv('C:\\Users\\leyva\\Documents\\Practicas CD\\Pandas\\netflix_titles.csv')
print(df[df['release_year'] == 2020].sort_values(by='description', ascending=False))