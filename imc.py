import time
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


def mostrarsrc():
	print('\033[41m**!!MOSTRAR CÓDIGO FONTE!!**\033[m')
	try:
		arquivo = open(r'imc.py', 'r')
		print(arquivo.read())
		input('Presione ENTER para continuar')
		return main()
	except Exception as erro:
		print('Erro arquivo: ' + str(erro))
	finally:
		arquivo.close()



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
	try:
		arquivo = open(r'Histórico IMC.html', 'a')
		arquivo.write('<p>')
		arquivo.write(str(imc))
		arquivo.write((4 * '- 	 -') + str(time.asctime()))
		arquivo.write('</p>')
		arquivo.write('<br>')
	except Exception as erro:
		print('Erro arquivo: ' + str(erro))
	finally:
		arquivo.close()
	input('Presione ENTER para continuar')
	
	return main()

def supersecretarea():
	print('\033[41m**!!ÁREA SUPER SECRETA!!**\033[m')
	try:
		arquivo = open(r'Histórico IMC.html', 'a')
		arquivo.write('<h1 style="color:red">Você achou a área super secreta!!</h1>\n')
		arquivo.write('<div style="width: 0px;height: 0px;border-right: 60px solid transparent;border-top: 60px solid red;border-left: 60px solid red;border-bottom: 60px solid red;border-top-left-radius: 60px;border-top-right-radius: 60px;border-bottom-left-radius: 60px;border-bottom-right-radius: 60px;"></div>\n')
		arquivo.write('<div style="width: 0px;height: 0px;border-right: 60px solid transparent;border-top: 60px solid red;border-left: 60px solid red;border-bottom: 60px solid red;border-top-left-radius: 60px;border-top-right-radius: 60px;border-bottom-left-radius: 60px;border-bottom-right-radius: 60px;"></div>\n')
		arquivo.write('<div style="width: 0px;height: 0px;border-right: 60px solid transparent;border-top: 60px solid red;border-left: 60px solid red;border-bottom: 60px solid red;border-top-left-radius: 60px;border-top-right-radius: 60px;border-bottom-left-radius: 60px;border-bottom-right-radius: 60px;"></div>\n')
		arquivo.write('<div style="width: 0px;height: 0px;border-right: 60px solid transparent;border-top: 60px solid red;border-left: 60px solid red;border-bottom: 60px solid red;border-top-left-radius: 60px;border-top-right-radius: 60px;border-bottom-left-radius: 60px;border-bottom-right-radius: 60px;"></div>\n')
		arquivo.write('<div style="width: 0px;height: 0px;border-right: 60px solid transparent;border-top: 60px solid red;border-left: 60px solid red;border-bottom: 60px solid red;border-top-left-radius: 60px;border-top-right-radius: 60px;border-bottom-left-radius: 60px;border-bottom-right-radius: 60px;"></div>\n')
		input('Presione ENTER para continuar')
		return main()
	except Exception as erro:
		print('Erro arquivo: ' + str(erro))
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
		elif escolha == 88:
			return mostrarsrc()
		else:
			print('Comando não encontrado, tente novamente')
			return main()
	except ValueError:
		print('Digite apenas números, tente novamente')
		return main()
	except Exception as erro:
		print('Erro encontrado: ' + str(erro))

try:
	arquivo = open(r'Histórico IMC.html', 'a')
	arquivo.write('<h1 style="color:blue">Histórico de IMCs Calculados</h1>\n')
except Exception as erro:
	print('Erro arquivo: ' + str(erro))
finally:
	arquivo.close()

main()
