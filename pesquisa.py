maior_idade = 0
qtd_mulheres_verdes_louros = 0
num_habitantes = int(input("Informe o número de habitantes: "))
for _ in range(num_habitantes):
  sexo = input("Informe o sexo do habitante (M/F): ")
  if sexo == '-1':  # Verifica se foi inserido o valor de término
    break
  cor_olhos = input("Informe a cor dos olhos (azuis, verdes ou castanhos): ")
  cor_cabelos = input(
      "Informe a cor dos cabelos (louros, castanhos, pretos): ")
  idade = int(input("Informe a idade do habitante: "))
  if idade > maior_idade:
    maior_idade = idade
  # Verifica se é uma mulher com olhos verdes, cabelos louros e idade entre 18 e 35 anos
  if sexo == 'F' and 18 <= idade <= 35 and cor_olhos == 'verdes' and cor_cabelos == 'louros':
    qtd_mulheres_verdes_louros += 1
print("Maior idade dos habitantes:", maior_idade)
print(
    "Quantidade de mulheres com olhos verdes, cabelos louros e idade entre 18 e 35 anos:",
    qtd_mulheres_verdes_louros)
