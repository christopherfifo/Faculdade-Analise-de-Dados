# EXPLICAÇÃO DO CODIGO

Como eu escolhi um arquivo xlsx (Excel), primeiro momento tive que selecionar a database e pular as primeiras linhas da tabela e selecionar a planilha a ser lida, pois havia uma apresentação da base de dados.

```py
dados = pd.read_excel(
    "PLANILHA DE TERCERIZADOS - FEVEREIRO 2024.xlsx",
    sheet_name="COLABORADORES",
    skiprows=4,
    header=0
)
```

Após isso, tratei as possveis colunas e linhas vazias, além de conferir o resultado

```py
dados = dados.dropna(how="all", axis=1)

dados = dados.dropna(how="all")

display(dados)
```

Por ultimo transformei o arquivo em csv e salvei, além de exibir novamente

```py
dados.to_csv("tercerizados_limpos.csv", index=False, encoding="utf-8-sig")

dados = pd.read_csv("tercerizados_limpos.csv")
dados.head(10)
```