with open('arquivo.txt', 'w') as arquivo:
    #Escreve informações em arquivo de texto externo
    arquivo.write("Programacao em Python")
    arquivo.write(" Escrita em texto externo")

with open('arquivo.txt', 'r') as arquivo:
    #Leitura de informações em arquivo de texto externo
    mensagem = arquivo.read()
    print(mensagem)