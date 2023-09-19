# Certifica-se de receber um número de cpf correto para execução
while (True):
  userCpf = input('Digite cpf a ser validado: ')

  if not (userCpf.isnumeric()):
    print('Digite apenas números. \n')
    continue
  elif len(userCpf) < 11 or len(userCpf) >= 12:
    print('Um CPF precisa ter 11 dígitos, por favor, tente novamente! \n')
    continue
  else:
    break

# Variável secundária, em forma de lista; remove os dois últimos díg. inseridos pelo usuário
newCpfList = list(userCpf)
newCpfList.pop(-2)
newCpfList.pop(-1)

# Inicialização de variáveis
firstDigit = 0
secondDigit = 0
cpfReturned = ''


# Função que encontra os dois dígitos verificadores:
def findDigits(cpf, digit, peso=0):
  i = peso
  resultado = 0

  for d in cpf:
    d = int(d)
    resultado += d * i
    i = i + 1

  digit = resultado % 11
  if digit == 10:
    digit = 0

  return digit


# Chamada da função para encontrar o 1º dígito verificador, depois adiciona esse díg. à variável
firstDigit = findDigits(newCpfList, firstDigit, 1)
newCpfList.append(str(firstDigit))

# Chamada da função para encontrar o 2º dígito verificador, depois adiciona o díg. à variável
secondDigit = findDigits(newCpfList, secondDigit)
newCpfList.append(str(secondDigit))

# Retornar o cpf para uma string
for i in newCpfList:
  cpfReturned += str(i)

# Comparação do cpf+os dígitos encontrados com o cpf inserido pelo usuário
print('=' * 15)
if cpfReturned == userCpf:
  print('CPF válido')
else:
  print('CPF inválido')
print('=' * 15)
