import pandas as pd

dados = pd.read_csv("https://raw.githubusercontent.com/alura-cursos/data-science-analise-exploratoria/main/Aula_0/ml-latest-small/ratings.csv")

# print(dados)

# print(dados.shape) # linhas e colunas da tabela

dados.columns = ["usuario","filme","nota","tempo"]

# print(dados["nota"]) # só coluna selecionada

# print(dados.head()) # por padrao as 5 primeiras


