import csv



#Abrir um arquivo CSV para leitura
with open("arquivo_dados.csv", "r", newline='') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv)

#Iterar pelas linhas do arquivo
for linha in leitor_csv:
    print(f'Nome: {linha[0]}, \
          Idade: {linha[1]}, \
          Cidade: {linha[2]}')