import os
import shutil

#Criação de diretório
os.mkdir("programacao_python")

#Verificar se o diretório existe
if os.path.exists("programacao_python"):
    print("Diretório existente")
else:
    print("O diretório não existe")

#Lista as informações de um diretório
arquivos_diretorios = os.listdir("programacao_python")
for arquivo_diretorio in arquivos_diretorios:
    print(arquivo_diretorio)

#Remover o diretório
os.rmdir("programacao_python")




#Cópia diretórios
shutil.copytree("programacao_python", "python_programacao")

#Movimentação de diretórios
shutil.move("programacao_python", "python_programacao")

#Exclusão de diretórios
shutil.rmtree("programacao_python")