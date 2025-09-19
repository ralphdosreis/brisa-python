#Bloco try-except
try:
  numero_texto = '123'
  numero = 456
  soma = numero_texto + numero
except TypeError as e:
  print(f"Erro: {e}")

#Variação do Except (except composto)
try:
  numero_inicial = 5
  resultado = 10 / numero_inicial
except ValueError as value_error:
  print(f"Erro de valor: {Value_error}")
except ZeroDivisionError as zero_division_error:
  print(f"Erro de Divisão por zero: {zero_division_error}")
except Exception as exception:
  print(f"Erro generico: {exception}")
else:
  print(f"Resultado: {resultado}")

try:
  nome = "Eduardo Guedes"
  for caractere in nome:
    if '0' <= caractere <= '9':
      raise ValueError("O nome nao pode conter numeros.")
  print(f"Nome digitado: {nome}")
except ValueError as e:
  print(f"Erro: {e}")
finally:
  print("Exemplo completo de utilizacao do tratamento de excecoes")


try:
  nome = "123"
  for caractere in nome:
    if '0' <= caractere <= '9':
      raise ValueError("O nome nao pode conter numeros.")
  print(f"Nome digitado: {nome}")
except ValueError as e:
  print(f"Erro: {e}")
finally:
  print("Exemplo completo de utilizacao do tratamento de excecoes")