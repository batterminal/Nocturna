# Faça um programa que peça um numero e mostre a mensagem: O número informado foi (numero):

numb = int(input("Digite um número: "))
print("O número digitado foi:", numb)

# Faça um programa que peça dois números e imprima a soma

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
soma = a + b
print("A soma dos números é: ", soma)

# Faça um Programa que peça as 4 notas bimestrais e mostre a média. 

nt1 = float(input("Primeira nota: "))
nt2 = float(input("Segunda nota: "))
nt3 = float(input("Terceira nota: "))
nt4 = float(input("Quarta nota: "))

media = (nt1 + nt2 + nt3 + nt4) / 4
print("A média das notas é: ", media)

# Faça um Programa que converta metros para centímetros

m = float(input("Valor em metros: "))
cm = m * 100
print("O valor em centímetros é: ", cm,"cm", sep="")

# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área. 

raio = float(input("Digite o valor do raio: "))
area = 3.14 * (raio ** 2)
print("A área do círculo é: ", area)

# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário

lado = float(input("Digite o valor do lado do quadrado: "))
area = lado ** 2
dobro_area = area * 2
print("A área do quadrado é: ", area)
print("O dobro da área do quadrado é: ", dobro_area)

# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

ganho_por_hora = float(input("Quanto você ganha por hora? R$"))
horas_trabalhadas = float(input("Quantas horas você trabalha por mês? "))
salario = ganho_por_hora * horas_trabalhadas
print("O seu salário no mês é: R$", salario, sep="")

# Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius. C = (5 * (F-32) / 9). 

F = float(input("Digite a temperatura em graus Farenheit: "))
C = 5*(F - 32) / 9
print("A temperatura em graus Celsius é: ", C, "°C", sep="")

# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit. 

C = float(input("Digite a temperatura em graus Celsius: "))
F = (C * 9/5) + 32
print("A temperatura em graus Farenheit é: ", F, "°F", sep="")

# Elaborar um algoritmo que efetue a apresentação do valor da conversão em real (R$) de um valor lido em dólar (US$). O algoritmo deverá solicitar o valor da cotação do dólar e também a quantidade de dólares disponíveis com o usuário.

cotacao_dolar = float(input("Digite a cotação do dólar: R$"))
valor_em_dolar = float(input("Digite o valor em dólar: US$"))
valor_em_real = cotacao_dolar * valor_em_dolar
print("O valor em real é: R$", valor_em_real, sep="")

# Faça um algoritmo que receba um valor que foi depositado e exiba o valor com rendimento após um mês. Considere fixo o juro da poupança em 0,70% a. m.

valor_depositado = float(input("Digite o valor depositado: R$"))
rendimento = valor_depositado * 0.7 / 100
valor_em_real = valor_depositado + rendimento
print("O valor com rendimento é: R$", valor_em_real)

# A Loja Mamão com Açúcar está vendendo seus produtos em 5 (cinco) prestações sem juros. Faça um algoritmo que receba um valor de uma compra e mostre o valor das prestações.

valor_compra = float(input("Digite o valor da compra: R$"))
valor_prestacao = valor_compra / 5
print("O valor de cada prestação é: R$", valor_prestacao)

# Faça um algoritmo que receba o preço de custo de um produto e mostre o valor de venda. Sabe-se que o preço de custo receberá um acréscimo de acordo com um percentual informado pelo usuário.

preco_custo = float(input("Digite o preço de custo do produto: R$"))
acrescimo_percentual = float(input("Digite o percentual de acréscimo: "))
valor_venda = preco_custo + (preco_custo * acrescimo_percentual / 100)
print("O valor de venda do produto é: R$", valor_venda)

# Escrever um algoritmo para determinar o consumo médio de um automóvel sendo fornecida a distância total percorrida pelo automóvel e o total de combustível gasto.

distancia_percorrida = float(input("Digite a distância total percorrida pelo automóvel (em km): "))
combustivel_gasto = float(input("Digite o total de combustível gasto (em litros): "))
consumo_medio = distancia_percorrida / combustivel_gasto
print("O consumo médio do automóvel é: ", consumo_medio, "Km/L", sep="")

a = int(input("Valor de a: "))
b = int(input("Valor de b: "))
c = int(input("Valor de c: "))
r = (a + b) ** 2
s = (b + c) ** 2

soma = (r + s) / 2
print("O resultado da soma é: ", soma)

# Escrever um algoritmo que leia o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas, informar o seu nome, o salário fixo e salário no final do mês.

nome_vendedor = input("Digite o nome do vendedor: ")
salario_fixo = float(input("Digite o salário fixo do vendedor: R$"))
total_vendas = float(input("Digite o total de vendas efetuadas pelo vendedor no mês (em dinheiro): R$"))
comissao = total_vendas * 0.15
salario_final = salario_fixo + comissao
print("Nome do vendedor: ", nome_vendedor)
print("Salário fixo: R$", salario_fixo, sep="")
print("Salário final no mês: R$", salario_final, sep="")

# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre: o produto do dobro do primeiro com metade do segundo; a soma do triplo do primeiro com o terceiro; o terceiro elevado ao cubo.

num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))
num3 = float(input("Digite um número real: "))

produto = (2 * num1) * (num2 / 2)
soma = (3 * num1) + num3
cubo = num3 ** 3

print("O produto do dobro do primeiro com metade do segundo é: ", produto)
print("A soma do triplo do primeiro com o terceiro é: ", soma)
print("O terceiro elevado ao cubo é: ", cubo)

# Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) – 58.

altura = float(input("Digite a sua altura (em metros): "))
peso_ideal = (72.7 * altura) - 58
print("O seu peso ideal é: ", peso_ideal, "Kg", sep="")

# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em MBps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

tamanho_arquivo = float(input("Digite o tamanho do arquivo para download (em MB): "))
velocidade_internet = float(input("Digite a velocidade do link de Internet (em MBps): "))
tempo_download = tamanho_arquivo / velocidade_internet
download_minutos = tempo_download /  60
print("O tempo aproximado de download é: ", download_minutos, "minutos", sep="")

# Ler dois valores para as variáveis A e B, e efetuar as trocas dos valores de forma que a variável A passe a possuir o valor da variável B e a variável B passe a possuir o valor da variável A. Apresentar os valores trocados.

a = int(input("Valor de a: "))
b = int(input("Valor de b: "))
aux = a
a = b
b = aux
print("a = ", a, "b = ", b)

a = int(input("Valor de a: "))
b = int(input("Valor de b: "))

a,b = b,a

print("a = ", a, "b = ", b)

# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê: salário bruto. quanto pagou ao INSS, quanto pagou ao sindicato, o salário líquido, calcule os descontos e o salário líquido, conforme a tabela abaixo:
# Salário Bruto : R$
# IR (11%) : R$
# INSS (8%) : R$
# Sindicato ( 5%) : R$
# Salário Liquido : R$

valor_hora = float(input("Quanto você ganha por hora? R$"))
horas_trabalhadas = float(input("Quantas horas você trabalha por mês? "))
salario_bruto = valor_hora * horas_trabalhadas
desconto_ir = salario_bruto * 0.11
desconto_inss = salario_bruto * 0.08
desconto_sindicato = salario_bruto * 0.05
salario_liquido = salario_bruto - (desconto_ir + desconto_inss + desconto_sindicato)
print("Salário liquido: R$", salario_liquido, sep="")
