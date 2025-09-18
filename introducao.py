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