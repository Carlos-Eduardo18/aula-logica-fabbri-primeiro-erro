# Exemplo de código para tratamento de erros em python

from typing import final


try:
  a = int(input("Digite um numerador:"))
  b = int(input("Digite um denominador"))
  res = a / b

except ZeroDivisionError:
  print("Não é permitido divisão por zero")
except KeyboardInterrupt:
  print("\n O usuároo optou por não informar nada ...")
except (ValueError, NameError):
  print("Digite um número inteiro")
except Exception as erro:
  print(f"O erro encontrado foi {erro.__class__}")
else:
  print(f"O resultado de {a} / {b} é {res}")
finally:
  print("A prática leva a perfeição. \nContinue assim...\o/")

# Adicionado o git e o github aqui