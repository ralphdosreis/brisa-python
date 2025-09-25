#class pessoa:
    #Criação de atributos para pessoa
#    nome_pessoa = ""
#    idade_pessoa = 00
#    def falar_pessoa(self, falar_nome,falar_idade):
#       self.falar_nome = nome_pessoa
 #       self.falar_idade = idade_pessoa

class veiculo:
    #Criação de atributos para veiculo
    marca_veiculo = ""
    modelo_veiculo = ""
    def falar_veiculo(self, falar_marca, falar_modelo):
        self.falar_marca = marca_veiculo
        self.falar_modelo = modelo_veiculo

class animal:
    #Criação de atributos para animal
    nome_animal = ""
    tipo_animal = ""
    def falar_animal(self, falar_nome, falar_tipo):
        self.falar_nome = nome_animal
        self.falar_tipo = tipo_animal


#Criação dos objetos
#pessoa_1 = pessoa()
#pessoa_1.nome_pessoa = "Eduardo"

veiculo_1 = veiculo()
veiculo_1.marca_veiculo = "BMW"

animal_1 = animal()
animal_1.tipo_animal = "Aquático"

#Impressão dos objetos na tela
#print(pessoa_1.nome_pessoa)
print(veiculo_1.marca_veiculo)
print(animal_1.tipo_animal)


class pessoa:
    def __init__(self, nome):
        self.nome = nome
    def falar(self):
        pass
class coordenador(pessoa):
    def falar(self):
        return f"Eu, {self.nome} sou o coordenador"
class gerente(pessoa):
    def falar(self):
        return f"Eu, {self.nome} sou o gerente"
#Declaração dos objetos
pessoa_1 = coordenador("Eduardo")
pessoa_2 = gerente("Luis")

#Impressão dos objetos
print(pessoa_1.nome)
print(pessoa_1.falar())

print(pessoa_2.nome)
print(pessoa_2.falar())


#Declaração da superclasse
class veiculo:
    def __init__(self, marca, modelo):
        self.__marca = marca #Privado
        self.__modelo = modelo #Privado
    def get_info(self):
        return f"Marca: {self.__marca}, Modelo: {self.__modelo}"

#Subclasse e reutilização(Polimorfismo) do método __init__
class carro(veiculo):
    def __init__(self, marca, modelo, ano):
        super().__init__(marca, modelo)
        self.__ano = ano #Privado

    def get_info(self):
        return f"Tipo: Carro, {super().get_info()}, Ano: {self.__ano}"
    
#Polimorfismo aplicado ao método
def exibir_info_veiculo(veiculo):
    print(veiculo.get_info())

#Objeto criado
carro_1 = carro("Mitsubishi", "Lancer", 2023)
carro_2 = carro("Subaru", "WRX", 2023)

exibir_info_veiculo(carro_1) #Saida da função com Polimorfismo
exibir_info_veiculo(carro_2) #Saida da função com Polimorfismo
