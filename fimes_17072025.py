import pandas as pd
import seaborn as sns



tmdb = pd.read_csv("https://raw.githubusercontent.com/alura-cursos/data-science-analise-exploratoria/main/Aula_0/tmdb_5000_movies.csv")

#print(tmdb.head())
print(sns.displot(tmdb["revenue"]))


