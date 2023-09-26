# Certifica-se de receber um número de cpf correto para execução
while (True):
  user_cpf = input('Digite cpf a ser validado: ')

  if not (user_cpf.isnumeric()):
    print('Digite apenas números. \n')
    continue
  elif len(user_cpf) < 11 or len(user_cpf) >= 12:
    print('Um CPF precisa ter 11 dígitos, por favor, tente novamente! \n')
    continue
  else:
    break

# Variável secundária, em forma de lista; remove os dois últimos díg. inseridos pelo usuário
new_cpf_list = list(user_cpf)
new_cpf_list.pop(-2)
new_cpf_list.pop(-1)

# Inicialização de variáveis
first_digit = 0
second_digit = 0
cpf_returned = ''


# Função que encontra os dois dígitos verificadores:
def find_digits(cpf, digit, peso=0):
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
first_digit = find_digits(new_cpf_list, first_digit, 1)
new_cpf_list.append(str(first_digit))

# Chamada da função para encontrar o 2º dígito verificador, depois adiciona o díg. à variável
second_digit = find_digits(new_cpf_list, second_digit)
new_cpf_list.append(str(second_digit))

# Retornar o cpf para uma string
for i in new_cpf_list:
  cpf_returned += str(i)

# Comparação do cpf+os dígitos encontrados com o cpf inserido pelo usuário
print('=' * 15)
if cpf_returned == user_cpf:
  print('CPF válido')
else:
  print('CPF inválido')
print('=' * 15)
