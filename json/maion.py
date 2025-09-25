import json

agenda = {
    "Nome": "Eduardo",
    "Idade": 30,
    "Cidade": "São Paulo"
}

with open('JSON_dados.json', 'w') as escrita_JSON:
    json.dump(agenda, escrita_JSON)

print("Dados JSON escritos com sucesso")


with open('JSON_dados.json', 'r') as leitura_JSON:
    info = json.load(leitura_JSON)

print(info)