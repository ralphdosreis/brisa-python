nota = 75
if nota >= 90:
    print("A nota é A.")
elif nota >= 80:
    print("A nota é B.")
elif nota >= 70:
    print("A nota é C.")
else:
    print("A nota é D.")


frutas = ["maça", "banana", "laranja"]
for fruta in frutas:
    print(fruta)

contador = 0
while contador < 5:
    print("Contagem:", contador)
    contador += 1

valor = 1
while valor <= 100:
    print("Valor:", valor)
    valor *= 2

numeros = [1,2,3,4,5,6,7,8,9,10]
for numero in numeros:
    if numero % 2 == 0:
        print(numero, "é par!")
    else:
        print(numero, "é ímpar!")
nome = "Eduardo"
sobrenome = "Sei"
mensagem = "Bem-vindos à lógica de programação, \n" +\
            "o professor " +\
            nome +\
            "" +\
            "\nlhes deseja um bom estudo."
print(mensagem)

maior_idade = True
permitir_acesso = False

PI = 3.14159
TAXA_JUROS = 0.059

soma = 5 + 7
subtracao = 7 - 5
multiplicacao = 5 * 7
divisao = 10 / 5
resto_divisao = 7 % 3
potencia = 7 ** 3

variavel_A = 10
variavel_B = 10

igualdade = variavel_A == variavel_B
diferenca = variavel_A != variavel_B
maior = variavel_A > variavel_B
menor = variavel_A < variavel_B
maior_igual = variavel_A >= variavel_B
menor_igual = variavel_A <= variavel_B


a = True
b = False

resultado = a and b
print(resultado)

resultado = a or b
print(resultado)

resultado = not a
print(resultado)

x = True
y = False
z = True

resultado = (x and y) or (not z)
print(resultado)

numeros = [1,2,3,4,5]
nomes = ["Eduardo", "Luis", "Carol"]
pi = 3.14
lista_mista = [1, "Eduardo", pi]

coordenadas = (1,5)
dados_cadastro = ("Eduardo", 34, \
                  "eduardo_sei@example.com")

cadastro_usuario = {"nome": "Eduardo", \
                    "idade": 34, \
                    "altura": 1.70}

endereco = {"rua": "Rua A", "cidade": \
            "São Paulo", \
            "sigla": "SP"}

print(cadastro_usuario)
print(endereco)

presente_na_lista = 10 in \
                    [2,4,6,8,10]

nao_presente_na_lista = 11 not in \
                        [2,4,6,8,10]

print(presente_na_lista)
print(nao_presente_na_lista)

import array
primeiro_array = array.array('i', \
                             [1,2,3,4,5])

print(primeiro_array)

matriz = [[1,2,3],
          [4,5,6],
          [7,8,9]]

print(matriz)

lista = [["Arroz", "Feijao", "Salada"],
         ["Carne", "Frango", "Peixe"],
         ["Agua", "Suco", "Refrigerante"]]

for linha in lista:
    print(linha)

primeira_lista = [1,2,3, "abc", True]
primeira_lista.append(5)
primeira_lista.remove(1)

print(primeira_lista)

# primeiro_dicionario = {"nome": "Eduardo", \
#                        "idade": 34, \
#                         "cidade": "São Paulo"}
# print("Nome:", primeiro_dicionario["nome"])
# print("Idade:", primeiro_dicionario["idade"])
# print("Cidade:", primeiro_dicionario["cidade"])

# primeiro_dicionario["Profissao"] = "Professor"
# print(primeiro_dicionario)

pilha = []

pilha.append(1)
pilha.append(2)
pilha.append(3)

# item_desempilhado - pilha.pop()
# print("Item desempilhado:", item_desempilhado)

# item_desempilhado - pilha.pop()
# print("Item desempilhado:", item_desempilhado)

if len(pilha) > 0:
    topo_da_pilha = pilha[-1]
    print("Topo da pilha:", topo_da_pilha)
else:
    print("A pilha está vazia.")


# Orientação a objetos
class usuario:
  def __init__(self, nome, idade):
    self.nome = nome
    self.idade = idade

  def mensagem(self):
    return f"Bem-vindo, meu nome é \
      {self.nome} tenho \
      {self.idade} anos."
  
pessoa1 = usuario("Eduardo", 34)
pessoa2 = usuario("Luis", 39)

print(pessoa1.nome)
print(pessoa1.idade)
print(pessoa1.mensagem())


# Encapsulamento: Conta Bancária
class conta_bancaria:
  def __init__(self, saldo):
    self.__saldo = saldo
  def depositar(self, valor):
    self.__saldo += valor
  def sacar(self, valor):
    if self.__saldo > valor:
      self.__saldo -= valor
    else:
      print("Saldo insuficiente.")

  def get_saldo(self):
    return self.__saldo
  
conta = conta_bancaria(1000)
print("Saldo Inicial:", conta.get_saldo())
conta.depositar(500)
print("Novo saldo:", conta.get_saldo())
conta.sacar(300)
print("Saldo após o saque:", conta.get_saldo())


# Herança: Veículo e Carro
class veiculo:
  def __init__(self, marca, modelo):
    self.marca = marca
    self.modelo = modelo
class carro(veiculo):
  def __init__(self, marca, modelo, cor):
    super().__init__(marca, modelo)
    self.cor = cor
  def info(self):
    print(f"Carro: {self.marca} {self.modelo}, Cor: {self.cor}")

# Uso das classes
carro1 = carro("Toyota", "Corrola", "Prata")
carro1.info()


# Polimorfismo: Animais
class animal:
  def falar(self):
    pass
class cachorro(animal):
  def falar(self):
    return "Au au!"
class gato(animal):
  def falar(self):
    return "Miau!"

# Uso das classes
animais = [cachorro(), gato()]

for animal in animais:
  print(animal.falar())

class pessoa:
  def __init__(self,nome,idade):
    self._nome = nome
    self._idade = idade
  def apresentar(self):
    return f"Olá, meu nome é {self._nome} e tenho {self._idade} anos."
class estudante(pessoa):
  def __init__(self, nome, idade, curso):
    super().__init__(nome, idade)
    self._curso = curso
  def apresentar(self):
    return f"Oi, sou {self._nome}, um estudante de {self._curso}."

# Uso de classes
pessoa = pessoa("Eduardo", 34)
print(pessoa.apresentar())

estudante = estudante("Luis", 20, "Computação")
print(estudante.apresentar())


# Declaração de variáveis
idade = 30
altura = 1.70
nome = "Eduardo"
ativo_para_acesso = True
restricao = False

# Impressao das variáveis
print("Idade:", idade)
print("Altura:", altura)
print("Nome:", nome)
print("AtivoParaAcesso:", ativo_para_acesso)
print("Restricao:", restricao)

# Declaração de variáveis
idade = 30
nome = "Eduardo"

# Atribuição de novos valores
idade = 45
nome = "Luis"

# Imprimir variáveis
print("Nome:", nome)
print("Idade:", idade)

# Variáveis global
nome_global = "Eduardo"

def funcao_local():
  # Variável Local
  nome_local = "Luis"
  print("Dentro da função local, " \
        + "" \
        + "o nome é: ", nome_local)
# Chamando a função
funcao_local()

# Acesso à variável global
print("Fora da função, " \
      + "" \
      + "o nome_global é: ", nome_global)

# Declaração da variável
variavel_a = 10
variavel_b = 3

# Operadores Aritméticos
soma = variavel_a + variavel_b
subtracao = variavel_a - variavel_b
multiplicacao = variavel_a * variavel_b
divisao = variavel_a / variavel_b
divisao_inteira = variavel_a // variavel_b
resto = variavel_a % variavel_b
potencia = variavel_a ** variavel_b

print("Soma:", soma)
print("Subtracao:", subtracao)
print("Multiplicacao:", multiplicacao)
print("Divisao:", divisao)
print("DivisaoInteira:", divisao_inteira)
print("Resto:", resto)
print("potenciacao:", potencia)

# Inicialização de variáveis
variavel_a = 10
variavel_b = 5

# Execução dos operandos de comparação
igual = variavel_a == variavel_b
print("Operador de igualdade:", igual)

diferente = variavel_a != variavel_b
print("Operador de diferenca:", diferente)

maior = variavel_a > variavel_b
print("Operador maior:", maior)

menor = variavel_a < variavel_b
print("Operador menor:", menor)

maior_igual = variavel_a >= variavel_b
print("Operador maior e igual:", maior_igual)

menor_igual = variavel_a <= variavel_b
print("Operador menor e igual:", menor_igual)


# Inicialização de variáveis
idade = 25
maior_idade = 18
renda = 30000
renda_base = 25000

# Execução das operações lógicas
elegivel = idade >= maior_idade and renda >= renda_base
print("Saida do operador AND: ", elegivel)

# Atualização de valores
renda = 2000

elegivel = idade >= maior_idade or renda >= renda_base
print("Saida do operador OR: ", elegivel)


elegivel = idade >= maior_idade and not renda >= renda_base
print("Saida do operador NOT: ", elegivel)

# Atualização de valores
renda = 30000

elegivel = idade >= maior_idade and not renda >= renda_base
print("Saida do operador NOT: ", elegivel)


# Criação das listas para aplicação dos operandos de identidade
lista_1 = [1,2,3]
lista_2 = lista_1
lista_3 = [4,5,6]

# Execução dos operadores
mesmo_objeto = lista_1 is lista_2
print("Objetos iguais? ", mesmo_objeto)

objeto_diferente = lista_1 is not lista_3
print("Objetos diferentes? ", objeto_diferente)

# Ordem de precedência - PEMDAS (Parêntese, Exponenciação, Multiplicação, Divisão, Adição e Subtração)
# Inicialização das variáveis
nota_a = 10
nota_b = 10
nome = "Eduardo"
sobrenome = "Sei"

# Execução da estrutura para impressão em tela
nome_completo = nome + " " + sobrenome
print("Qual o nome do desenvolvedor: ", nome_completo)

media = nota_a + nota_b / 2
print("Media das notas sem PEMDAS: ", media)

media = (nota_a + nota_b) / 2
print("Media das notas com PEMDAS: ", media)

#Inicialização das variáveis
nota_escola = 7
nota_aluno = 7

if(nota_aluno >= nota_escola):
  print("Aprovado")
else:
  print("Reprovado")


# Inicialização de listas
lista_numeros = [1,2,3,4,5]
lista_strings = ['a', 'b', 'c', 'd']
lista_mista = [10, 'Oi', 3.14, True]
lista_vazia = []

# Implementação e execução das listas
# Listas podem ser entendidas como sequências mutáveis, ou seja, sequências que podemos modificar e que possuímos o controle de ordenamento dos dados.
print("Numeros: ", lista_numeros)
print("Informacoes: ", lista_strings)
print("Mista: ", lista_mista)
print("Vazia: ", lista_vazia)


# Inicialização de tuplas
tupla_1 = (1,2,3)
tupla_2 = 'a', 'b', 'c'
tupla_mista = (10, 'hello', 3.14)
tupla_vazia = ()

# Implementação e execução das tuplas
# As tuplas possuem caráter imutável, ou seja, os valores alocados não podem ser alterados durante a sua execução. 
print("Tupla1: ", tupla_1)
print("Tupla2: ", tupla_2)
print("TuplaMista: ", tupla_mista)
print("TuplaVazia: ", tupla_vazia)

# Inicialização de conjuntos
# Em conjuntos, possuímos uma estrutura única, imutável e não ordenada de informações.
conjunto_1 = {1,2,3}
conjunto_2 = set([3,4,5])
conjunto_vazio = set()

# Implementação e execução dos conjuntos
print("Conjunto 1: ", conjunto_1)
print("Conjunto 2: ", conjunto_2)
print("Conjunto Vazio: ", conjunto_vazio)


# Inicialização do dicionário
# Se trata de uma estrutura de dados complexa para armazenar um conjunto de pares chaves-valor, as chaves são únicas e o valor pode ser duplicado. 
pessoa = {
  'Nome': 'Eduardo',
  'Idade': 34,
  'Cidade': 'São Paulo'
}

#Implementação e execução do dicionário
print("Idade da Pessoa: ", pessoa['Idade'])

# Inicialização da lista
nomes = ['Eduardo', 'Amanda', 'Luis']

# Execução do loop for
for nome in nomes:
  print(nome)

# Execução do loop for
for numero in range(1,6):
  print(numero)

#Inicializador da variável
contador = 5

#Execução do loop for
while contador > 0:
  print(contador)
  contador -= 1

#Declaração de função
def soma(a, b):
  resultado = a + b
  return resultado

print("O resultado da soma dos numeros e: ", soma(1,3))

def minha_funcao():
  variavel_local = 10
  print(variavel_local)

minha_funcao()
# print(variavel_local) # Erro, a variável não pode ser acessada

variavel_global = 20

def minha_funcao():
  print(variavel_global)

minha_funcao()
print(variavel_global)

import math as matematica # Importação um módulo e a atribuicao de um apelido a ele com as
x = matematica.sqrt(4)
print(x)

from math import sqrt #Importação de partes específicas
raiz = sqrt(25)
print(raiz)

from math import * #“*” para indicar que queremos carregar todas as funções e classes presentes em math. 
expo = exp(5) # e (numero de Euler) elevado a 5
print(expo)

# Namespace Embutido (ou Built-In): Se refere ao conjunto de nomes que são automaticamente disponíveis em qualquer programa Python. O diferencial deste tipo de namespace é a característica de não precisar importar nomes para implementar suas funções.

#Usando funções built-in
numero = 42
print("Numero binario: ", bin(numero))
print("Numero absoluto: ", abs(numero))

# Usando objetos built-in
lista = [1,2,3,4,5]
print("Comprimento da lista: ", len(lista))
print("Tipo de variavel 'lista': ", type(lista))