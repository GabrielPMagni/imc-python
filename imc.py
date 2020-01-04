#cálculo de IMC

def setInfo():
	try:
		peso = (input('Digite seu peso em kilogramas: '))
		altura = (input('Digite sua altura em metros ou centímetros: '))
		peso = float(peso.replace(',', '.'))
		altura = float(altura.replace(',', '.'))
		if altura < 4:
			return calcular(True, peso, altura)
		else:
			return calcular(False, peso, altura)
	except ValueError:
		print('Digite apenas números')
		return setInfo()
	except Exception as erro:
		print('Erro encontrado: ' + str(erro))
		return setInfo()


def calcular(decisao, peso, altura):
	if decisao:
		imc = (peso / (altura**2))
		return resultado(imc)
	else:	
		imc = (peso / ((altura/100)**2))
		return resultado(imc)



def resultado(imc):
	print('Seu IMC é: \033[36m' + str(imc) + '\033[m')
	if imc < 17:
		print('\033[31mVocê está muito abaixo do peso\033[m')
	elif imc < 18.49:
		print('\033[33mVocê está abaixo do peso\033[m')
	elif imc < 24.49:
		print('\033[32mVocê está com peso normal\033[m')
	elif imc < 29.49:
		print('\033[33mVocê está acima do peso\033[m')
	elif imc < 34.99:
		print('\033[31mVocê está com Obesidade grau I\033[m')
	elif imc < 39.99:
		print('\033[31mVocê está com Obesidade grau II (severa)\033[m')
	else:
		print('\033[31mVocê está com Obesidade grau III (mórbida)\033[m')
	continuar = input('Presione ENTER para continuar')
	return main()

def supersecretarea():
	print('\033[41m**!!ÁREA SUPER SECRETA!!**\033[m')

def historico():
	try:
		arquivo = open(r'Histórico IMC', 'a')
		arquivo.write()
	except Exception as erro:
		print('Erro: ' + str(erro))
	finally:
		arquivo.close()

def main():
	try:
		escolha = int(input('\033[46m***CALCULADORA DE IMC***\033[m\n\nEscolher:\n\n\t1>Calcular\n\t2>Sair\n\n\t\t>'))
		if escolha == 1:
			return setInfo()
		elif escolha == 2:
			exit()	
		elif escolha == 99:
			return supersecretarea()
		else:
			print('Comando não encontrado, tente novamente')
			return main()
	except ValueError:
		print('Digite apenas números, tente novamente')
		return main()
	except Exception as erro:
		print('Erro encontrado: ' + erro)


main()



